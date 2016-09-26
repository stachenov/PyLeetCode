import pytest
from problems.trapping_rain_2 import Solution


@pytest.mark.parametrize("heightMap, expected", [
    ([[2, 2, 2],
      [2, 1, 2],
      [2, 2, 2]
      ], 1),
    ([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ], 4),
    ([[1103,1106,1107,1105,1103,1105,1106,1102,1109,1101,1102,1107,1100,1109,1103,1106,1100,1106,1102,1106,1101,1108,1107,1109,1102,1100,1102,1103,1107,1105,1109,1102,1102,1108,1109,1107,1103,1106,1101,1102,1109,1103,1101,1109,1104,1107,1108,1104,1105,1100],[1103,536,101,990,966,883,872,180,1006,291,315,935,94,337,346,515,856,739,323,867,134,905,592,555,824,377,444,374,53,760,97,818,286,188,798,594,413,661,764,409,942,70,686,378,749,22,236,596,104,549],[1105,580,444,388,477,611,107,912,327,502,662,766,311,290,296,451,875,699,454,629,450,739,41,127,107,781,491,685,719,937,577,866,507,363,596,975,316,693,229,634,538,881,742,839,513,29,280,378,718,725],[1100,159,806,733,628,255,856,461,931,565,389,498,774,238,851,360,203,510,44,774,134,924,997,866,753,501,237,375,869,946,442,561,447,238,285,417,484,131,868,405,39,247,245,803,828,438,153,21,938,539],[1106,414,453,773,623,548,616,850,914,828,138,698,379,927,927,1006,334,753,480,193,500,509,782,735,654,600,515,149,964,796,679,92,552,474,207,517,365,814,358,621,632,838,309,353,756,578,350,432,321,820],[1105,811,671,740,888,315,330,746,454,636,532,475,718,426,292,268,934,647,72,634,610,46,462,909,389,560,478,81,983,141,891,940,943,904,670,173,209,991,909,1006,969,783,823,678,200,105,936,476,94,350],[1100,694,386,552,946,117,455,766,189,428,897,422,358,182,669,19,346,220,352,597,216,311,723,382,331,265,829,609,731,914,949,821,950,677,715,238,137,160,994,668,930,234,432,279,406,91,640,94,302,982],[1102,860,635,395,232,309,650,52,908,723,308,200,534,600,219,591,829,346,742,165,1004,14,389,779,283,786,860,265,870,152,589,894,1003,215,631,577,514,623,971,764,336,269,954,212,212,516,794,31,852,878],[1108,199,882,918,968,508,46,818,763,258,313,343,143,658,900,764,577,756,378,539,510,56,798,807,259,1000,313,43,373,507,263,902,696,135,162,1006,985,198,167,739,446,470,424,931,470,314,38,37,60,758],[1106,912,804,707,709,53,49,12,438,413,510,691,657,548,169,161,545,144,349,702,225,137,514,639,59,974,295,439,353,345,187,910,248,981,959,299,377,998,302,805,753,154,839,400,692,350,551,579,836,242],[1101,52,370,127,33,771,91,319,200,435,1006,377,687,244,700,636,534,67,624,178,215,368,322,396,110,356,736,1004,926,562,588,539,956,300,657,980,61,90,641,603,867,637,322,896,224,365,522,100,422,489],[1100,979,199,284,365,651,630,443,997,898,348,576,780,294,866,427,616,270,859,247,215,69,227,528,955,793,883,468,883,647,299,493,617,488,767,324,481,739,110,469,628,448,35,398,84,243,167,691,503,368],[1100,709,427,849,579,373,632,804,183,857,441,472,692,400,302,801,67,125,531,167,584,501,957,961,241,31,547,750,64,40,108,335,91,526,526,12,241,149,806,414,348,590,228,31,980,872,822,389,987,695],[1106,914,186,493,217,769,867,754,509,921,137,960,246,570,828,115,573,59,254,721,815,944,301,385,965,624,599,778,1003,928,815,892,832,992,727,40,103,584,136,603,496,263,553,84,824,723,189,387,772,785],[1108,929,720,742,304,27,356,245,147,701,163,953,583,338,935,301,720,28,227,846,973,65,100,868,140,914,581,671,643,695,799,83,614,861,815,260,878,513,495,16,205,649,959,130,977,236,773,687,606,991],[1105,570,46,965,780,528,221,352,542,206,389,331,280,994,182,437,244,50,293,82,408,840,73,357,960,40,583,724,69,532,57,934,92,445,242,214,964,453,908,496,650,288,169,272,272,693,51,858,733,334],[1102,132,164,345,831,467,375,757,181,786,279,228,711,713,663,943,917,969,738,816,807,730,94,318,344,708,1001,386,908,725,62,181,199,569,516,20,26,234,119,549,10,388,119,63,91,124,348,999,436,77],[1107,233,797,241,542,132,291,885,860,189,600,264,360,141,823,867,504,191,91,613,730,443,992,191,497,425,306,835,414,732,902,561,307,42,144,191,516,425,67,718,605,1009,972,307,493,786,164,987,319,597],[1102,392,31,276,573,870,692,221,695,96,295,940,1000,593,324,486,126,830,902,535,538,849,535,500,146,370,628,653,347,938,592,631,320,965,898,235,825,580,447,863,18,732,793,360,667,107,837,136,279,81],[1101,159,920,538,649,408,898,620,403,587,900,986,209,562,941,97,787,109,667,576,962,27,651,745,378,308,194,205,786,815,276,438,964,538,318,603,288,207,565,682,784,455,10,335,1007,293,422,137,392,431],[1103,344,449,344,431,169,995,967,364,771,772,982,551,726,862,860,672,492,409,227,164,183,25,516,861,374,800,273,501,182,47,547,869,838,881,290,997,866,600,351,980,362,675,521,79,527,371,93,361,122],[1100,516,648,677,374,499,42,164,114,885,689,151,422,548,979,646,180,966,854,770,659,824,475,324,336,896,193,49,979,545,162,631,403,800,299,119,641,683,274,745,558,305,887,323,843,208,959,365,165,803],[1108,166,970,943,833,296,181,368,687,150,255,191,771,1000,333,60,110,964,85,374,52,634,669,929,299,854,479,248,561,986,393,29,143,353,314,966,991,485,676,21,977,922,202,739,912,878,141,12,184,217],[1108,226,193,387,497,482,583,967,72,135,943,807,506,428,151,163,736,484,990,403,495,958,315,40,39,569,908,170,572,434,729,290,651,912,20,490,736,593,799,150,718,733,948,567,503,441,720,230,915,700],[1103,401,648,280,431,677,839,681,190,753,105,909,34,98,164,396,579,242,979,720,383,40,443,673,597,289,104,659,509,361,349,474,752,340,96,525,359,925,196,891,21,644,143,397,732,297,783,653,529,752],[1104,254,134,149,269,73,428,363,722,279,715,414,743,809,744,829,325,445,97,863,679,460,497,812,847,572,99,620,215,970,714,921,567,839,413,826,902,831,532,615,453,589,371,538,388,457,710,55,892,797],[1109,561,599,396,363,436,958,804,46,516,117,102,427,674,931,830,490,176,1004,364,133,447,943,494,327,322,941,27,719,175,166,618,79,755,1005,432,181,305,579,569,811,686,662,581,350,935,753,182,101,99],[1107,576,888,822,60,206,134,343,223,196,509,380,804,578,125,151,352,649,447,273,208,600,949,212,523,641,138,267,814,581,356,693,148,235,505,550,431,982,236,644,168,735,366,962,655,482,456,349,121,893],[1103,671,835,552,226,349,184,354,606,340,277,304,23,767,529,870,660,302,842,886,289,1000,963,645,305,608,117,751,947,580,986,550,594,811,93,810,502,619,506,450,949,773,745,314,883,616,174,533,261,359],[1101,540,349,714,175,996,312,635,89,601,557,417,494,141,571,929,941,63,538,437,504,829,553,591,133,778,197,649,653,448,998,404,330,690,108,496,28,762,473,108,705,20,515,189,152,76,108,435,482,988],[1103,976,807,758,557,282,526,96,922,169,887,910,563,207,942,13,45,961,117,508,59,164,871,916,344,13,335,794,438,807,773,643,125,570,391,24,195,907,110,107,418,339,359,323,889,644,326,924,595,785],[1105,996,940,636,902,626,639,579,762,419,376,525,405,843,438,786,857,623,36,310,72,796,639,773,110,518,407,426,785,992,554,550,330,836,528,575,804,509,144,556,918,863,72,313,696,852,442,544,817,820],[1104,879,606,825,994,706,334,392,475,461,726,371,353,47,197,871,612,991,370,98,889,630,951,303,934,638,145,718,172,952,880,1006,173,476,821,510,525,497,244,342,300,960,703,643,349,890,504,303,223,864],[1102,454,485,333,748,761,961,883,821,475,178,691,823,693,509,987,545,24,474,779,356,117,82,401,750,421,633,597,67,846,803,449,291,630,124,381,381,428,606,544,893,774,577,707,810,77,684,345,443,500],[1107,142,959,539,533,700,302,157,639,359,345,432,150,978,53,265,349,776,35,946,663,270,62,230,967,214,297,993,550,731,836,1007,215,137,888,738,179,180,237,808,530,573,231,670,893,626,277,233,392,302],[1101,45,563,573,618,872,778,905,208,670,978,386,19,183,513,897,264,683,67,491,833,939,406,54,952,290,22,219,865,757,864,376,144,769,291,752,983,411,648,181,423,968,909,432,494,765,671,100,790,81],[1103,613,10,330,10,952,962,22,514,817,769,368,535,904,127,168,646,100,570,636,624,983,947,875,758,431,630,419,873,410,842,796,14,843,468,366,137,420,378,641,579,138,351,456,384,468,615,20,911,175],[1109,877,500,936,742,248,709,715,10,572,467,842,358,471,27,817,179,507,579,548,138,149,28,480,595,402,290,552,764,543,717,753,410,560,31,495,798,730,200,150,644,657,335,993,471,704,152,640,201,73],[1100,330,564,548,152,502,940,432,44,695,318,104,790,718,654,812,555,794,532,97,935,167,745,612,502,558,306,996,540,850,59,61,522,966,599,664,458,882,438,492,567,98,586,347,807,230,149,704,15,24],[1102,292,533,879,246,25,427,894,363,309,734,764,360,246,720,302,252,168,174,33,651,731,121,579,420,270,800,912,965,157,926,99,791,449,968,27,816,385,911,521,684,988,275,387,576,986,679,171,144,843],[1106,137,916,1009,707,326,270,849,580,577,996,496,18,777,287,976,146,445,703,47,956,729,377,222,106,944,550,127,105,684,960,641,812,218,640,861,535,252,700,457,171,686,944,179,805,573,145,941,361,190],[1100,307,910,698,871,1006,984,411,124,79,438,426,62,592,635,692,443,512,287,133,959,800,161,245,970,956,809,457,239,512,638,559,809,538,599,23,886,573,776,1000,994,204,769,46,786,394,81,219,248,710],[1104,549,500,845,785,460,791,936,260,372,438,888,274,589,768,863,954,644,779,721,987,115,267,746,152,44,482,575,605,720,275,642,259,117,477,386,568,611,312,170,973,92,48,237,24,806,443,968,440,564],[1109,417,669,937,505,811,323,977,728,270,39,345,902,641,453,722,17,363,323,672,523,638,106,561,866,120,709,651,79,491,205,100,899,864,379,746,18,692,714,736,305,743,424,197,374,867,261,734,220,574],[1108,733,203,844,636,411,955,335,404,376,816,599,466,57,805,836,794,813,870,850,892,165,583,658,705,300,515,956,376,77,873,114,800,418,300,778,171,245,103,565,611,261,154,420,661,301,598,445,457,458],[1105,691,966,210,339,661,852,844,959,570,911,174,674,53,582,965,821,743,552,266,650,506,869,146,268,520,438,856,307,885,304,934,566,260,135,895,263,329,81,565,890,334,729,906,377,654,213,540,739,756],[1106,380,604,655,868,862,518,296,708,815,523,354,740,431,957,217,668,210,888,739,117,768,63,189,17,782,185,220,312,914,318,450,636,912,96,495,116,956,133,814,761,647,511,843,420,458,402,79,10,281],[1100,118,391,566,297,398,338,472,961,993,728,269,433,355,524,871,192,982,817,667,139,921,304,640,754,67,88,147,136,88,770,638,196,151,194,835,892,875,649,843,858,368,454,633,65,320,495,599,293,654],[1106,422,565,903,52,310,960,130,799,438,560,559,66,747,52,251,924,934,468,564,119,668,274,564,291,329,226,128,270,509,773,516,273,328,409,315,980,711,787,121,139,338,22,196,427,65,789,693,989,599],[1107,99,257,863,1005,890,534,221,1009,794,721,124,653,336,794,52,642,117,106,771,228,235,451,241,773,220,296,904,904,627,845,493,68,92,347,63,325,223,627,324,1008,690,790,651,16,574,45,648,33,141]], 353397),
])
def test_trapRainWater(heightMap, expected):
    assert Solution().trapRainWater(heightMap) == expected
