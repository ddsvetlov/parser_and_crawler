import unittest
import web_parser
import docs_parser
import web_parser
import io
import os
from data import empty, special_docx, special_pdf, ru_pdf, ru_docx,\
				 eng_pdf, eng_docx, multi_pdf, multi_docx


class TestParser(unittest.TestCase):
  # docs test
  def test_emply_docx(self):
    self.assertEqual(docs_parser.docx_get_lines_ret("empty.docx"), empty)

  def test_empty_pdf(self):
    self.assertEqual(docs_parser.pdf_get_lines_ret("blank.pdf"), empty)

  def test_ru_pdf(self):
    self.assertEqual(docs_parser.pdf_get_lines_ret("ru_list.pdf"), ru_pdf)

  def test_ru_docx(self):
    self.assertEqual(docs_parser.docx_get_lines_ret("ru_list.docx"), ru_docx)

  def test_eng_pdf(self):
    self.assertEqual(docs_parser.pdf_get_lines_ret("eng_list.pdf"), eng_pdf)

  def test_eng_docx(self):
    self.assertEqual(docs_parser.docx_get_lines_ret("list_english.docx"), eng_docx)

  def test_special_docx(self):
    self.assertEqual(docs_parser.docx_get_lines_ret("special.docx"), special_docx)

  def test_special_pdf(self):
    self.assertEqual(docs_parser.pdf_get_lines_ret("special.pdf"), special_pdf)    

  def test_multi_docx(self):
     self.assertEqual(docs_parser.docx_get_lines_ret("multi_page.docx"), multi_docx)    

  def test_multi_pdf(self):  
     self.assertEqual(docs_parser.pdf_get_lines_ret("multi_page.pdf"), multi_pdf)    
  
  # web test
  def test_main_spbu(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/main_spbu.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_main_spbu.txt")))

  def test_main_msu(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/main_nsu.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_main_nsu.txt")))

  def test_msu_news(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/msu_news.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_msu_news.txt")))

  def test_msu_science(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/msu_science.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_msu_science.txt")))

  def test_spbu_univer(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/univer_spbu.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_spbu_univer.txt")))

  def test_spbu_student(self):
  	self.assertListEqual(list(io.open(os.getcwd()+"/result/student_spbu.txt")),
    					 list(io.open(os.getcwd()+"/web_test_data/test_student_spbu.txt")))


if __name__ == '__main__':
  unittest.main()