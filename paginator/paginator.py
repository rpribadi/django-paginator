#try:
#    from django.conf import settings
#except ImportError:
import settings

from django.core.paginator import Paginator as Pgtr, Page, PageNotAnInteger, EmptyPage

DEFAULT_RECORDS_PER_PAGE = getattr(settings, 'PAGINATOR_RECORDS_PER_PAGE', 20)
DEFAULT_TOTAL_PAGE_NAV = getattr(settings, 'PAGINATOR_TOTAL_PAGE_NAV', 5)
DEFAULT_TOTAL_JUMPER = getattr(settings, 'PAGINATOR_TOTAL_JUMPER', 3)
DEFAULT_RAISE_404_ON_INVALID_PAGE = getattr(settings, 'PAGINATOR_RAISE_404_ON_INVALID_PAGE', False)


class Paginator(Pgtr):
    def __init__(self, object_list, per_page, **kwargs):
        if not per_page:
            per_page = DEFAULT_RECORDS_PER_PAGE
        super(Paginator, self).__init__(object_list, per_page)

    def _get_delta(self):
        delta_left = int((DEFAULT_TOTAL_PAGE_NAV - 1 )/ 2)
        delta_right = DEFAULT_TOTAL_PAGE_NAV - delta_left - 1
        return delta_left, delta_right

    def _get_main_page_numbers(self, page):
        delta_left, delta_right = self._get_delta()
        start_page = page - delta_left
        end_page = page + delta_right
        print "PAGE", page
        print "DEFAULT_TOTAL_PAGE_NAV", DEFAULT_TOTAL_PAGE_NAV
        print "DELTA", delta_left, ' - ', delta_right

        # + 1 to include end_page
        return [i for i in range(start_page, end_page + 1)]

    def _get_left_jumpers(self, number):
        jumpers = []
        return jumpers

    def _get_right_jumpers(self, number):
        jumpers = []
        return jumpers

    def _get_page_nav(self, page):
        page_nav = []
        if self.num_pages <= DEFAULT_TOTAL_PAGE_NAV:
            page_nav = [i for i in range(1, self.num_pages + 1)]
        else:
            page_nav = self._get_main_page_numbers(page)
        return page_nav


