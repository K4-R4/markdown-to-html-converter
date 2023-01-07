import markdown
import sys

def main():
    if len(sys.argv) != 4:
        print("入力が正しくありません")
        sys.exit()
    if sys.argv[1] == "markdown":
        try:
            inputpath = sys.argv[2]
            outputpath = sys.argv[3]
            with open(inputpath, "r") as f:
                contents = f.read()
            html = markdown.markdown(contents)
            with open(outputpath, "w") as f:
                f.write(html)
        except FileNotFoundError:
            print("入力ファイルが存在しません")
    else:
        print("無効なコマンドです")

if __name__ == "__main__":
    main()