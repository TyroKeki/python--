import requests

# session = requests.session()
# #可能的referer："https://passport.17k.com/login/",
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.8151 SLBChan/115 SLBVPV/64-bit",
#     "Referer":"https://www.17k.com/",
#     "Origin":"https://passport.17k.com",
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
# }
# data={
#     'loginName': '18112368065',
#     'password': 'hjx!967205',
# }
# url = "https://passport.17k.com/ck/user/login"
# resp = session.post(url,data=data,headers=headers)
# print(resp.text)

headers = {
    "Cookie":"""GUID=58353cfa-64ae-4da7-8ca3-f8095bf73e26; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1763379450,1763452158; HMACCOUNT=7377622557745785; acw_sc__v2=691c2c2afc753f3707f7a6e5b0fb614171434db4; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F13%252F73%252F68%252F104386873.jpg-88x88%253Fv%253D1763453014000%26id%3D104386873%26nickname%3DHappyFromFish%26e%3D1779007144%26s%3Df1ed69cbb8c6cfe6; tfstk=gaSoLPVr2a875qiSrJx7rPUokHUvN3tBl6np9HdUuIRX98OJw95hKO8eU05RoBfViQ-p2gEh-I-yRadpwBxhd12Y6lEOFTtBT5FTXXjT7e-6U4Jr9Er2LHvPok3a2TtBYSHxYPEGF_L2T1-yY-x2pdieYL5eunRXdplyL0yc3IO2LbJezKu2IpAeU6-UntRXLHRFTUyc3I9eYBlYN2OGN1I4Oo9umZXfXivkrCW45mnXzcL2_tdmYusDEDRNUImEYCRp8CXce7m1H3sFsdC800fGLO_eoMc4sBsc3g7Fhb22jtbAWUb0aDAA2pYwYEDEYtXyMESebllDhZWR8g1oKDJ52GLH1E2EAeKVXF7NZvw133JFOFsL10OPLOs1Whqo1LbVInjzsquwa6oIxJImR2TyhKAOSLFw_JuPOVy0nVZ2zK97m-2mR2TyhKATn-0ZuUJXFof..; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104386873%22%2C%22%24device_id%22%3A%2219a919b1006603-0737c960cbab16-422b5103-1821369-19a919b1007619%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2258353cfa-64ae-4da7-8ca3-f8095bf73e26%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1763455191; ssxmod_itna=1-eqIOPAxxCi0Ki7qit0oPYKDKYbql4BtGR0DIqGQGcD8xiKDHYG5iiVKDU2hDxAKsqBgRcGNtD=DDsqlZxGzDiwPGhDBn5FQbSYvIGxOS3yPCzu2WTHItl=rgPs3cQvEyyqWwVC83cT/xDHxi8DBKxUlx_sDiiFx0rD0eDPxDYDG4DoaYDn=4DjxDdaUEvszoDbxi3a4iaDGeDeagwDY5eDDHWq407IGEKDGvKeLxwgj04jKMGct4XCbij5WoD9O4Dsgq98WoUOX6KwKLn5AfbN40kEq0Ost4EPRdQ7F3Af/hdYAm/sD_ddirQr5dDGt0P/YGwxxP05eGDd7433_T0xgr=gD58nYGDDi1e5lxeBNrUYccUyPXgZhDSq50eYS_SiGgAACB4mBRPiKCei10wsBqZPrC/xyWreCThbbHQxxD; ssxmod_itna2=1-eqIOPAxxCi0Ki7qit0oPYKDKYbql4BtGR0DIqGQGcD8xiKDHYG5iiVKDU2hDxAKsqBgRcGNtDxDfNe12BTUsDF2OtfeODGNF/mRRfh6dltr3xH_Z_0Q8FqCg1DM6UnYc/g6qSb7Ukl/1GWppvkprrG0Ews1r7kL=Fh0gGW8Oy8gO5CUmq8WS9CzeHsg=2402R48/wKS15aljP4FPENSgGCc7KxSpTOBh0FTnPzl8BLe7Cs7RL1dICFw2EO98piMIpaUx5nw2PuOcvkdtGKqmpCXQvBlPlvG2Ldz5Olzu5X_dvqTjcvyTHO7xp3eql4yQ94mq09_Njb2nu7zAkSwe5GyBF0e7C09s9Yn728FYCjwqRrFfqR0yX0FNboS_AO4F/mR4_v5gaHWHNi5ftYS4ACGIdYFQVEdavuC04S5R8wGmAqgYPwoTBmb2xocPxniHYRtFfG0PIBfWlhqivut07BrpbA6enxjAW7LOV05Dxz22402tSxiCR4IGdC01djd7R1PD""",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.8151 SLBChan/115 SLBVPV/64-bit"
}
resp = requests.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919",headers=headers)
print(resp.json())