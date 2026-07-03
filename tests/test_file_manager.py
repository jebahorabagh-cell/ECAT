from app.services.file_manager import FileManager

fm = FileManager()

fm.add_files([
    r"E:\Test\File1.xlsx",
    r"E:\Test\File2.xlsx",
    r"E:\Test\File1.xlsx"
])

print("Total Files:", fm.count())

for file in fm.get_files():
    print(file)

fm.remove_file(0)

print("\nAfter Remove")

for file in fm.get_files():
    print(file)