if __name__ == "__main__":
    object_list = [
        "PFjaziDspkgCeZHJtBhYyuvTUOmKR",
        "oOHKmyzShUvlwRxgXedpqCGTZJbnB",
        "jWTVOcnAxCbqSQouYMhtGEXdzvimyrlRU",
        "jZsPoQTKbneNfDcVgMFJSWAXlU",
        "SUKuwQVtCPhFzJqWyOLbdfgMB",
        "DJcaQhUAtCfWrqnpMzHB",
        "kHnequwIbvNDfEmYKxgsLzo",
        "IjnBUvtTowfQEsuMlpDAaJyHkOWcFbS",
        "qHiroTltGjuwCIfMngycVmeBdOaNWsEvSpU",
        "zsLrxVnTqwMWFEgCbaSmBtlPjNdXuIy",
        "ZGfoezVtMNOPDaHiUTQxIvBuErcySkXYJRgLCn",
        "jlYqNAySVMCviDwBRxUehftLmaFGKsXbT",
        "aiAsTZSYCOEQXBGNUbkgJPxKlMwrvRjqzc",
        "yBDHRFowUfJpVNlhvPixskOMCYXTnQEtequWKZc",
        "HjwBOJVhvcNFAiWnrabmygoDPMlSdXs",
        "GvqOfeAxIMudpYwsHaLkQXrjScW",
        "AmcoxLOwdSvaUKCupsHebBkXlZqRJTNYIEDPFMfi",
        "veINcpDHAoQTrPnGasUYSZ",
        "YfhOvsJiXKQobFPkZInSlTUaAuENrHLe",
        "FadMrRuPIlJQAmwgsyZLSDj",
        "OydEAJUjCkfaplZKuctbVTLMBHWIwYeDPih",
        "lHcgShPdpExiAXvBDfkKYCaVs",
        "RewcWYgFKqTavzdprxEiAMjonuSOLsCQhmytkJBG",
        "GZPWNgsbTpSaAdrXIlmHvoVKQOFEJ",
        "iOyoCNFelPbaktwYKLVxGrUnvMXgcDBhHZzQf",
        "TfyehEQZWgNAbPSvGuBzjXLlqRYp",
        "pNuXUVSOmxYhMKDtTsEHWJZzvIil",
        "xadplqXkDmgzCZrotMchvbQRSwfNsIUyJKTFP",
        "OmnVxMILBJtwFXDykqKTvfbjGNuWlSZacoeQYH",
        "NAQsThdeXYKizVtcZCyxbGrJMIfOvjkRLBa",
        "ZuybqGSoLmxnWBXQzklfsrFEH",
        "zHyhmkLNVOPcwdxnortfW",
        "SwUGFPqBoOXughxrpDcCKtQlbeanEZvsIAM",
        "TnkJhMfydRribWCeaAPoBQKV",
        "QlAqVxPyOpserDztmGMnSFbdE",
        "QFpKdgztTqyNBlXJauwAGEPsDSWvrLmUiYoCxcIZ",
        "vNPxaRWDQdyEXMwnsoUpkOmlLbYruB",
        "QcbgyOTwlenKBapHPvrxqLNJhiEozkmYFCMS",
        "lecXOtydzrZQLnjNaqAgBVfSYPChERvJHM",
        "BtArWUZCwQSxhfkcFziJIdbHajgqTNY",
        "lQYWKfRdqipMJSkNrnLVHCTXUPZw",
        "oJREIQSqzkrKhiVyuLsgeldftpGP",
        "BZXmvCwiFdgzMlQeIDVaSrGbnf",
        "mvpabJAYunxZqzMBGScPoIRTjiOtVgsNWKF",
        "fHxECFlpZPvLumQrMXckTsdUytKjYGVOShNq",
        "gxwMuSNsayCjeKkLfAUZoVpEJliObGWcYTI",
        "AWLeFIvDuXmSBqyTwKHJptaobOPz",
        "GupWQeixZBfbHPYgvLMEcNVasKJjDnzSkTdX",
        "nGTkDoxAEdRKLfuCqlSNWeVh",
        "ismcApbNyfIVxuroHWgKG",
        "uqfxocMDKLOGPXTaRltgsByCvJYWNEZzkhbVmrUi",
        "hGamkPJfDtyUZlbKQOdTFMqp",
        "OVGEJMfKasrztWpDPvumCYkLTRZjUyn",
        "QksNVKXuUcrtDwYbxijMCZoB",
        "eFMEBqLisfQbVKJNlxWcuHGyPzaToYgXhZ",
        "katQFeDYRVzvEdhIpiOHBxWKgrTujJ",
        "hVlYTbzQHxpqwduZcoKmjWgUtvRe",
        "ymwrANvlSuxhHXokizeDTB",
        "hmuWljKrdYFkiHRxaMDoOTQbsLztXNp",
        "lgEdQDCOsTHyeBKcLMwqJuxftoIPSz",
        "dAlBVgNurviRoUMXSHEGfIYswJ",
        "QotVxjsiGOqbeZWlBHhKMpDECSuvFgfYUnkP",
        "zYbevVFDyXBwRZJUPNnWlkEiHThSqoOQjfam",
        "dtwZjxEzXYDOqeBrKMgQUWJ",
        "gPATIrVflyiMnoBUpmkOXGcYZxKtaFzsw",
        "NetohzYajsLMUEuJCrblyv",
        "ILfxbZgHOahXqrwQuveKS",
        "OqCwZjVpBYItSuTcivArkfaxeEmlNdsyQDXzWUM",
        "omZbDRpJTyjGrsQFxEaMgkAIlXwnvC",
        "NUXIKwtSBJQjbxgszVCmZdEif",
        "lSMfHevobVLucwCiEURJAqWnzahK",
        "TRkCxSMcLuqrIsyVdDGHZbAQKaYwpovjWfOE",
        "KUtXiRLphrDeQAFWCxzMgSGwBHdsIPjylonkEmqT",
        "zTsiJguVSqbtvGEoKXyPcDfNemhM",
        "tqlVJWAgcETwrpbSmyDuoiYxZkNU",
        "YlUbJyzpQoCGNKmhEugitA",
        "NYUwxrjVMIZsEounSQGiJh",
        "JsPRmGUZYctafubrnQjkOTHL",
        "iWkGsHJgCPwEoZchOfdAbmxnzKpqLRYyuUaF",
        "noCHNIwOJGPpgaKYQXtceyFALZrflzbSWjd",
        "UvyzXfnshqKWcRdlmwoJxaDkp",
        "TGZgWAxSEoDqRlJfisuNMPhazFUnIcLKCQwHVp",
        "zKQZloqHXJSREbPuFfdAWrcwI",
        "ScrPmTbWpzOMydNGaAXLRiVQHEwex",
        "GokqtAspMnzjTvLKHVEBuJIibdZDxweWOcQPSfN",
        "MQKNBoYptiFAOrumqsvDUkwIzCbyhZfXSaexdEG",
        "xHYNeZUluSfpLXQAmjzqsTrwIRy",
        "ZRqjaktEecKVPplSAFLburYnTH",
    ]
    
    paginator = Paginator(object_list, 10)
    print "----------------------"
    print paginator._get_main_page_numbers(1)
    print "----------------------"
    print paginator._get_main_page_numbers(2)
    print "----------------------"
    print paginator._get_main_page_numbers(3)
    print "----------------------"
    print paginator._get_main_page_numbers(4)
    print "----------------------"
    print paginator._get_main_page_numbers(5)
    print "----------------------"
    print paginator._get_main_page_numbers(6)
    print "----------------------"
    print paginator._get_main_page_numbers(7)
    print "----------------------"
    print paginator._get_main_page_numbers(8)
    print "----------------------"
    print paginator._get_main_page_numbers(9)

