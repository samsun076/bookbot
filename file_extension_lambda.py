def categorize_file(filename):
    get_category = lambda extension: {
        ".txt": "Text",
        ".py": "Code",
        "docx": "Document,"
    }.get(extension, "Unknown")

    return get_category(filename[filename.rfind(".") :])



files = ["name.txt", "python.py", "excel.xls"]

for file in files:
    print(categorize_file(file))
