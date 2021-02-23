import os
import easygui


def main():
    directory = easygui.diropenbox(title="Chose directory")
    files = os.listdir(directory)
    files = [i for i in files if i.endswith('.pdf')]
    makeOCR(files, directory)


def makeOCR(paths, folder):
    for path in paths:

        out_path = f'output/{path}'
        os.system(f'ocrmypdf --skip-text {folder}/{path} {out_path}')
    print("Ready")


if __name__ == '__main__':
    main()
