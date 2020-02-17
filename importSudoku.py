import os


def SDKtoMatrix(filename):
    fileObject = open(filename, 'r')
    lines = fileObject.readlines()
    i = 0
    if len(lines) > 9:
        for i in range(len(lines)):
            if "[Puzzle]" in lines[i]:
                i += 1
                return [list(map(int, list(row.replace(".", "0").strip()))) for row in lines[i:i + 9]]
        return [list(map(int, list(row.replace(".", "0").strip()))) for row in lines[-9:]]
    fileObject.close()


def SStoMatrix(filename):
    fileObject = open(filename, 'r')
    lines = fileObject.readlines()
    if len(lines) > 9:
        for line in lines:
            if "-" in line:
                lines.remove(line)
    listReplacedStrings = [row.replace('.', '0').replace('|', '').replace('X', '0').strip() for row in lines]
    return [list(map(int, list(row))) for row in listReplacedStrings]

    fileObject.close()


def fileToMatrix(filename: str):
    base = os.path.basename(filename).lower().split(".")
    if base[-1] == "ss":
        return SStoMatrix(filename)
    if base[-1] == "sdk":
        return SDKtoMatrix(filename)
    raise Exception("File format not recognized")


def main():
    from sudokuSolver import pBo, solve
    #board = SDKtoMatrix("example1.sdk")
    #board = fileToMatrix("example1.ss")
    board = fileToMatrix("example0.sdkr")
    pBo(board)
    solve(board)
    pBo(board)


if __name__ == "__main__":
    main()
