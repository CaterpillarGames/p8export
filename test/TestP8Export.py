from src.p8export import P8Export

# from TestFileSystemOperations import TestFileSystemOperations
from BaseTest import BaseTest, TempFileEnum, TestFileEnum
import os
import shutil
from pathlib import Path


class TestP8Export(BaseTest):
    p8exportBaseDir: Path = BaseTest.getTempFolderPath() / "p8export-test"

    # super - soldiers
    # ORCHESTRATION_TEST_FILE
    @classmethod
    def setUpClass(cls) -> None:
        os.makedirs(cls.p8exportBaseDir, exist_ok=False)

    def setUp(self):
        self.currentTestFolder: Path = self.p8exportBaseDir / self._testMethodName
        os.makedirs(self.currentTestFolder, exist_ok=False)

    def test_folder_structure(self):
        templateDir: Path = self.currentTestFolder / "game-template"
        os.makedirs(templateDir)
        p8fileStart: Path = templateDir / "new-game.p8"
        shutil.copy(
            self.getTestFilePath(TestFileEnum.BASIC_GAME_TEMPLATE_FILE), p8fileStart
        )
        P8Export.export(p8fileStart)

        expectedGameDir = self.currentTestFolder / "mongo-bongo"

        self.assertPathExists(expectedGameDir)
        self.assertPathExists(expectedGameDir / "images/")
        self.assertPathExists(expectedGameDir / "images" / "itch-cover.png")
        self.assertPathExists(expectedGameDir / "images" / "cover.png")
        self.assertPathExists(expectedGameDir / "export/")
        self.assertPathExists(expectedGameDir / "mongo-bongo.p8")

    def test_optional_dir(self):
        pass