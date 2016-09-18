import pytest
from problems.frog_jump import Solution


@pytest.mark.parametrize("stones,expected", [
    ([0, 1, 3, 5, 6, 8, 12, 17], True),
    ([0, 1, 2, 3, 4, 8, 9, 11], False),
    ([0,1,4802,9103,16575,22205,27053,28867,29267,30417,31405,34707,43336,53294,55333,55998,64793,68689,75678,82652,90431,95881,103008,109632,116318,116933,119297,126733,127952,132915,139669,140909,146981,151865,161412,164007,167313,168823,172304,173477,179161,183704,185141,195063,201550,204198,209480,215670,223347,226781,231389,235292,241493,246602,253901,262911,270903,272223,281944,281961,289697,298024,305665,311795,314918,320902,321336,322290,332101,339974,348169,351335,359734,367738,375903,378542,388182,396197,401433,410790,414915,415866,423433,432717,437566,442690,451119,461065,466730,472056,473648,481001,484792,494230,497666,499403,504660,512258,517435,523627,528086,536166,540883,545150,546571,546941,551730,560177,562279,566575,567699,573413,573836,582734,585003,593170,595909,597308,605978,612963,615716,621272,623481,633479,635586,636632,640204,644901,646532,651223,654983,656359,658108,664357,667539,674348,679495,680730,688992,693560,694063,701259,709974,717944,724252,727035,727754,737164,744124,752664,753018,753804,755128,759032,760134,767348,775216,779748,783363,791968,793968,796771,801363,803158,813155,821115,821960,826093,829883,835559,844964,850905,855267,863212,865371,868185,873230,882430,886486,893182,901773,910048,917982,926410,927337,937018,946250,950944,953586,955333,959157,968323,971715,975839,978039,981137,989012,992868,998465,1007758,1009991,1019392,1020453,1022286,1022966,1032741,1035483,1041434,1049056,1055151,1061227,1069400,1078141,1087379,1094142,1103011,1106409,1109258,1116265,1120875,1129199,1132299,1142165,1143688,1150724,1155998,1158706,1165480,1173428,1181991,1182796,1182998,1190341,1195549,1204853,1207888,1215316,1221906,1226015,1231983,1240495,1240595,1246880,1250381,1253839,1263274,1269597,1269942,1272290,1277126,1285421,1292280,1298149,1302027,1303856,1306006,1314715,1315733,1318736,1324358,1331449,1341377,1345260,1350688,1359498,1365529,1366913,1369025,1369130,1373711,1376151,1379711,1381640,1391328,1400203,1405356,1408057,1416142,1425100,1429025,1431654,1435895,1438486,1439232,1446276,1454672,1460438,1467815,1474772,1484209,1493886,1503812,1509466,1518045,1520547,1523127,1525534,1528415,1533201,1533988,1543162,1550720,1559134,1567005,1572667,1575703,1582352,1591815,1599915,1609505,1612012,1617538,1623988,1624198,1625414,1630419,1635121,1638608,1647101,1654194,1656119,1658305,1663152,1668475,1671199,1673428,1681466,1683648,1686035,1694826,1695700,1702239,1706170,1712727,1718109,1719227,1724830,1724839,1731467,1735854,1737912,1738037,1742368,1744123,1749963,1756155,1763558,1763915,1769188,1777210,1779964,1788397,1796263,1805194,1814184,1814921,1815947,1818677,1828597,1830373,1837657,1847019,1855344,1860941,1863734,1864533,1872127,1881060,1887213,1895335,1903568,1908411,1917927,1927459,1937173,1938316,1941066,1944617,1952316,1962163,1969990,1977991,1984302,1990786,1991654,2000906,2009825,2014816,2019538,2025009,2032629,2037412,2037949,2045057,2052919,2061207,2062970,2071619,2077885,2087818,2096145,2097187,2098866,2102856,2103496,2107017,2107320,2108528,2108843,2114108,2121181,2129615,2130503,2139371,2146795,2156596,2157914,2160418,2166700,2171657,2178545,2185566,2185600,2191593,2195499,2204904,2207714,2209075,2215792,2224919,2227642,2236875,2240907,2246831,2252850,2258464,2263105,2271426,2275238,2282886,2284021,2289254,2297900,2298316,2302424,2312099,2312595,2316125,2324793,2334290,2340169,2347810,2348114,2353076,2358992,2368312,2372428,2372782,2375203,2385088,2388880,2391227,2395822,2403946,2412780,2415637,2422675,2428972,2430024,2435845,2445336,2450767,2459991,2460081,2469714,2474044,2476729,2478842,2488218,2495846,2499254,2508837,2509173,2511503,2514422,2517611,2523739,2529492,2531190,2539865,2545406,2546484,2548900,2549493,2558849,2568792,2572675,2580663,2589948,2593029,2598623,2604108,2611815,2613976,2620029,2626127,2632207,2636399,2645487,2647904,2648447,2652197,2659074,2659573,2666975,2669422,2674279,2677538,2682169,2685602,2685730,2694845,2700210,2708955,2710052,2710238,2715640,2719782,2727633,2735158,2745128,2746348,2752528,2757317,2765011,2773041,2781273,2781455,2790816,2794608,2803113,2804947,2808677,2816979,2826092,2832070,2839585,2841082,2845683,2851716,2858824,2861955,2870062,2879917,2881807,2887952,2897780,2905577,2914324,2922210,2930291,2939438,2948755,2951069,2957913,2962275,2972253,2975364,2978032,2985508,2989192,2995785,2997857,2999284,3007356,3015575,3022423,3024608,3029623,3032486,3035619,3036741,3039669,3040333,3048880,3053923,3059160,3062778,3065940,3066569,3071618,3076161,3078703,3087682,3093135,3102572,3110231,3117585,3123780,3131290,3131660,3139448,3147181,3153097,3159635,3160786,3163192,3170455,3172156,3176047,3179282,3181548,3190002,3198110,3201181,3203734,3212408,3215228,3222132,3224284,3233047,3233712,3234545,3242908,3251242,3259546,3264268,3270276,3276844,3277964,3283424,3287438,3295499,3302101,3310146,3313635,3319933,3328349,3329505,3333245,3335504,3341466,3343105,3351704,3352170,3356292,3357207,3361677,3364444,3372406,3381478,3381579,3383212,3383829,3392764,3396988,3405261,3414652,3420813,3427897,3436284,3439024,3446546,3454872,3459180,3465367,3473864,3476916,3477474,3486861,3495835,3499814,3507979,3509821,3516004,3516702,3525632,3534535,3543807,3551844,3558365,3566524,3571570,3574770,3578743,3579730,3584018,3593487,3594187,3597336,3601529,3609651,3615181,3621820,3631655,3634790,3644568,3653246,3658067,3659049,3666580,3676150,3682028,3686679,3690949,3693928,3701277,3701475,3704277,3710832,3716698,3719986,3728277,3736305,3739484,3747938,3748734,3757573,3760050,3765011,3771003,3775882,3777288,3777783,3785928,3786478,3787332,3793172,3796443,3805842,3813903,3822928,3827755,3831261,3835535,3841776,3849005,3858189,3859666,3866984,3872432,3879859,3886246,3892508,3899063,3907914,3916168,3917771,3921369,3930025,3938790,3948607,3953515,3956870,3961625,3962233,3966717,3967834,3975223,3979802,3985706,3992329,3994858,3997325,3999512,4003714,4004644,4005120,4006600,4013009,4016526,4018170,4021037,4025110,4034700,4042903,4049040,4051134,4054414,4055422,4063394,4068427,4068665,4069219,4069857,4070418,4071955,4076529,4082807,4085488,4085969,4091596,4094010,4094425,4100302,4102717,4111013,4119665,4126167,4128612,4134555,4138163,4147300,4151708,4157379,4163125,4165166,4165831,4167793,4173195,4182811,4190236,4194169,4196363,4197542,4206889,4209705,4218824,4225409,4229387,4238633,4247786,4253066,4253375,4258831,4265851,4272922,4279712,4286642,4295689,4304352,4314304,4320854,4324424,4330342,4338565,4346020,4349885,4356630,4357558,4361399,4367249,4370375,4372822,4380624,4390070,4390475,4393532,4400580,4409685,4418966,4421674,4424994,4430831,4438717,4448318,4456652,4457848,4459933,4464970,4473243,4478683,4483082,4486974,4490091,4496417,4497504,4505157,4507690,4514842,4519387,4527995,4537391,4546511,4550019,4551395,4557358,4563242,4572022,4576469,4583363,4587225,4595577,4601357,4602205,4612192,4621610,4631570,4636175,4644247,4649534,4656468,4659197,4667721,4672686,4676773,4680930,4685557,4694571,4699079,4705528,4706405,4712168,4715817,4717351,4719192,4728145,4729997,4739668,4744370,4746546,4753962,4759220,4760485,4760896,4761321,4771219,4777845,4785387,4787381,4791757,4795554,4801833,4804651,4805257,4813421,4818730,4824410,4825485,4829939,4838908,4842625,4851075,4854026,4860312,4863754,4869653,4870150,4872704,4881927,4889675,4897966,4898932,4900251,4905691,4913960,4919044,4922054,4925439,4928109,4934196,4934710,4936750,4942337,4950693,4959068,4968935,4976953,4986841,4992879,4994493,4995134,5000011,5008638,5010555,5016729,5022235,5029805,5029816,5037171,5042826,5051956,5059204,5066349,5069000,5071014,5078961,5086464,5089111,5094790,5097860,5100594,5103562,5113186,5114548,5121427,5124062,5128064,5131217,5132549,5141521,5145911,5149847,5159119,5164868,5171645,5171771,5174628,5176706,5182156,5191936,5199093], False),
])
def test(stones, expected):
    assert Solution().canCross(stones) == expected