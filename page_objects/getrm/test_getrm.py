import unittest
from nose2.tools import params
from GeTRM import GeTRM


expected_vals = { "1q24" : "Homo sapiens: GRCh37.p\d+\s+Chr\s1\s\WNC_000001.\d+\W:\s164.7\d+M\s-\s173.6\d+M",
                 "Neurofibromatosis" : "Homo sapiens: GRCh37.p\d+\s+Chr\s17\s\WNC_000017.\d+\W:\s29.6\d+M\s-\s29.\d+M"} 



class GetrmTestCase(unittest.TestCase):
    def setUp(self):
        self.getrm_page = GeTRM()
        self.getrm_page.open()

    @params(("1q24", "Homo sapiens: GRCh37.p\d+\s+Chr\s1\s\WNC_000001.\d+\W:\s164.7\d+M\s-\s173.6\d+M"),
            ("Neurofibromatosis", "Homo sapiens: GRCh37.p\d+\s+Chr\s17\s\WNC_000017.\d+\W:\s29.6\d+M\s-\s29.\d+M"))
    def test_getrm(self, term, expected_value):
        #for term, expected_val in expected_vals.iteritems():
        page = self.getrm_page
        page.search(term)
        page.result_arrow_should_exist()
        page.go_to_results()
        page.headers_should_match(expected_value)
            
    
    def tearDown(self):
        self.getrm_page.close()


if __name__ == "__main__":
    unittest.main()