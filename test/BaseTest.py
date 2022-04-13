import unittest
import pathlib
from src.FileRegistry import TestFileEnum, TempFileEnum
import shutil
from os.path import exists
from pathlib import Path
from src.pico8fileparser import Pico8FileParser


class BaseTest(unittest.TestCase):
    def assertContentsEqual(self, actual: str, expected: TestFileEnum):
        self.assertEqual(actual, self.getTestFileContents(expected))

    def assertFilesEqual(self, actual: TempFileEnum, expected: TestFileEnum):
        self.assertContentsEqual(
            actual=self.getTempFileContents(actual), expected=expected
        )

    # For the PICO-8 exports, no point in checking that the contents of the file
    # match (just setting ourselves up for unnecessary maintenance when PICO-8
    # changes). Just check if the file exists
    def assertFileExists(self, tempFile: TempFileEnum):
        self.assertTrue(
            exists(self.getTempFilePath(tempFile)),
            f"File {tempFile.value} ({tempFile}) does not exist",
        )

    def assertPathExists(self, path: Path):
        self.assertTrue(exists(path), f"File or folder {path} does not exist")

    def assertPathDoesNotExist(self, path: Path):
        self.assertFalse(
            exists(path), f"File or folder {path} does exist but was expected to"
        )

    def getTestFilePath(self, testFileName: TestFileEnum) -> pathlib.Path:
        # return testFileName.filepath
        return pathlib.Path("test/" + testFileName.value)

    def getTempFilePath(self, tempFileName: TempFileEnum) -> pathlib.Path:
        return pathlib.Path("tmp/" + tempFileName.value)

    @classmethod
    def getTempFolderPath(cls):
        return pathlib.Path("tmp/")

    def getTestFileContents(self, testFileName: TestFileEnum) -> str:
        with open(self.getTestFilePath(testFileName=testFileName)) as file:
            return file.read()

    def getTestFileBytes(self, testFileName: TestFileEnum) -> bytes:
        with open(self.getTestFilePath(testFileName=testFileName), "rb") as file:
            return file.read()

    def getTempFileBytes(self, tempFileName: TempFileEnum) -> bytes:
        with open(self.getTempFilePath(tempFileName), "rb") as file:
            return file.read()

    def getTempFileContents(self, tempFileName: TempFileEnum) -> str:
        with open(self.getTempFilePath(tempFileName), "r") as file:
            return file.read()

    def parseFile(self, testFile: TestFileEnum):
        return Pico8FileParser.parse(self.getTestFilePath(testFile))


#     tmp file
