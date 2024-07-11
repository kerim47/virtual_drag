import unittest
from unittest.mock import patch
from io import StringIO
from virtual_drag.main import main, process_file

class TestVirtualDrag(unittest.TestCase):

    @patch('sys.argv', ['main.py', 'test_file.txt'])
    @patch('builtins.open', return_value=StringIO('Test içerik'))
    def test_main_with_file(self, mock_open):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            self.assertIn("İşlenecek dosya: test_file.txt", fake_out.getvalue())
            self.assertIn("Dosya içeriği:\nTest içerik", fake_out.getvalue())

    @patch('sys.argv', ['main.py'])
    def test_main_without_file(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            self.assertIn("Lütfen bir dosya yolu belirtin.", fake_out.getvalue())

    def test_process_file_not_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            process_file('nonexistent_file.txt')
            self.assertIn("Hata: nonexistent_file.txt dosyası bulunamadı.", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()