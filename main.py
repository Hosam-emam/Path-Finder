# def main():
#     print("Hello from path-finder!")


# if __name__ == "__main__":
#     main()

from gitingest import ingest

summary, tree, content = ingest(source="https://github.com/Hosam-emam/Face_Detection_App")

print(summary)
print(tree)
print(content)