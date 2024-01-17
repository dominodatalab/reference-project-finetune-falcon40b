import unittest
import os
import importlib.util

class TestFalcon40b(unittest.TestCase):

    def test_library_torch_installed(self):
        """ Test if pytorch library is installed """
        torch_installed = importlib.util.find_spec("torch") is not None
        self.assertTrue(torch_installed, "torch is not installed")

    def test_library_peft_installed(self):
        """ Test if peft library is installed """
        peft_installed = importlib.util.find_spec("peft") is not None
        self.assertTrue(peft_installed, "peft library is not installed")
        
    def test_library_datasets_installed(self):
        """ Test if datasets library is installed """
        datasets_installed = importlib.util.find_spec("datasets") is not None
        self.assertTrue(datasets_installed, "datasets library is not installed")
                
    def test_library_transformers_installed(self):
        """ Test if transformers library is installed """
        transformers_installed = importlib.util.find_spec("transformers") is not None
        self.assertTrue(transformers_installed, "transformers library is not installed")
        
    def test_library_bitsandbytes_installed(self):
        """ Test if bitsandbytes library is installed """
        bitsandbytes_installed = importlib.util.find_spec("bitsandbytes") is not None
        self.assertTrue(bitsandbytes_installed, "bitsandbytes is not installed")

if __name__ == '__main__':
    unittest.main()
