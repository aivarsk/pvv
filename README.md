# PVV collisions

Just a small script for a [conference talk](https://www.topconf.com/conference//topconf-tallinn-2017/talk/host-card-emulation-how-a-300-mobile-phone-can-do-what-a-0-3-payment-card-does/) that calculates [Pin Verification Values](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.csfb400/csfb4za2598.htm) to find PVV collisions.

Chooses a random key and a random PAN and calculates PVV values for all 10,000 PINs (4 digits). Prints out the largest set of PINs that all have the same PVV value.

```
Using random PIN Verification Key EDBB6083B46A73BFB1546BD53051A294 with Index 1
PAN 4112981604239691 has 6281 unique PVVs; PINs ['1756', '2234', '2276', '4117', '4428', '5904'] => PVV '7618'
PAN 4112983172949359 has 6363 unique PVVs; PINs ['2600', '3384', '3411', '3613', '3708', '9421'] => PVV '8125'
PAN 4112984531812527 has 6296 unique PVVs; PINs ['0181', '0309', '3482', '5256', '7442', '9095', '9452'] => PVV'8769'
PAN 4112988727897351 has 6310 unique PVVs; PINs ['1711', '1841', '3290', '4141', '4379', '7194'] => PVV '7164'
PAN 4112981125372988 has 6299 unique PVVs; PINs ['0236', '1671', '1840', '2128', '2637', '4392', '6643', '8275'] => PVV '4209'
PAN 4112982864601073 has 6303 unique PVVs; PINs ['2149', '3758', '4191', '4392', '5661', '8197', '8512'] => PVV'1159'
PAN 4112985976213908 has 6342 unique PVVs; PINs ['0073', '3197', '4602', '6181', '8461', '8602', '8739'] => PVV'5995'
PAN 4112986721579562 has 6313 unique PVVs; PINs ['0083', '2621', '6683', '6876', '6993', '8132', '9666'] => PVV'9391'
PAN 4112986975879151 has 6314 unique PVVs; PINs ['3087', '6543', '6587', '7094', '7490', '8003', '8375', '8380'] => PVV '3050'
```
