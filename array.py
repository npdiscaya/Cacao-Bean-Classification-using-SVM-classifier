import cv2
import glob

image_list = []
for filename in glob.glob('dataset/*.JPG'):
    img=cv2.imread(filename)
    image_list.append(img)

cropped1 = img[531:801, 2:383]
cv2.imwrite("dataset/test/Cacao/(01,01).jpg", cropped1)
cropped2 = img[783:1053, 2:383]
cv2.imwrite("dataset/test/Cacao/(01,02).jpg", cropped2)
cropped3 = img[1035:1305, 12:393]
cv2.imwrite("dataset/test/Cacao/(01,03).jpg", cropped3)
cropped4 = img[1289:1559, 15:396]
cv2.imwrite("dataset/test/Cacao/(01,04).jpg", cropped4)
cropped5 = img[1541:1811, 22:403]
cv2.imwrite("dataset/test/Cacao/(01,05).jpg", cropped5)
cropped6 = img[1798:2068, 20:401]
cv2.imwrite("dataset/test/Cacao/(01,06).jpg", cropped6)
cropped7 = img[2058:2328, 29:410]
cv2.imwrite("dataset/test/Cacao/(01,07).jpg", cropped7)
cropped8 = img[523:793, 384:765]
cv2.imwrite("dataset/test/Cacao/(02,01).jpg", cropped8)
cropped9 = img[789:1059, 384:765]
cv2.imwrite("dataset/test/Cacao/(02,02).jpg", cropped9)
cropped10 = img[1038:1308, 381:762]
cv2.imwrite("dataset/test/Cacao/(02,03).jpg", cropped10)
cropped11 = img[1289:1559, 381:762]
cv2.imwrite("dataset/test/Cacao/(02,04).jpg", cropped11)
cropped12 = img[1537:1807, 391:772]
cv2.imwrite("dataset/test/Cacao/(02,05).jpg", cropped12)
cropped13 = img[1803:2073, 397:778]
cv2.imwrite("dataset/test/Cacao/(02,06).jpg", cropped13)
cropped14 = img[2064:2334, 405:786]
cv2.imwrite("dataset/test/Cacao/(02,07).jpg", cropped14)
cropped15 = img[530:800, 754:1135]
cv2.imwrite("dataset/test/Cacao/(03,01).jpg", cropped15)
cropped16 = img[779:1049, 756:1137]
cv2.imwrite("dataset/test/Cacao/(03,02).jpg", cropped16)
cropped17 = img[1032:1302, 761:1142]
cv2.imwrite("dataset/test/Cacao/(03,03).jpg", cropped17)
cropped18 = img[1290:1552, 766:1144]
cv2.imwrite("dataset/test/Cacao/(03,04).jpg", cropped18)
cropped19 = img[1546:1808, 768:1146]
cv2.imwrite("dataset/test/Cacao/(03,05).jpg", cropped19)
cropped20 = img[1808:2070, 779:1157]
cv2.imwrite("dataset/test/Cacao/(03,06).jpg", cropped20)
cropped21 = img[2070:2332, 782:1160]
cv2.imwrite("dataset/test/Cacao/(03,07).jpg", cropped21)
cropped22 = img[519:781, 1138:1516]
cv2.imwrite("dataset/test/Cacao/(04,01).jpg", cropped22)
cropped23 = img[776:1038, 1143:1521]
cv2.imwrite("dataset/test/Cacao/(04,02).jpg", cropped23)
cropped24 = img[1042:1304, 1150:1528]
cv2.imwrite("dataset/test/Cacao/(04,03).jpg", cropped24)
cropped25 = img[1303:1565, 1160:1538]
cv2.imwrite("dataset/test/Cacao/(04,04).jpg", cropped25)
cropped26 = img[1546:1808, 1166:1544]
cv2.imwrite("dataset/test/Cacao/(04,05).jpg", cropped26)
cropped27 = img[1817:2079, 1166:1534]
cv2.imwrite("dataset/test/Cacao/(04,06).jpg", cropped27)
cropped28 = img[2075:2337, 1169:1537]
cv2.imwrite("dataset/test/Cacao/(04,07).jpg", cropped28)
cropped29 = img[522:784, 1538:1933]
cv2.imwrite("dataset/test/Cacao/(05,01).jpg", cropped29)
cropped30 = img[785:1047, 1542:1937]
cv2.imwrite("dataset/test/Cacao/(05,02).jpg", cropped30)
cropped31 = img[1047:1309, 1532:1927]
cv2.imwrite("dataset/test/Cacao/(05,03).jpg", cropped31)
cropped32 = img[1295:1557, 1539:1934]
cv2.imwrite("dataset/test/Cacao/(05,04).jpg", cropped32)
cropped33 = img[1552:1814, 1539:1934]
cv2.imwrite("dataset/test/Cacao/(05,05).jpg", cropped33)
cropped34 = img[1824:2086, 1529:1924]
cv2.imwrite("dataset/test/Cacao/(05,06).jpg", cropped34)
cropped35 = img[2073:2335, 1549:1944]
cv2.imwrite("dataset/test/Cacao/(05,07).jpg", cropped35)
cropped36 = img[528:790, 1933:2328]
cv2.imwrite("dataset/test/Cacao/(06,01).jpg", cropped36)
cropped37 = img[788:1050, 1928:2323]
cv2.imwrite("dataset/test/Cacao/(06,02).jpg", cropped37)
cropped38 = img[1045:1307, 1927:2322]
cv2.imwrite("dataset/test/Cacao/(06,03).jpg", cropped38)
cropped39 = img[1309:1571, 1930:2325]
cv2.imwrite("dataset/test/Cacao/(06,04).jpg", cropped39)
cropped40 = img[1542:1804, 1928:2323]
cv2.imwrite("dataset/test/Cacao/(06,05).jpg", cropped40)
cropped41 = img[1826:2088, 1934:2329]
cv2.imwrite("dataset/test/Cacao/(06,06).jpg", cropped41)
cropped42 = img[2089:2351, 1940:2335]
cv2.imwrite("dataset/test/Cacao/(06,07).jpg", cropped42)
cropped43 = img[521:783,  2330:2725]
cv2.imwrite("dataset/test/Cacao/(07,01).jpg", cropped43)
cropped44 = img[789:1051, 2335:2730]
cv2.imwrite("dataset/test/Cacao/(07,02).jpg", cropped44)
cropped45 = img[1042:1304, 2328:2723]
cv2.imwrite("dataset/test/Cacao/(07,03).jpg", cropped45)
cropped46 = img[1303:1565, 2338:2733]
cv2.imwrite("dataset/test/Cacao/(07,04).jpg", cropped46)
cropped47 = img[1560:1822, 2331:2726]
cv2.imwrite("dataset/test/Cacao/(07,05).jpg", cropped47)
cropped48 = img[1827:2089, 2331:2726]
cv2.imwrite("dataset/test/Cacao/(07,06).jpg", cropped48)
cropped49 = img[2084:2346, 2345:2740]
cv2.imwrite("dataset/test/Cacao/(07,07).jpg", cropped49)
cropped50 = img[521:783, 2738:3133]
cv2.imwrite("dataset/test/Cacao/(08,01).jpg", cropped50)
cropped51 = img[782:1044, 2729:3124]
cv2.imwrite("dataset/test/Cacao/(08,02).jpg", cropped51)
cropped52 = img[1046:1308, 2733:3128]
cv2.imwrite("dataset/test/Cacao/(08,03).jpg", cropped52)
cropped53 = img[1307:1569, 2730:3125]
cv2.imwrite("dataset/test/Cacao/(08,04).jpg", cropped53)
cropped54 = img[1566:1828, 2738:3133]
cv2.imwrite("dataset/test/Cacao/(08,05).jpg", cropped54)
cropped55 = img[1831:2093, 2738:3133]
cv2.imwrite("dataset/test/Cacao/(08,06).jpg", cropped55)
cropped56 = img[2095:2357, 2740:3135]
cv2.imwrite("dataset/test/Cacao/(08,07).jpg", cropped56)
cropped57 = img[521:783, 3136:3531]
cv2.imwrite("dataset/test/Cacao/(09,01).jpg", cropped57)
cropped58 = img[783:1045, 3141:3536]
cv2.imwrite("dataset/test/Cacao/(09,02).jpg", cropped58)
cropped59 = img[1050:1312, 3139:3534]
cv2.imwrite("dataset/test/Cacao/(09,03).jpg", cropped59)
cropped60 = img[1310:1572, 3139:3534]
cv2.imwrite("dataset/test/Cacao/(09,04).jpg", cropped60)
cropped61 = img[1567:1829, 3139:3534]
cv2.imwrite("dataset/test/Cacao/(09,05).jpg", cropped61)
cropped62 = img[1829:2091, 3139:3534]
cv2.imwrite("dataset/test/Cacao/(09,06).jpg", cropped62)
cropped63 = img[2097:2359, 3121:3516]
cv2.imwrite("dataset/test/Cacao/(09,07).jpg", cropped63)
cropped64 = img[522:784, 3540:3935]
cv2.imwrite("dataset/test/Cacao/(10,01).jpg", cropped64)
cropped65 = img[783:1045, 3540:3935]
cv2.imwrite("dataset/test/Cacao/(10,02).jpg", cropped65)
cropped66 = img[1045:1307, 3544:3939]
cv2.imwrite("dataset/test/Cacao/(10,03).jpg", cropped66)
cropped67 = img[1311:1573, 3540:3935]
cv2.imwrite("dataset/test/Cacao/(10,04).jpg", cropped67)
cropped68 = img[1569:1831, 3542:3937]
cv2.imwrite("dataset/test/Cacao/(10,05).jpg", cropped68)
cropped69 = img[1830:2092, 3540:3935]
cv2.imwrite("dataset/test/Cacao/(10,06).jpg", cropped69)
cropped70 = img[2095:2357, 3545:3940]
cv2.imwrite("dataset/test/Cacao/(10,07).jpg", cropped70)
cropped71 = img[522:784, 3949:4344]
cv2.imwrite("dataset/test/Cacao/(11,01).jpg", cropped71)
cropped72 = img[783:1045, 3950:4345]
cv2.imwrite("dataset/test/Cacao/(11,02).jpg", cropped72)
cropped73 = img[1045:1307, 3950:4345]
cv2.imwrite("dataset/test/Cacao/(11,03).jpg", cropped73)
cropped74 = img[1312:1574, 3946:4341]
cv2.imwrite("dataset/test/Cacao/(11,04).jpg", cropped74)
cropped75 = img[1570:1832, 3946:4341]
cv2.imwrite("dataset/test/Cacao/(11,05).jpg", cropped75)
cropped76 = img[1833:2095, 3946:4341]
cv2.imwrite("dataset/test/Cacao/(11,06).jpg", cropped76)
cropped77 = img[2093:2355, 3946:4341]
cv2.imwrite("dataset/test/Cacao/(11,07).jpg", cropped77)
cropped78 = img[532:794, 4348:4743]
cv2.imwrite("dataset/test/Cacao/(12,01).jpg", cropped78)
cropped79 = img[797:1059, 4348:4743]
cv2.imwrite("dataset/test/Cacao/(12,02).jpg", cropped79)
cropped80 = img[1063:1325, 4341:4736]
cv2.imwrite("dataset/test/Cacao/(12,03).jpg", cropped80)
cropped81 = img[1320:1582, 4341:4736]
cv2.imwrite("dataset/test/Cacao/(12,04).jpg", cropped81)
cropped82 = img[1579:1841, 4338:4733]
cv2.imwrite("dataset/test/Cacao/(12,05).jpg", cropped82)
cropped83 = img[1843:2105, 4342:4737]
cv2.imwrite("dataset/test/Cacao/(12,06).jpg", cropped83)
cropped84 = img[2102:2364, 4336:4731]
cv2.imwrite("dataset/test/Cacao/(12,07).jpg", cropped84)
cropped85 = img[535:797, 4740:5135]
cv2.imwrite("dataset/test/Cacao/(13,01).jpg", cropped85)
cropped86 = img[806:1068, 4752:5147]
cv2.imwrite("dataset/test/Cacao/(13,02).jpg", cropped86)
cropped87 = img[1065:1327, 4752:5147]
cv2.imwrite("dataset/test/Cacao/(13,03).jpg", cropped87)
cropped88 = img[1311:1573, 4742:5137]
cv2.imwrite("dataset/test/Cacao/(13,04).jpg", cropped88)
cropped89 = img[1580:1842, 4734:5129]
cv2.imwrite("dataset/test/Cacao/(13,05).jpg", cropped89)
cropped90 = img[1854:2116, 4727:5122]
cv2.imwrite("dataset/test/Cacao/(13,06).jpg", cropped90)
cropped91 = img[2100:2362, 4750:5145]
cv2.imwrite("dataset/test/Cacao/(13,07).jpg", cropped91)
cropped92 = img[550:812, 5147:5542]
cv2.imwrite("dataset/test/Cacao/(14,01).jpg", cropped92)
cropped93 = img[810:1072, 5149:5544]
cv2.imwrite("dataset/test/Cacao/(14,02).jpg", cropped93)
cropped94 = img[1060:1322, 5137:5532]
cv2.imwrite("dataset/test/Cacao/(14,03).jpg", cropped94)
cropped95 = img[1319:1581, 5135:5530]
cv2.imwrite("dataset/test/Cacao/(14,04).jpg", cropped95)
cropped96 = img[1585:1837, 5135:5530]
cv2.imwrite("dataset/test/Cacao/(14,05).jpg", cropped96)
cropped97 = img[1844:2106, 5127:5522]
cv2.imwrite("dataset/test/Cacao/(14,06).jpg", cropped97)
cropped98 = img[2101:2363, 5123:5518]
cv2.imwrite("dataset/test/Cacao/(14,07).jpg", cropped98)
cropped99 = img[544:806, 5526:5921]
cv2.imwrite("dataset/test/Cacao/(15,01).jpg", cropped99)
cropped100 = img[825:1087, 5533:5928]
cv2.imwrite("dataset/test/Cacao/(15,02).jpg", cropped100)
cropped101 = img[1066:1328, 5523:5918]
cv2.imwrite("dataset/test/Cacao/(15,03).jpg", cropped101)
cropped102 = img[1316:1578, 5523:5918]
cv2.imwrite("dataset/test/Cacao/(15,04).jpg", cropped102)
cropped103 = img[1567:1829, 5540:5935]
cv2.imwrite("dataset/test/Cacao/(15,05).jpg", cropped103)
cropped104 = img[1840:2102, 5520:5915]
cv2.imwrite("dataset/test/Cacao/(15,06).jpg", cropped104)
cropped105 = img[2099:2361, 5516:5921]
cv2.imwrite("dataset/test/Cacao/(15,07).jpg", cropped105)
