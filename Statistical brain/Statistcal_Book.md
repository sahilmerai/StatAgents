B R I A N B L A I S
S TAT I S T I C A L I N F E R E N C E
F O R E V E R Y O N E

LIFE’S MOST IMPORTANT QUESTIONS ARE, FOR THE MOST PART, NOTH-
ING BUT PROBABILITY PROBLEMS.
PIERRE-SIMON LAPLACE
STATISTICAL THINKING WILL ONE DAY BE AS NECESSARY FOR EFFICIENT
CITIZENSHIP AS THE ABILITY TO READ AND WRITE.
H.G.WELLS
STATISTICS ARE THE HEART OF DEMOCRACY.
SIMEON STRUNSKY

B R I A N B L A I S
S TAT I S T I C A L I N F E R E N C E
F O R E V E R Y O N E
SAVE THE BROCCOLI PUBLISHING

Copyright©2020BrianBlais
published by save the broccoli publishing
typeset with tufte-latex
ThisbookislicensedundertheCreativeCommonsAttribution-ShareAlikelicense,version4.0,http://
creativecommons.org/licenses/by-sa/4.0/,exceptforthosephotographsanddrawingsofwhichIam
nottheauthor,aslistedinthephotocredits. Ifyouagreetothelicense,itgrantsyoucertainprivileges
thatyouwouldnototherwisehave,suchastherighttocopythebook,ordownloadthedigitalversion
freeofchargefromhttp://web.bryant.edu/~bblais. Atyouroption,youmayalsocopythisbook
undertheGNUFreeDocumentationLicenseversion1.2,http://www.gnu.org/licenses/fdl.txt,withno
invariantsections,nofront-covertexts,andnoback-covertexts.
Firstprinting,September2014. LastCompiledApril17,2020.

Dedicated to all of the wonderful people at
Bryant University in the Library, Writing
Center, and the Center for Teaching and
Learning who have been exceedingly supportive
of me through the entire process of writing.



Acknowledgements
Iwouldliketoacknowledgethefollowingpeoplewhohaveadded
tothisbook,inbigwaysandinsmall. Thebookismuchbetterasa
result.
BillieAnderson JimBishop JeniferBond
PaulCampbell StephanieCarter AllenDowney
RobertFairhead RodrigoFernandez-Vizarra ThomasHartl
HaroldHausmann SteveHeller JeremyHussell
LauraKohl DavidLouton PatrickMarchand
AlanOlinksy JohnQuinn MattRenfro
StevenRush HakanSaraoglu PhillisSchumacher
JamesScott-Brown RobertShea ShergunovVasiliy



Contents
29
Proposal
33
1 Introduction to Probability
34
1.1 Models and Data
35
1.2 What is Probability?
Card Game 36
Other Observations 38
39
1.3 Conditional Probability
Probability Notation 39
40
1.4 Rules of Probability
Negation Rule 41
Product Rule 42
Independence 43
Conjunction 43
Sum Rule 45
Marginalization 46
Bayes’ Rule 47
49
1.5 Venn Mnemonic for the Rules of Probability
50
1.6 Lessons from Bayes’ Rule - A First Look
53
2 Applications of Probability
53
2.1 Cancer and Probability
55
2.2 Weather
First Solution - Independence 55
Second Solution - Correlation 55

10
56
2.3 Adding Dice
58
2.4 The Birthday Problem
Two People on April 3 58
Two People 58
Three People 59
Two People...Out of Three 60
Two People...Out of Thirty 62
62
2.5 The Lottery Problem or Rare Things Are Common
64
2.6 Monty Hall Problem
Two Doors with Information 65
Three Doors with Information 65
Three Doors Down To Two 66
66
2.7 Exercises
67
2.8 Some Philosophical Applications
Doctors’ Claims - English Language and Probability 67
Diverging Opinions 68
A problem of independence 69
Another problem with independence 71
Prosecutor’s Fallacy 72
72
2.9 Computer Examples
Coin Flips 72
75
3 Random Sequences and Visualization
75
3.1 Coin Flipping
Counting the Rearrangements 78
Sequences of Heads and Tails 79
82
3.2 Binomial Distribution
82
3.3 Some Philosophical Applications
Streaks 82
Gambler’s Fallacy 83
The Hot Hand - Correlations in Random Sequences 84
Regression Toward the Mean 85

11
87
3.4 Visualization of Data
Histograms 87
Scatter Plots 90
92
3.5 Computer Examples
Histograms 92
Scatter Plot 92
95
4 Introduction to Model Comparison
95
4.1 The High/Low Deck Game
What does our intuition say? 95
Before the data - the prior 97
The “easy” question - the likelihood 97
Applying the Bayes’ recipe 98
Drawing the next card 99
Prior information or not? 100
102
4.2 Multiple Hypotheses
109
5 Applications of Model Comparison
109
5.1 Disease Testing
Consequences 111
112
5.2 M&M’s
Updating with other data 113
114
5.3 Psychic Octopi
Making a Well Posed Problem 114
The First Model Comparison 116
Furthering the Comparison 117
117
5.4 Monty Hall Problem
121
6 Introduction to Parameter Estimation
121
6.1 Bent Coins
124
6.2 Priors versus Data

12
125
6.3 Moving Toward the Continuous
127
6.4 MAP and Areas
129
6.5 Quartiles
131
6.6 Best Estimates
133
6.7 Uncertainty in the Best Estimates
134
6.8 Marginalization
134
6.9 Exercises
135
6.10Computer Examples
Beta Distribution Example 135
139
7 Priors, Likelihoods, and Posteriors
139
7.1 Binomial and Beta Distributions
140
7.2 The Normal Distribution - Properties
The Shape 140
The location parameter, µ 141
The deviation parameter, σ 141
Summarizing the Distribution 142
Moving from a General Normal to the Standard Normal and Back 142
Sum and Differences 144
146
7.3 The Normal Distribution - Estimating From Data
Estimating the mean, µ, knowing the deviation, σ 146
Estimating the mean, µ, not knowing the deviation, σ 148
149
7.4 Normal Approximation
The Beta Distribution 149
The Binomial Distribution 151
The Student’s t Distribution 152
154
7.5 Summary
155
7.6 Computer Examples
Estimating Lengths 155

13
159
8 Common Statistical Significance Tests
159
8.1 z-test
161
8.2 What it means and doesn’t mean
Significance 161
162
8.3 Student-t-test
163
8.4 Computer Examples
165
9 Applications of Parameter Estimation and Inference
165
9.1 Normal Model - Inference about Means
166
9.2 Normal Model Again - Inference about Means and Deviations
170
9.3 Beta Model - Inference About Proportions
173
9.4 Model Construction
180
9.5 Computer Examples
Iris Example 181
Sunrise 183
Cancer Example 184
Pennies 185
Ball Bearing Sizes 190
193
10 Multi-parameter Models
193
10.1Simple Linear Regression
Mean Squared Error 195
An Educational Example 197
199
10.2Multiple regression
202
10.3Polynomial Regression
202
10.4Computer Examples
211
11 Introduction to MCMC
211
11.1One-Dimensional Models
Reading the Output 212

14
213
11.2Multi-Dimensional Models
215
11.3Hierarchical Model Example - Kruschke BEST Test
219
12 Concluding Thoughts
219
12.1Where have we come?
220
12.2Where are we going?
221
Bibliography
223
Appendix A: Computational Analysis
225
Appendix B: Notation and Standards
225
B.1 Useful Greek Letters
225
B.2 Some Math Notation
Variables 225
Sums 226
Products 226
Sample Mean 226
Sample Standard Deviation 227
Estimates 227
Factorials 227
227
B.3 Qualitative labels to probability values
229
Appendix C: Common Distributions and Their Properties
229
C.1 Discrete and Continuous
229
C.2 Uniform
Discrete 229
Continuous 229
232
C.3 Binomial
232
C.4 Beta
233
C.5 Normal (Gaussian)

15
235
Appendix D: Tables
235
D.1 Credible Intervals for Standard Normal Distribution
236
D.2 Credible Intervals for Student’s t Distribution
238
D.3 Cumulative Standard Normal Distribution



List of Figures
1.1 Standard52-carddeck. 13cardsofeachsuit,labeledSpades,Clubs,
Diamonds,Hearts. 36
1.2 Venndiagramofastatement, A,inaUniverseofallpossiblestate-
ments. ItiscustomarytothinkoftheareaoftheUniversetobeequal
to1sothatwecantreattheactualareasasfractionalareasrepresent-
ingtheprobabilityofstatementslike P(A). Inthisimage, A takes
up1/4oftheUniverse,sothat P(A) =1/4. Alsoshownisthenega-
tionrule. P(A)+P(not A) = 1or“inside”of A +“outside”of A
addsuptoeverything. 49
1.3 Venndiagramofthesumandproduct. Therectangle B takesup1/8
oftheUniverse,andtherectangle A takesup1/4oftheUniverse. Their
overlaphereis1/16oftheUniverse,andrepresents P(A and B). Their
totalareaof5/16oftheUniverserepresents P(A or B). 49
1.4 Venndiagramofconditionalprobabilities, P(A B) and P(B A). (Right)
| |
P(A B) isrepresentedbythefractionofthedarkerarea(whichwas
|
originallypartof A)comparednottotheUniversebuttotheareaof
B,andthusrepresents P(A B) = 1/2. Inaway,itisasifthecon-
|
ditionalsymbol,“ ,”definestheUniversewithwhichtomakethecom-
|
parisons. (Left)Likewise,thesamedarkerareathatwasoriginally
partof B represents P(B A) whichmakesup1/4oftheareaof A.
|
Thus P(B A) =1/4. 50
|
1.5 Venndiagramofmutuallyexclusivestatements. Onecanseethat P(A and B) =
0(theoverlapiszero)and P(A or B) = P(A)+P(B) (thetotalarea
isjustthesumofthetwoareas) 50
2.1 Probabilityforrollingvarioussumsoftwodice. Shownarethere-
sultsfortwo6-sideddice(left)andtwo20-sideddice(right). Thedashed
lineisforclarity,butrepresentsthefactthatyoucan’trollafractional
sum,suchas2.5. 57
2.2 Probabilityofhavingatleasttwopeopleinagroupwiththesame
birthdaydependingonthenumberofpeopleinthegroup. The50%
markisexceededoncethegroupsizeexceeds23people. 63

18
3.1 Probabilityofgetting h headsin30flips. Clearlythemostlikelyvalue
is15,butallofthenumbersfrom12upto18havesignificantprob-
ability. 81
3.2 Probabilityofgetting h headsin30flipsgivenapossibleunfaircoin.
Onecoinhas p =0.1,wherethemaximumisfor3heads(or1/10
ofthe30flips),but2headsisnearlyaslikely. Anotherhas p =0.5,
andisthefaircoinconsideredearlierwithamaximumat15heads
(or1/2ofthe30flips). Finally,anothercoinshownas p =0.8where
24heads(or8/10ofthe30flips)ismaximum. 83
4.1 HighDeck-55Cardswithten10’s,nine9’s,etc... downtooneAce.
Acesareequivalenttothevalue1. 96
4.2 LowDeck-55CardswithtenAces,nine2’s,etc... uptoone10. Aces
areequivalenttothevalue1. 96
4.3 Drawinganumberof9’sinarow,possiblyfromaHigh,Low,and
Ninesdeck. 105
5.1 Rarediseaseandtesting. Shownisapopulationof3000where1in
every200peoplehavethedisease(largecircles). Atestwhichis99%
effectiveisappliedtoeveryoneinthepopulation,andthepositive
testresults(i.e. thetestsaysthatyouhavethedisease)areshownask
smallblackdots. Noticethatalthoughnearlyallofthosethathave
thediseasetestpositive(asmallblackdotinsidealargecircle),there
aremanyfalsepositives(blackdotinanemptysquare)-healthypeo-
plethattestpositiveforthedisease. Eventhoughthetestisquitegood,
therearemanymorehealthypeopleand1outof100ofthemwill
erroneouslytestpositive. 111
5.2 ThefullresultsofthepredictionsofPaultheOctopus,reproduced
fromen.wikipedia.org/wiki/Psychic_octopus. 115
6.1 BentCoins 121
6.2 Probabilityfordifferentbent-coinmodels,giventhedata=9tails,3
heads. 123
6.3 Probabilityfordifferentbent-coinmodels,givennodata(left),the
firsttails(middle),andthesecondtails(right). Thecurvefornodata
isthesameasthepriorprobability,andinthiscaseallmodelsare
equallylikely. Whenthefirsttailsisobserved,themodelwhichstates
thatheadsarecertain(coin10)goestozeroprobability. Asmoretails
areobserved,theprobabilityforthelowermodelsisincreased. 125
6.4 Probabilityfordifferentbent-coinmodels,giventhreetails(left),the
firstheads(middle),andanothertails(right). Whenthefirstheads
isobserved,themodelwhichstatesthatheadsareimpossible(coin
0)goestozeroprobability. 125

19
6.5 Probabilityfordifferentbent-coinmodels,givennodata(left),the
firsthalfofthedataset(middle),andtheentiredatasetof9tailsand
3heads(right). 126
6.6 Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata3headsand9tails,withamaximumat θ =0.25. 128
6.7 Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata3headsand9tails. Theareaunderthecurvefrom θ = 0
(the“allheads”coin)to θ =0.5(the“fair”coin)is0.954. 129
6.8 Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata3headsand9tails. Theareaunderthecurvefrom θ = 0
(the“allheads”coin)to θ = 0.28is0.5-halfthearea. Thisrepre-
sentsthemedianofthedistribution. 130
6.9 Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata3headsand9tails. Thevariousquartilesareshowninthe
plot,andsummarizedintheaccompanyingtable. 131
6.10Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata10headsand20tails. Thevariousquartilesareshowninthe
plot,andsummarizedintheaccompanyingtable. 135
7.1 TheNormalDistribution. 140
7.2 TheNormaldistributionwithdifferentlocationparameters, µ. 141
7.3 TheNormaldistributionwithdifferentdeviationparameters, σ. 142
7.4 TheStandardNormalDistribution(theNormaldistributioninthe
specialcasewhere µ = 0and σ = 1). Thepercentilesshownare
forpositions1-σ awayfromthecenter,2-σ away,and3-σ away. The
areawithin1-σ is0.68,within2-σ is0.95,and3-σ is0.99. Theselo-
cationsarethemostprevalentlyusedinanykindofstatisticaltest-
ing,andthuswewillseethemmanytimes. 143
9.1 Probabilitydistributionsforthesubsetofirispetallengths. Eachdis-
tributionfollowsaStudent-tform. 168
9.2 Probabilitydistributionsforthedifferencebetweenirispetallengths
fortheclosesttwoiristypes,VirginicaandVersicolor. Thedistribu-
tionfollowsaStudent-tform,andclearlyshowssignificantproba-
bility(greaterthan99%)forbeinggreaterthanzero. 169
9.3 MassofPenniesfrom1960to1974. 174
9.4 MassofPenniesfrom1960to1974,withbestestimatesand99%CI
(i.e. 3σ)uncertainty. 177

20
9.5 MassofPenniesfrom1960to2003,withbestestimatesand99%CI
(i.e. 3σ)uncertainty. 179
9.6 MassofPenniesfrom1960to2003,withbestestimatesforthetwo
truevaluesandtheir99%CI(i.e. 3σ)uncertaintyplotted. Thereis
clearlynooverlapintheircredibleintervals,thusthereisastatisti-
callysignificantdifferencebetweenthem. 180
9.7 Differenceintheestimatedvaluesofthepre-andpost1975pennies,
µ µ . Thevaluezeroisclearlyoutsideofthe99%intervalofthe
1 2
−
difference,thusthereisastatisticallysignificantdifferencebetween
thetwovalues µ and µ . 181
1 2
10.1Heights(ininches)andshoesizesfromasubsetofMcLaren(2012)
data. 194
10.2Posteriordistributionfortheslopeforthelinearmodelontheshoe
sizedatasubset. 195
10.3Posteriordistributionfortheinterceptforthelinearmodelonthe
shoesizedatasubset. 196
10.4Bestlinearfitfortheshoesizedatasubset. 196
10.5MinimizingtheMeanSquaredError(MSE)resultsinthebestlin-
earfitfortheshoesizedatasubset. 197
10.6TotalSATscorevsexpenditure(top)andthedistributionsfortheslope
(bottomleft)andintercept(bottomright). 198
10.7PercentofstudentstakingtheSATvsperpupilexpenditure(top)
andthedistributionsfortheslope(bottomleft)andintercept(bot-
tomright). 200
10.8Theposteriordistributionsforcoefficientsontheexpenditureterm,
thepercenttakingterm,andtheintercept. 201
11.1So-calledMCMC“chains”forparameter θ versustime. Observethat
thevaluesof θ startspreadevenlyfrom0to1atthebeginningand
thenthindowntoarangeofabout0.5-0.8withthemiddlearound
0.7(17/25=0.68). 212
11.2Distributionof θ,andthe95%credibleinterval. 213
11.3Chainsforparameters a, b,andthenoise σ. 213
11.4Data(blue)andpredictions(green)forthemodel-thewidthofthe
predictionsdemonstratestheuncertainty. 214
11.5Distributionsforparameters a and b (slopeandintercept). 215
11.6Chainsforparameter mu ,themeanofthedruggroup. 217
1
11.7Distributionforparameter mu ,themeanofthedruggroup. 217
1
11.8png 218
11.9Distributionforparameter δ,themeanofthedifferencebetweenthe
druggroupandtheplacebogroup. 218
C.1 Discreteuniformdistributionforvalues1to6. Thevalueforeach
is p(x ) =1/6. 230
i

21
C.2 Continuousuniformdistributionbetweenvalues0and1 231
C.3 Continuousuniformdistributionfortheplumberexample(Exam-
pleC.1). 231
C.4 Probabilityofgetting h headsin30flipsgivenapossibleunfaircoin.
Onecoinhas p =0.1,wherethemaximumisfor3heads(or1/10
ofthe30flips),but2headsisnearlyaslikely. Anotherhas p =0.5,
andisthefaircoinconsideredearlierwithamaximumat15heads
(or1/2ofthe30flips). Finally,anothercoinshownas p =0.8where
24heads(or8/10ofthe30flips)ismaximum. 232
C.5 Posteriorprobabilitydistributionforthe θ valuesofthebentcoin-
theprobabilitythatthecoinwilllandheads. Thedistributionisshown
fordata3headsand9tails. Thevariousquartilesareshowninthe
plot. 233
C.6 Thenormaldistribution. 234



List of Examples
1.1 Whatisthefractionofthefirstcardasajackgiventhatweknow
thatthefirstcardisafacecard?. . . . . . . . . . . . . . . . . 41
1.2 WhatisthefractionofcardsthatareJacksandaheart? . . . 42
1.3 WhatistheprobabilityofdrawingtwoKingsinarow? . . 42
1.4 Whatistheprobabilityofflippingtwoheadsinarow? . . . 43
1.5 MarginalizationandCardSuit . . . . . . . . . . . . . . . . . 46
1.6 Whatistheprobabilityofdrawingajack,knowingthatyou’ve
drawnafacecard? . . . . . . . . . . . . . . . . . . . . . . . . 47
2.1 Whatistheprobabilityofbothhavingcancerandgettinga
positivetestforit? . . . . . . . . . . . . . . . . . . . . . . . . 53
2.2 Whatistheprobabilityofbothnothavingcancerandgetting
apositivetestforit? . . . . . . . . . . . . . . . . . . . . . . . 54
2.3 Whatistheprobabilityofhavingcancergivenapositivetest
forit? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
2.4 IftheprobabilitythatitwillrainnextSaturdayis0.25andthe
probabilitythatitwillrainnextSundayis0.25,whatistheprob-
abilitythatitwillrainduringtheweekend? . . . . . . . . . 55
2.5 Whatistheprobabilityofthesumoftwodicegettingapar-
ticularvalue,say,7? . . . . . . . . . . . . . . . . . . . . . . . 56
2.6 Whatistheprobabilityofrollingasummorethan7withtwo
dice? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
2.7 Whatistheprobabilityofrollingvarioussumswithtwodice
eachwith20sides? . . . . . . . . . . . . . . . . . . . . . . . . . 57
2.8 Let’simaginewehavethecasewheretwopeoplemeetonthe
street. WhatistheprobabilitythattheybothhaveApril3as
theirbirthday? . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.9 Twopeoplemeetonthestreet,andweaskwhatistheprob-
abilitythattheybothhavethesamebirthday? . . . . . . . . 58
2.10 Whatistheprobabilitythatthreerandompeoplehavethesame
birthday? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.11 Whatistheprobabilitythatatleasttwohavethesamebirth-
day? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
2.12 Whatistheprobabilitythatatleasttwohavethesamebirth-
day? Aclevershortcut. . . . . . . . . . . . . . . . . . . . . . . 61

24
2.13 Whenyouhaveagroupof30people,likestudentsinaclass-
room,andyouaskwhattheprobabilityoffindingtwointhe
roomwiththesamebirthday,wouldyourintuitionsayitis
greaterorlessthan50%? . . . . . . . . . . . . . . . . . . . . 62
2.14 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: behindonedoorisacar;behindtheothers,goats.
Youpickadoor,sayNo. 1(butthedoorisnotopened),and
thehost,whoknowswhat’sbehindthedoors,opensanother
door,sayNo. 3,whichhasagoat. Hethensaystoyou,"Do
youwanttochangeyourchoicetodoorNo. 2?"Isittoyour
advantageordisadvantagetoswitchyourchoice,ordoesit
matterwhetheryouswitchyourchoiceornot? . . . . . . . 64
2.15 Imaginewehaveagamewithtwodoors: Behindonedoor
isacar;behindtheotherisagoat. Youpickadoor,sayNo.
1(butthedoorisnotopened),andthehost,whoknowswhat’s
behindthedoors,saysthatthereisa90%chancethatthecar
isbehinddoorNo. 2. Isittoyouradvantagetoswitchyour
choice? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
2.16 Thehost,whoknowswhat’sbehindthedoors,pointstoadoor,
choosingthecorrectdoor90%ofthetimeandtheincorrect
one10%. Youpickadoor,sayNo. 1,andthehostpointsto
doorNo. 2. Isittoyouradvantagetoswitchyourchoice? . 65
2.17 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: Behindonedoorisacar;behindtheothers,goats.
Youpickadoor,sayNo. 1(butthedoorisnotopened),and
thehost,whoknowswhat’sbehindthedoors,saysthatan-
otherdoor,sayNo. 3,hasa0%chanceofhavingacar,andthat
theremainingdoor(thatyouhaven’tchosen-i.edoorNo. 2)
hasa66%ofhavingthecar. Hethensaystoyou,"Doyouwant
topickdoorNo. 2?"Isittoyouradvantagetoswitchyourchoice?
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
2.18 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: behindonedoorisacar;behindtheothers,goats.
Youpickadoor,sayNo. 1(butthedoorisnotopened),and
thehost,whoknowswhat’sbehindthedoors,opensanother
door,sayNo. 3,whichhasagoat. Hethensaystoyou,"Do
youwanttochangeyourchoicetodoorNo. 2?"Isittoyour
advantageordisadvantagetoswitchyourchoice,ordoesit
matterwhetheryouswitchyourchoiceornot? . . . . . . . . 66
2.19 BeardandMustache-AnExaminationofIndependence . . 70
3.1 Whatistheprobabilityofflippingthreeheadsinarow,with
afaircoin? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
3.2 Whatistheprobabilityofflippingthirtyheadsinarow,with
afaircoin? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

25
3.3 Whatistheprobabilityofflippingtwoheadsinthreeflips,
withafaircoin? . . . . . . . . . . . . . . . . . . . . . . . . . 76
3.4 Whatistheprobabilityofflippingtenheadsinthirtyflips,
withafaircoin? . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.5 HowmanywayscanwerearrangetheuniquesymbolsA,B,
C,andD? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
3.6 HowmanywayscanwerearrangethesymbolsA,A,A,and
D? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
3.7 Howmanywaysarethereofrearrangingthesymbols“AA
ADD”? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.8 Whatistheprobabilityofflippingtenheadsinthirtyflips,
withafaircoin? . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.9 Whatistheprobabilityofgetting17ormoreheadsin30flips? 81
4.1 Whatistheprobabilityofdrawinga9,giventhatweknow
thatwe’reholdingtheHighDeck? . . . . . . . . . . . . . . 97
4.2 Whatistheprobabilitythatyouareholdingoneofeitherthe
HighortheLowDeckhavingdrawnfive9’sinarowfromthat
deck? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
4.3 Whatistheprobabilitythatyouareholdingoneofeitherthe
HighortheLowDeckhavingdrawn m 9’sinarowfromthat
deck,where m standsforanumber(m =1,2,3, )? . . . . 103
···
4.4 Whatistheprobabilitythatyouareholdingoneofeitherthe
High,Low,orNinesDeckhavingdrawn m 9’sinarowfrom
thatdeck? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
5.1 Isitbettertoswitchdoors? -MontyHallProblemrevisited 117
6.1 Whatisthebestestimateoftheprobabilityofabentcoinflip-
pingheads,giventheobservationof9tailsand3heads? . . 132
7.1 GivenaNormaldistributionwithameanof µ = 150anda
σ =20,whatisthemostlikelyvalue? . . . . . . . . . . . . . 143
7.2 GivenaNormaldistributionwithameanof µ =150and σ =
30,whatistheprobability P(x >170) . . . . . . . . . . . . . 143
7.3 WehavetwoNormaldistributions P(x) =Normal(µ =8,σ =
2) and P(y) = Normal(µ = 20,σ = 7). Whatisthedistri-
butionfor z = y x? . . . . . . . . . . . . . . . . . . . . . . 145
−
7.4 EstimatingtheTrueLengthofanObject . . . . . . . . . . . . 147
7.5 EstimatingtheTrueLengthofanObject...Again . . . . . . . 148
7.6 EstimatingtheTrueLengthofanObject...YetAgain . . . . . 153
9.1 Irispetallengths-Bestestimate . . . . . . . . . . . . . . . . 165
9.2 Irispetallengths-Adifferentspecies? . . . . . . . . . . . . . 166
9.3 Irispetallengths-Significantlydifferent? . . . . . . . . . . . 166
9.4 BallBearingSizes . . . . . . . . . . . . . . . . . . . . . . . . . 168
9.5 Whatisthebestestimate(anduncertainty)foreachofthetwo
productionlinesofballbearings?. . . . . . . . . . . . . . . . 169

26
9.6 Isitreasonabletobelievethatthereisadifferenceinthesize
producedbetweenthetwolines? . . . . . . . . . . . . . . . . 170
9.7 TheSunriseProblem . . . . . . . . . . . . . . . . . . . . . . . 170
9.8 CancerRates . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
9.9 CancerRates-NormalApproximation . . . . . . . . . . . . 171
9.10 Willitrainonthe4th ofJuly? . . . . . . . . . . . . . . . . . . 172
9.11 HotHandReexamined . . . . . . . . . . . . . . . . . . . . . . 172
9.12 MassofthePenny,Model1-OneTrueValue. . . . . . . . . 173
9.13 MassofthePenny,Model1-OneTrueValuewithMoreData176
9.14 MassofthePenny,Model2-TwoTrueValues . . . . . . . . 179
C.1 Youcallaplumber,andtheysaythattheycancomeanytime
inthenext4hours. Theprobabilityofthemarrivingatany
particulartimecanberepresentedwithauniformdistribu-
tion. Whatistheprobabilitythattheyarriveinthefirst20min-
utesofthesecondhour? . . . . . . . . . . . . . . . . . . . . 230
D.1 UsageoftheCredibleIntervalTablefortheNormalDistribu-
tion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
D.2 UsageoftheCredibleIntervalTablefortheStudent’s t Dis-
tribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237

List of Tables
1.1 Roughguidefortheconversionofqualitativelabelstoprobability
values. 51
3.1 TotalCorrectGuessesfromStudents“Predicting”theResultsof50
CoinFlips. Shownaretheresultsofafirstroundandasecondround
ofguessing. 86
3.2 PerformanceintheSecondRoundofStudents“Predicting”theRe-
sultsof50CoinFlips. Shownaretheresultsforthosestudentswho
performedbestinthefirstround(left),andthosethatperformedworst
inthefirstround(right). 86
3.3 106MaleStudentHeights(incm)fromaSurvey. 88
4.1 Drawing m 9’sinarow,fromeitheraHighDeckorLowDeck. 104
6.1 Probabilitiesforflippingheadsgivenacollectionofbentcoins 121
6.2 Probabilityfordifferentbent-coinmodels,giventhedata=9tails,3
heads. Themiddlecolumnisthenon-normalizedvaluefromBayes’
Rule,needingtobedividedby K (thesumofthemiddlecolumn)
togetthefinalcolumnwhichistheactualprobability. 123
8.1 Roughguidefortheconversionofdeviationsawayfromzeroand
thequalitativelabelsforprobabilityvaluesforbeingasignificantde-
viation. 161
9.1 Irispetallengths,incentimeters,forIristypeSetosa. 165
9.2 Subsetofirispetallengths,incentimeters,foriristypesVirginica,Se-
tosa,andVersicolor. 166
9.3 Productionlinesareproduceaballbearingwithadiameterofap-
proximately1micron. Tenballbearingswererandomlypickedfrom
theproductionline(i.e. theFirstline)atonetime,andthenagainfor
adifferentproductionline(i.e. theSecondline). Romano,A.(1977)
AppliedStatisticsforScienceandIndustry. 169
9.4 MassofPenniesfrom1960to1974. 174
9.5 MassofPenniesfrom1989to2003. 176

28
10.1Heights(ininches)andshoesizesfromasubsetofMcLaren(2012)
data. 193

Proposal
Iwouldliketoproposeanewintroductorystatisticalinferencetext-
book,whichIbelievetakesafreshlookatacoursethatfitsinto
nearlyeveryquantitativemajoratuniversities.
Initial Motivation
Mymotivationforthisprojectstemsfrommydissatisfactionwithtra-
ditionalapproachestothetopic,andmybeliefthatthereisabetter
way. Afirstsemesterstatisticscourseisgenerallydividedintothe
followingfourparts:
I BasicStatisticalConcepts
• Basicstatisticalconceptsincludingpopulation,parameter,sam-
ple,andstatistic
• Typesofdata(ordinal,time-series,etc...),andsamplingmethod-
ology
• Organizingthedatavisuallyorgraphically-includinghis-
tograms,piegraphs,boxplots,andstem-and-leafplots
• Statisticalcomputationsincludingmean,median,mode,stan-
darddeviation,andpercentiles
II Probability
• Propertiesofunions,intersections,conditionalprobability,
independenceandmutualexclusivity
• Permutationsandcombinations
• Discretedistributions
• Continuousdistributions
• Normaldistribution
III One-sampleStatistics
• Confidenceintervals

30
• Samplingdistributions
• Computationsinvolvingthenormaldistribution,t-distribution,
andbinomialdistribution(forproportions)
• Hypothesistesting
IV Two-sampleStatistics
• Twosampleproblems-expandingtopicsfromPartIIItotwo
variables
Obviously,thereissomevariabilitytothesetopics,butasonecan
seefrommostintroductorystatisticstextbooks,thereisaconsistent
approach. Mymainconcernsaboutthetraditionalapproachcanbe
summarizedasfollows:
1 PartII(probability)generallycoversatleastonequarterofthema-
terialinanintroductorystatisticscourse. Thereisashiftfromdata
collectionandanalysis(PartI)toprobabilitytheory. Subsequently,
PartIIIshiftsbacktoadatacenteredapproachandonlyasmall
portionofPartIIgenerallyappliesinPartIII.Thisdisconnectbe-
tweenPartsI,II,andIII,impedesthelearningprocess. Itseemsto
thestudentsasifthepartsarerelatedsomehow,buttheconnec-
tionisrarelymade. Thestudentsarethenleftwithafeelingthat
thecourseconcernstwocompletelyunrelatedtopics: probability
andstatistics.
2 Thenormaldistributioniscoveredrepetitivelythroughoutmany
chaptersofmostintroductorystatisticsbooks. Thecoverageis
includedinsectionssuchas: empiricalbell-shapedcurve(Part
I),normaldistributionasatypeofcontinuousdistribution(Part
II),samplingdistributions(PartIII),intervalestimation(PartIII),
hypothesistesting(PartIII),andtwopopulationtesting(Part
IV).Thereisredundantfocusonthenormalandt-distributions.
Thesetopicsarecloselyrelated,butnothandledcohesively. More
importantly,thereislittleornodiscussionoftheassumptionsof
thenormalmodelorhowtotellwhatconstitutes“closeenough”
tonormal. Inaddition,thereisgenerallyequalconsiderationgiven
totherarepracticalsituationinwhichthestandarddeviationis
known(andknowingthisdoesnotgenerallyaltertheresultmuch
atall).
3 Aftertheconceptofa“statistic”iscovered,therearemanychap-
terswhichrepeatessentiallythesameproblemmultipletimes,
fromonlyslightlydifferentperspectives. Thisgivesthestudenta
feelingthattheseareallverydifferentproblems,despitetheap-
pearances,andleadsthestudenttoapproachsolvingproblems

31
likea“cookbook”: justfindtherightrecipefortherightproblem.
Thefundamentalunderstandingofstatisticalinferenceisunder-
minedbythisapproach.
Itismyviewthatthetraditionalapproachdetractsfromstudent
understanding,withits“cookbook”perspective,disjointedcover-
ageofprobability,andthealmostexclusionaryfocusonthenormal
distribution.
A New Approach
Inthefieldofstatisticalinference,therearetwoprimaryschoolsof
thought. Eachhasitsproponents,butitisgenerallyacceptedthaton
allproblemscoveredinanintroductorycourse,thatbothapproaches
arevalidandleadtothesamenumericalvalueswhenappliedto
actualproblems. Onlyoneoftheseapproachesiscoveredinatra-
ditionalcourse,whichdeniesthestudentsaccesstoanentirefield
ofstatisticalinference. Thetraditionalapproach,alsocalledthefre-
quentistororthodoxperspective,leadsalmostdirectlytoproblem(1)
1
above. Theotherapproach,alsocalledProbabilityTheoryasLogic , 1E.T.Jaynes. ProbabilityTheory:
derivesallstatisticalinferencefromprobabilitytheorydirectly. Itis TheLogicofScience. Cambridge
UniversityPress,Cambridge,2003.
thisapproachthatIhopetoexposestudentstoinanintroductory
EditedbyG.LarryBretthorst
course.
Theprobabilitytheoryapproachtostatisticalinferencehasseveral
benefits:
1 Allofthesameproblemsashandledtraditionallycanbehandled
2
withthisperspective,yieldingexactlythesameanswers . 2Onereasonwhy“Probability
theoryasLogic”conceptsare
2 Statisticalinferenceistheoreticallygroundedinprobabilitytheory, coveredonlyinadvancedcourses
which,althoughadmittedlybeyondanintroductorycourse,avoids isthemisperceptionthattheyare
applicableonlytomoreadvanced
the“cookbook”approach,wheredifferentproblemsneeddifferent
problems,andnotapplicableto
methods,thatstudentstakeawayfromthetraditionaltextbooks. problemsnormallyfoundinan
introductoryclass.Thefactthat
Hereallproblemsusethesamemethod,derivedfromprobability
thismisperceptionexistsisastrong
theory. argumentforabooklikethisone,
todispelthismisperceptionandto
3 Thereasoningprocessusingtheprobabilitytheoryperspective
communicatebothtostudentsand
ismoreintuitivethantheorthodoxperspective,especiallywhen instructorsalikethevalueofathis
approachtobasicproblems.
dealingwithhypothesistesting.
Forexample,everystatisticsinstructorfacesthechallengeof
gettingstudentstointerpret p-valuesproperly,andthelogicbe-
hindsettingupnull-hypotheses. Theyhavetocombatthestu-
dents’initialintuitionthatthe p-valuerepresentsthe“probability
thatthenullistrue,”andmanystudentsneverreallyobtainthe
properunderstanding. Ihaveevenheardinstructorsuseitthis
way.

32
IntheProbabilityTheoryasLogicperspective,thissamecalcu-
latedvalueisinterpretedexactlylikethestudents’initialintuition!
Thus,testinghypotheses,estimatingparameters,anddetermining
uncertaintiesarefarmoredirectandintuitiveusingthisapproach
thanthetraditionalapproach.
What I Am Proposing
Thistextcanhelpsolvethechallengesdescribedabove,andmore.
Byfocusingonmodelsanddata,asopposedtopopulationsand
samples,thistextcanmorecohesivelybridgethetopicsdescribedin
PartsI,II,andIIIabove. Probabilitywillbeintroducedasanatural
partofsolvingproblems,asopposedtoitsstandalonetreatment
traditionallydoneintoday’stexts.
Inthistext,IwillusetheProbabilityTheoryasLogicapproach
appliedtothesameproblemsthataretraditionallycovered. This
viewpointcangreatlyenhanceourunderstandingofstatisticsand
canhandletopicssuchasconfidenceintervalsandhypothesistesting
inaveryintuitivemanner. Statisticalinferencecoveredinthisway
alsoaddressesreal-lifequestionsthatarenotaddressedbytraditional
3
statisticalmethods. 3Oneofthereasonswhythisap-
Finally,thiswillbeaproblemorientedtextbook. Itisimperative proachisusuallycoveredonlyin
moreadvancedcoursesisthediffi-
thattheproblemsarecohesivewiththepedagogy. Iwillalsoplanto
cultyofthemathematicsgenerally
usetechnology,whereappropriate,tofurtherstudentlearningand associatedwithit.Orthodoxstatis-
ticsmakesheavyuseofsampling,
makethetextbookmoreinteractive.
whichisdeemedmoreintuitive
Attheleveltargetedforthisbook,thereisonlyonetextbookthat thanprobabilitydistributions.It
Iknowofthatcoversinferencefromtheperspectiveproposedhere, ismyintentiontostartwithlow-
dimensionalcases,buildingto
andthatisDonaldBerry’sbookStatistics: ABayesianPerspective,
distributions,andtoaugmentall
1996. Itismyintentiontomodernizetheapproach,andincludesome conceptswithnumericalexercises.
topicsthatarenotcovered,specificallyfromthephysicalsciences
andbusiness.

1 Introduction to Probability
Life’smostimportantquestionsare,forthemostpart,nothingbutprobability
problems. -Laplace
In1968ajuryfounddefendantMalcolmRicardoCollinsandhis
1
wifedefendantJanetLouiseCollinsguiltyofseconddegreerobbery . 1J.Sullivan. Peoplev.Collins,
Thedecisionhingedonthetestimonyofbystanders,whichstated 68cal.2d319,1968. URLhttp:
//scocal.stanford.edu/opinion/
thattheperpetratorshadbeen“blackmale,withabeardandmous-
people-v-collins-22583
tache,andacaucasianfemalewithblondehairtiedinaponytail,”
andthattheyescapedina“yellowmotorcar.” Amathematician
testifiedthattheoddsagainstthiscouplebeinginnocentwereone
intwelvemillion,andthiswasenoughforthejurytoconvict. Later,
inanappeal,theCaliforniaSupremeCourtreversedthedecision
primarilybecauseoflackofevidence,andfaultyinference.
Inanothercase,SallyClarkwasconvictedin1999ofthemurder
2
ofhertwoyoungsons . Again,thetestimonyhingedonastatistical 2LordJusticeKay. RvsSally
argument-thechancesofonebabydyingintheirbed1in8500,so Clark,April2003. URLhttp:
//www.bailii.org/ew/cases/EWCA/
thereforethechancesoftwoofthemdyinginthesamewayisthe
Crim/2003/1020.html
squareofthis,or1in73million. Severalyearslater,andapublic
statementfromtheRoyalStatisticalSocietyhighlightingtheerro-
neouslogic,SallyClarkwasreleased-althoughsheneverovercame
theresultingdamagetoherlifethattheconvictionhadcaused.
Wewillcoverthesecasesinmoredetaillater,andwhythein-
ferencewasfaulty,butIintroducethestoriesherefortworeasons.
First,istopointoutthattherearecasesinwhichproperstatistical
inferencecanbealifeanddeathmatter. Second,itistohighlightthe
factthatsuchinferencecanruncountertoone’sintuition. Partofthe
purposeofthisbookistoretrainyourintuitionsandyourhabitsof
intuitiontoavoidsuchfailures.
Wehavetomakedecisionsnearlyeverysecondofourlives,and
thosedecisionsarebasedonourstateofknowledge. Unfortunately,
wearenever100%sureofanyinformationinourlives,soweare
constantlyforcedtomakedecisionsinthefaceofuncertainty. In
manycasesourcommonsenseisenoughtomakesophisticateddeci-
sions,takingintoaccounttheuncertainnatureofthesituation. How-
ever,therearemanytimeswhereourcommonsenseisnotenoughto

34 statistical inference for everyone
quantitativelyresolvethelevelofuncertainty,andmakevalidinfer-
ences. Itisinthesecasesthatstatisticalinferenceismostuseful.
Statisticalinferencereferstoafieldofstudywherewetrytoinfer
unknownpropertiesoftheworld,givenourobserveddata,inthe
faceofuncertainty. Itisamathematicalframeworktoquantifywhat
ourcommonsensesaysinmanysituations,butallowsustoexceed
ourcommonsenseincaseswherecommonsenseisnotenough. Ig-
noranceofproperstatisticalinferenceleadstopoordecisionsand
wastedmoney. Aswithignoranceinanyotherfield,ignoranceofsta-
tisticalinferencecanalsoallowotherstomanipulateyou,convincing
youofthetruthofsomethingthatisfalse.
Forexample,in1978aRussiansatellitedeviatedfromitsorbitand
3
becameincreasinglyerratic,andwasgoingtocrashintotheEarth. 3LHeaps. Operationmorning
Thissortofeventoccursfromtimetotime,evenincludingarecent light. Paddington,S.l,1978. ISBN
0709203233
crashofaUSspysatellitein2008. 4 Therewasalocalnewsbroadcast
4JamesOberg. U.S.satelliteshoot-
abouttheimpendingRussiansatellitecrashwhichsaidsomething down:Theinsidestory. IEEE
like,“thescientistshadstudiedthetrajectoryofthesatellite,and
Spectrum,2008
determinedthattherewasonlya25%chanceofitstrikingland,and
evenamuchsmallerchancestrikingapopulatedarea.” Thereport
wasclearlydesignedtocalmthepublic,andconvincethemthat
thescientistshadagoodhandleonthesituation. Unfortunately,
givenalittlethought,onerealizesthattheEarth’ssurfaceconsists
ofabout25%landand75%water,soifyouknewnothingaboutthe
trajectoryofthesatellite,youwouldsimplystatethatithada25%
chanceofstrikingland. Insteadofcommunicatingknowledgeofthe
situation,thenewsbroadcastcommunicated(tothosewhoknew
basicstatisticalinference)thateitherthescientistswereincomplete
ignoranceofthetrajectoryorthereporterhadmisinterpretedacasual
statementaboutprobabilitiesanddidn’trealizewhatwasimplied.
Eitherway,theintentofthemessageandthecontentofthemessage
(tothosewhounderstoodbasicprobability)wereindirectconflict.
1.1 Models and Data
Therearetwomainaspectsofstatisticalinference: descriptionof
dataandmodelanalysis. Inthedescriptionofdata,oneattemptsto
summarizeasetofdatawithasmallersetofnumbers. Gradesin
theclassroomaresummarizedbytheaverage,votesinastateare
summarizedbyapercentage,etc... Thissmallerdescriptionofthe
dataisusefulforbothpracticalandtheoreticalreasons. Itismore
expedienttocommunicateasmallsetofnumbersthantheentiredata
set,anditisalmostalwaysthecasethatthedetailedpropertiesofa
setofdataarenotrelevanttothequestionsthatyouareasking.
Amodelreferstoamathematicalstructurewhichisusedtoap-

introduction to probability 35
proximatetheunderlyingcausesofthedata,andunifyseemingly
unrelatedproblems. Onemayhavea(mathematical)modelfora
coinflipwhichignoresallofthedetailsoftheflip,thebounce,and
thecatchandsummarizesthepossibleresultsbyasinglenumber:
thechancethatthecoinwillcomeupheads. Youmaythenusethat
samemodeltodescribethevotingbehaviorofcitizensduringapres-
identialelection,ortodescribetheradioactivedecayofparticlesina
physicsexperiment. Themathematicsisidentical,buttheinterpreta-
tionofthecomponentsofthemodelwillbedifferentdependingon
theproblem. Modelssimplify,bysummarizingdatawithasmallset
ofcauses,andtheyareusedforinference,allowingonetopredictthe
outcomeofsubsequentevents.
Thegoalofstatisticalinferenceisthentotakedata,andupdate
ourknowledgeaboutvariouspossiblemodelsthatcandescribethe
data. Thisoftenmeansdecidingwhichofseveralmodelsisthemost
likely. Itcanalsoentailtherefinementofasinglemodel,giventhe
newdata. Alloftheseactivitiesarecloselyrelatedto(andperhaps
identicalto)themethodsinscience. Whatwearetryingtodois
makethebestinferencesfromthedata,improveourinferencesas
newdatacomein,andplanwhatdatawouldbethemostusefulto
improveourinferences. Inanutshell,theapproachis:
InitialInference+NewData ImprovedInference
→
Inordertodealwithawidevarietyofproblems,werequirea
minimalamountofmathematicalstructureandnotation,whichwe
introduceinthischapter.
1.2 What is Probability?
Probabilitytheoryisnothingbutcommonsensereducedtocalculation. -
Laplace
Whenyouthinkaboutprobability,thefirstthingsthatmightcome
tomindarecoinflips(“there’sa50-50chanceoflandingheads”),
weatherreports(“there’sa20%chanceofraintoday”),andpoliti-
calpolls(“theincumbentcandidateisleadingthechallenger53%to
47%”). Whenwespeakaboutprobability,wespeakaboutapercent-
agechance(0%-100%)forsomethingtohappen,althoughweoften
writethepercentageasadecimalnumber,between0and1. Ifthe
probabilityofaneventis0thenitisthesameassayingthatyouare
certainthattheeventwillneverhappen. Iftheprobabilityis1thenyou
arecertainthatitwillhappen. Lifeisfullofuncertainty,soweassigna
numbersomewherebetween0and1todescribeourstateofknowl-
edgeofthecertaintyofanevent. Theprobabilitythatyouwillget

36 statistical inference for everyone
struckbylightningsometimeinyourlifeis p = 0.0002,or1outof
5000. Statisticalinferenceissimplytheinferenceinthepresenceof
uncertainty. Wetrytomakethebestdecisionswecan,givenincom-
pleteinformation. Inthisbook,ourapproachisto
Onecanthinkofprobabilityasamathematicalshort-handforthe determine,foreachproblem,what
degreeofconfidencewehavein
commonsensestatementswemakeinthepresenceofuncertainty.
allofthepossibleoutcomes.The
Thisshort-hand,however,becomesaverypowerfultoolwhenour approachofstatisticalinference
coveredinthisbookisaboutthe
commonsenseisnotuptothetaskofhandlingthecomplexityofa
procedureofmostrationallyassign-
problem. Thus,wewillstartwithexamplesthatwillperhapsseem ingvariousdegreesofconfidence
simpleandobvious,andmovetoexampleswhereitwouldbea (whichwecallprobability)tothe
possibleoutcomesofsomeprocess
challengeforyoutodeterminetheanswerwithoutthepowerof
usingalltheobjectivelyavailable
statisticalinference. data.
Let’swalkthroughasimplesetofexamplestoestablishthenota-
tion,andsomeofthebasicmathematicalpropertiesofprobabilities.
Card Game
Asimplegamecanbeusedtoexploreallofthefacetsofprobability.
Weuseastandardsetofcards(Figure1.1)asthestartingpoint,and
usethissystemtosetuptheintuition,aswellasthemathematical
notationandstructureforapproachingprobabilityproblems.
Figure1.1:Standard52-carddeck.
13cardsofeachsuit,labeled
Spades,Clubs,Diamonds,Hearts.
5
WestartwithwhatIsimplycallthesimplecardgame ,whichgoes 5Inthisdescriptionofthegame,
wedonotreshuffleaftereachdraw.
Thedifferencesbetweenthisnon-
reshuffledversionandtheonewith
reshufflingwillbeexploredlater,
butwillonlychangesomesmall
detailsintheoutcomes.

introduction to probability 37
like:
Fromastandardinitiallyshuffled

d
ca
e
r
c
d
k,
it
w
i
e
sa
d
n
ra
d
w
se
o
t
n
i
e
ta
c
s
a
i
r
d
d
e
,
.
n
W
ot
e
e
t
w
he
h
n
at
simplecardgame drawanothercard,notewhatcard (1.1)
≡ 
i
t
t
h
i
e
s
re
an
a
d
re
s
n
e
o
ti
m
ta
o
s
r
i
e
de
c
.
ar
C
d
o
s
n
,
t
n
in
ot
u
in
e
g
un
ea
ti
c
l
h
onealongtheway.
Therearecertainprinciplesthatguideusindevelopingthemath-
ematicalstructureofprobability. Westartwithsomecommonsense
notions,writteninEnglish,andthenwritethemasgeneralprinci-
ples. Theseprinciples,then,constrainourmathematicssothatwe
canapplytheideasquantitatively.
Whenasked“whatistheprobabilityofdrawingaredonthe
firstdraw?” youwouldgenerallysay50-50,or50%,orequivalently
writtenasaprobability, P(R ) = 0.5. Thereasonforthisisthat
1
wearecompletelyignorantoftheinitialconditionsofthedeck(i.e.
whereeachcardislocatedinthedeckaftertheinitialshuffling).
Giventhislevelof(orlackof)knowledge,wecouldswapthecolors
ofthetwosuitsandwewouldhaveanequivalentstateofknowledge
-theproblemwouldbeidentical. Wewillkeepcomingbacktothis
concept,butingeneral:
PrincipleofKnowledgeandProbabilityEquivalentstatesof PrincipleofKnowledgeand
knowledgemustyieldequivalentprobabilityassignments. ProbabilityEquivalentstatesof
knowledgemustyieldequivalent
Becauseofthisprinciple,weareledtotheconclusionthat
probabilityassignments.
P(R ) = P(B )
1 1
where R representsthestatement“aredonthefirstdraw”and B
1 1
represents“ablackonthefirstdraw.” Becausethesearetheonlytwo
options,andtheyaremutuallyexclusive,thentheymustaddupto1.
Thuswehave
P(R ) =1 P(B )
1 1
−
whichleadsdirectlytoouroriginalassignment
P(R ) = P(B ) =0.5
1 1
MutuallyExclusiveIfIhavealistofmutuallyexclusiveevents,then MutuallyExclusiveIfIhavea
thatmeansthatonlyoneofthemcouldpossiblybetrue. Example listofmutuallyexclusiveevents,
thenthatmeansthatonlyone
eventsincludeflippingheadsortailswithacoins,rollinga1,2,
ofthemcouldpossiblybetrue.
3,4,5or6ondice,ordrawingaredorblackcardfromadeckof Examplesincludestheheads
andtailsoutcomesofcoins,or
thevaluesofstandard6-sided
dice.Intermsofprobability,this
meansthat,foreventsAandB,
P(AandB)=0.

38 statistical inference for everyone
cards. Intermsofprobability,thismeansthat,foreventsAandB,
P(A and B) =0.
NonMutuallyExclusiveIfIhavealistofeventsthatarenotmutu- NonMutuallyExclusiveIfIhave
allyexclusive,thenitispossiblefortwoormoretobetrue. Examples alistofeventsthatarenotmutually
exclusive,thenitispossiblefor
includeweatherwithrainandcloudsorholdingthehighandthe
twoormoretobetrue.Examples
lowcardinapokergame. includeweatherwithrainand
cloudsorholdingthehighandthe
Now,thiswasalong-windedwaytogettotheanswerweknew
lowcardinapokergame.
fromthestart,butthatishowitmustbegin. Westartworkingthings
outwhereourcommonsenseisstrong,sothatweknowweare
proceedingcorrectly. Wecanthen,confidently,applythetoolsin
placeswhereourcommonsenseisnotstrong.
Insummary,withnomoreinformationthanthattherearetwo
mutuallyexclusivepossibilities,weassignequalprobabilitytoboth.
Ifthereareonlytwocolorsofcardsinequalamounts,redandblack,
thentheprobabilityofdrawingaredis P(R ) =0.5andtheprobabil-
1
ityforablackisthesame, P(B ) =0.5.
1
Other Observations
Ifinsteadofjustthecolor,wewereinterestedinthesuit(hearts,
diamonds,spades,andclubs),thentherewouldbefourequaland
mutuallyexclusivepossibilities. Wehaveacertainnumberofpossi-
bilities,andourstateofknowledgeisexactlythesameifwesimply
swaparoundthelabelsonthecards. Ifwe’reinterestedinthespecific
card,notjustthesuit,thelogicisthesame. Thus,wehave
P( ) = P( ) = P(♦) = P(♥)
♠ ♣
andfordrawingonespecificcardfromthedeck,
P(A ) = P(2 ) = P(3 ) = = P(K♥)
♠ ♠ ♠ ···
Further,theyallmustaddupto1,sowegetforsuits
P( )+P( )+P(♦)+P(♥) =1
♠ ♣
andforthespecificcardfromthedeck,
P(A )+P(2 )+P(3 )+ +P(K♥) =1
♠ ♠ ♠ ···
(cid:124) (cid:123)(cid:122) (cid:125)
52cards
Puttingittogether,wegetforthesuits
1
P( ) = P( ) = P(♦) = P(♥) =
♠ ♣ 4

introduction to probability 39
andforthespecificcard
1
P(A ) = P(2 ) = P(3 ) = = P(K♥) =
♠ ♠ ♠ ··· 52
ProbabilitiesforMutuallyExclusiveEvents Ingeneral,formutu- ProbabilitiesforMutuallyExclu-
allyexclusiveevents,wehave siveEvents
(numberofcasesfavorabletoA)
P(A)=
(totalnumberofequallypossiblecases)
(numberofcasesfavorabletoA)
P(A) = (1.2)
(totalnumberofequallypossiblecases)
1.3 Conditional Probability
Itisimportanttounderstandthatprobabilityreflectsourstateof
knowledgeaboutthesystem. Asourknowledgechanges,sodoour
probabilityassignments. Aswegainmoreinformation,wechange
ourprobabilityassignments. Twopeopleobservingthesamesystem,
butwithdifferentinformationaboutthesystem,willgivedifferent
probabilityassignments. Allweneedtomakesureprobabilitytheory
matchesourcommonsenseisfortwopeoplewiththesamestateof
knowledge,orthesameinformation,toyieldidenticalprobability
assignments.
Becauseourinformationaboutasystemissoimportantinassign-
ingprobabilities,weintroduceawayofwritingitmathematically
thatwewillusefortherestofthebook. Itwillbegoodforthereader
togetusedtoreadingthemathematicalshort-handinEnglishin
ordertogainanunderstandingforwhatitmeans.
Probability Notation
Inmath,wechoosetoabbreviatelongsentencesinEnglish,inorder
tousetheeconomyofsymbols. Inthisbookwechooseamiddle-
groundbetweenmathematicalsuccinctnessandtheeaseofunder-
standingEnglish. Westartwiththesimplecardgame(Equation1.1)
Wethendefineanewsymbol, ,whichshouldbereadas“given.”
|
Whenthereisinformationgivenwecallthisprobabilityconditional
onthatinformation. Whenwewritethefollowing:
P(redonfirstdraw simplecardgame) (1.3)
|
or
P(R simplecardgame) (1.4)
1
|
thisisshortfor

40 statistical inference for everyone
“Theprobabilityofdrawingaredonthefirstdraw,giventhatwehavea
standardinitiallyshuffleddeckandwefollowtheprocedurewherewedraw
onecard,notewhatcoloritisandsetitasideandcontinuedrawing,noting,
andsettingasideuntiltherearenomorecards.”
Onecaneasilyseethatthemathematicalnotationisfarmore
efficient. Itisimportanttobeabletoreadthenotation,becauseit
describeswhatweknowandwhatwewanttoknow.
ConditionalProbabilityWheninformationisgiven,andex- ConditionalProbabilityWhen
pressedontheright-handsideofthe sign,wesaythattheproba- informationisgiven,andexpressed
| ontheright-handsideofthe
bilityisconditional. P(I’mgoingtogetwettoday rainingoutside) is |
sign,wesaythattheprobability
|
anassessmentofhowlikelyitisthatIwillgetwetgiven,orcondi- isconditional. P(I’mgoingtoget
wettodayrainingoutside)isan
tionalon,thefactthatitisrainingoutside. Clearlythisnumberwill |
assessmentofhowlikelyitisthat
bedifferentifitwasconditionalonthefactthatitissunnyoutside- Iwillgetwetgiven,orconditional
differentstatesofknowledgeyielddifferentprobabilityassignments. on,thefactthatitisrainingoutside.
Clearlythisnumberwillbediffer-
Whenweputacomma(“,”)ontherightsidethenwereadthisas
entifitwasconditionalonthefact
“andweknowthat.” Forexample,whenwewritethefollowing: thatitissunnyoutside.
Causation.Imaginewehavea2-card
game:asmalldeckwithonered
cardandoneblackcard,andIdraw
P(redonseconddraw simplecardgame,redonfirstdraw) (1.5)
aredcardfirst.Clearlythismakes
|
theprobabilityofdrawingredas
or thesecondcardequaltozero-it
can’thappen.We’retemptedto
interpret
P(R simplecardgame,R ) (1.6)
2 1
| P(R2| R 1,2-cardgame)=0
thisisshortfor tomeanthatbecausewedrewared
onthefirstdraw,thiscausesthe
impossibilityofdrawingtheredonthe
“Theprobabilityofdrawingaredontheseconddraw,giventhatwehavea
second-thereisonly1redcardafter
standardinitiallyshuffleddeckandwefollowtheprocedurewherewedraw
all,anddrawingitseemstocause
onecard,notewhatcoloritisandsetitasideandcontinuedrawing,noting, theimpossibilityofdrawingredin
andsettingasideuntiltherearenomorecardsandweknowthatwedrewa thefuture.However,considerthe
redonthefirstdraw.” following:
P(R
1|
R2,2-cardgame)=0
1.4 Rules of Probability whichis,ifweknewthatthesecond
cardwedrewwasred,thenit
makesitimpossibletohavedrawn
Fromtheruleformutuallyexclusiveevents(Equation1.2),weassign
aredcardasthefirstcard.Thisis
thefollowingprobabilitiesforthefirstdrawfromthisdeck 6 : justastrueasthepreviouscase,
however,youcan’tinterpretthisas
causation-theseconddrawdidn’t
• P(10) = 4
52 causethefirstdraw.
Instead,probabilitystatementsare
• P(♥) = 13 = 1 statementsoflogic,notcausation.One
52 4
canuseprobabilitiestodescribe
• P(10♥) = 1 causation(i.e. P(rain | clouds)),but
52 thestatementsofprobabilityhave
notimecomponent-laterdraws
• P(facecard) = 1 5 2 2 fromthedeckofcardsactexactly
thesameasearlierones.
• P(numbercard) = 40
52 6AfacecardisdefinedtobeaJack,
Queen,orKing.Anumbercardis
definedtobeAce(i.e.1)through
10.

introduction to probability 41
Itturnsoutthatmathematically,therulesforfractionsofthings
andofprobabilitiesarethesame. Thus,togainanunderstanding
fortherulesofprobability,wewillcalculatefractions(whichare
moreimmediatelyintuitive),andthensummarizethesamerulefor
probabilities.
Negation Rule
InthissectionI’llusetheletter F forfraction,andwecandetermine
thevaluessimplybycounting. Thefractionofcardswhicharehearts
(♥)is
Either-orfallacy.Thenegation
rule,shouldnotbetakentoimply
thateverythingis“blackand
F(♥) = 13 = 1 white,”or“thereareonlytwo
52 4 sidestoeverystory.”Itreallyis
justastatementoflogic,should
Thefractionofcardswhicharenothearts(i.e. the3othersuits)is: becarefullyconsideredandhas
somelimitations.Forexample,the
13 3 3
F(not♥) = × = followingistrue,
52 4
P(objectisblack)+P(objectisnotblack)=1
Thesenumbersadduptoone: F(♥)+F(not♥) = 1. Wecandothis
However,thisdoesnotmeanthe
withmorecomplexstatements. samethingas
12 P(objectisblack)+P(objectiswhite)=1
F(firstcardisafacecard) = (cid:54)
52 “Notblack”isnottheequivalentof
40 “white.”Itcouldbered,orgray,or
F(firstcardisnotafacecard) =
someothercolor.Acommonlogical
52
fallacysometimesreferredtoasthe
F(firstcardisafacecard)+F(firstcardisnotafacecard) = 1
“either-orfallacy”orthe“fallacy
oftheexcludedmiddle,”turnson
Example1.1 Whatisthefractionofthefirstcardasajackgiventhatwe
thispoint.Someexamplesofthese
knowthatthefirstcardisafacecard? fallaciesare:
• Ifwedon’treducepublicspend-
Wecanalsoapplythenegationruletoconditionalstatements,like ing,oureconomywillcollapse.
“thefirstcardisajackgiventhatweknowthatthefirstcardisaface • You’reeitherwithusoryou’rea
card.” Noticethatthereare12cardsthatarefacecards,sowerestrict terrorist.
• Eithermodernmedicinecan
ourcountstothose.
explainhowMs.Xwascured,or
4 itisamiracle.
F(jack facecard) = =1/3
| 12
8
F(notajack facecard) = =2/3
| 12
F(jack facecard)+F(notajack facecard) = 1
| |
andtheyadduptoone.
NegationRule Givenanyinformation,wehave NegationRule
P(AB)+P(notAB)=1
P(statement information)+P(notstatement information) =1 | |
| |
or
P(A B)+P(not A B) =1 (1.7)
| |

42 statistical inference for everyone
Product Rule
Theproductrulecomesfromlookingatthecombinationofevents:
eventAandeventB.Asbefore,we’llworkonthenumbersfromthe
fractionsofthecardgame.
Example1.2 WhatisthefractionofcardsthatareJacksandaheart?
Thisisclearly F(J♥) = 1/52,butwecanlookatitadifferentway
thatisequivalent. WenotethattheJacksconstitute4/52ofthecards,
andthatofthose4,onlyonequarterofthemarehearts(onecardout
ofthefourcards). So,wecanarriveatthefractionofJ♥bytaking
onequarterofthefractionofjacks. Sowhatwehaveis
1 4 1
F(jackand♥) = F(♥ jack) F(jack) = =
| × 4 × 52 52
Onecanequivalentlyreasonfromthesuitfirst: theheartsconstitute
13/52ofthecards,andthatofthose13,theJacksconstitute1/13
ofthecards. So,wecanarriveatthefractionofJ♥bytakingone
thirteenthofthefractionof♥. Again,wehave
1 13 1
F(jackand♥) = F(jack ♥) F(♥) = =
| × 13 × 52 52
Ingeneralwehave
ProductRule ProductRule
P(AandB) = P(AB)P(B)
P(A and B) = P(A B)P(B) = P(B A)P(A) (1.8) |
| | = P(B A)P(A)
|
Example1.3 WhatistheprobabilityofdrawingtwoKingsinarow?
Thisisthesameas
P(K and K )
2 1
Fromtheproductrule(Equation1.8)wehave
P(K and K ) = P(K K )P(K )
2 1 2 1 1
|
Thesecondpartisstraightforward: P(K ) = 4/52. Thefirstpartis
1
askingtheprobabilityofdrawingasecondking,knowingthatwe
havedrawnakingonthefirstdraw. Now,thereareonly51cards
remainingwhenwedotheseconddraw,andonly3kings. Thus,we
have P(K K ) =3/51andfinally
2 1
|
P(K and K ) = P(K K )P(K )
2 1 2 1 1
|
3 4 1
= =
51 × 52 221

introduction to probability 43
Independence
Asaspecificcaseoftheproductrule,wecanchangetheruleofthe
cardgamessuchthatwereshufflethedeckaftereachdraw. Inthis
way,theresultofonedrawgivesyounoinformationaboutother
draws. Inthiscase,theeventsareconsideredindependent.
IndependentEventsTwoevents,AandB,aresaidtobeinde- IndependentEventsTwoevents,
pendentifknowledgeofonegivesyounoinformationontheother. AandB,aresaidtobeindepen-
dentifknowledgeofonegives
Mathematically,thismeans
younoinformationontheother.
Mathematically,thismeans
P(A B) = P(A)
P(AB)=P(A)
| |
and
and
P(B A)=P(B)
|
P(B A) = P(B)
|
Inthiscase,theproductrulereducestothesimplifiedrulefor
independentevents: theproductoftheindividualeventprobabilities.
JointProbabilitiesforIndependentEvents JointProbabilitiesforIndependent
Events
P(A and B) = P(A) P(B) (1.9) P(AandB)=P(A) P(B)
× ×
Wehavealreadyseenanexampleofthis,whenwelookedat
drawingtheJackofHearts: drawingaheartgivesyounoinforma-
tionaboutwhetheritisajack,andviceversa. Thus,
P(♥ jack) = P(♥)
|
Example1.4 Whatistheprobabilityofflippingtwoheadsinarow?
Theprobabilityofgetting“heads”onanygivencoinflipis P(H) =
0.5. Theprobabilityofflippingtwoheadsinarowisthensimply
P(H ) P(H ) = 0.5 0.5 = 0.25,becausethesecondflipisin-
1 2
× ×
dependentofthefirst. Ifitwasn’t,thenyou’dhavetodetermine
howtheknowledgeofthefirstflipinfluencesourknowledgeofthe
secondflip,whichiswrittenas P(H H ) andthefullproductrule
2 1
|
(Equation1.8)wouldneedtobeused.
Conjunction
Oneoftheconsequencesofcombinationsofeventsisthattheprob-
abilityoftwoeventshappening,AandB,hastobelessthan(or
possiblyequalto)theprobabilityofjustoneofthem,sayA,happen-
ing. Themathematicalfactisseenbylookingatthemagnitudeofthe

44 statistical inference for everyone
termsintheproductrule
P(A and B) = P(B A) P(A) P(A)
| × ≤
(cid:124) (cid:123)(cid:122) (cid:125)
less
thanor
equalto
1
Inotherwords,coincidencesarelesslikelythaneithereventhap-
peningindividually. Weintuitivelyknowthis,whenwemakecom-
mentslike“Wow! Whatarethechancesofthat?” referringto,say,
someonewinningthelotteryandthengettingstruckbyacarthe
nextday. Sometimes,however,itseemsasifone’sintuitiondoesnot
matchtheconclusionsoftherulesofprobability. Onesuchcaseis
calledtheconjunctionfallacy. CombinationsofEventsandthe
Inaninterestingexperiment,TverskyandKahneman[Tverskyand EnglishlanguageIbelievethatthe
issueoftheconjunctionfallacyis
Kahneman,1983]gavethefollowingsurvey:
moresubtlethanthis.InEnglish,
ifIweretosay“Doyouwantsteak
Lindais31yearsold,single,outspoken,andverybright. Shemajored fordinner,orsteakandpotatoes?”
inphilosophy. Asastudent,shewasdeeplyconcernedwithissuesof onewouldimmediatelyparsethis
discriminationandsocialjustice,andalsoparticipatedinanti-nuclear aschoicebetween
demonstrations. 1 steakwithnopotatoes
2 steakwithpotatoes
Whichismoreprobable?
Althoughstrictlogicwouldparse
1 Lindaisabankteller. thischoiceas
2 Lindaisabanktellerandisactiveinthefeministmovement. 1 steak,possiblywithpotatoes
andpossiblywithoutpotatoes
85%choseoption2.[TverskyandKahneman,1974]This,theyat- 2 steak,definitelywithpotatoes,
tributed,totheconjunctionfallacy-mistakingtheconjunctionoftwo itiscommoninEnglishtohave
theimpliednegative(i.e.steak
eventsasmoreprobablethanasingleevent. Theywentfurtherand
withnopotatoes)whengiven
didasurveyofmedicalinternistswiththefollowing achoicewherethealternative
isaconjunction(i.e.steakwith
Whichismorelikely: thevictimofanembolism(clotinthelung)will potatoes).
experiencepartialparalysisorthatthevictimwillexperienceboth
partialparalysisandshortnessofbreath?
CombinationsofEventsandthe
andagain,91percentofthedoctorschosethattheclotwasless EnglishlanguageIfweinterpretthe
doctor’schoicewiththisimplied
likelytocausetherareparalysisratherthantocausethecombination
negative,wehave:
oftherareparalysisandthecommonshortnessofbreath. 1 clotwithparalysisandno
Evenwhencorrect,theconsequenceforconjunctionscanbemis- shortnessofbreath
used,oratleastmisidentified. Returningtoourexampleofsomeone 2 clotwithparalysisandshortness
ofbreath
winningthelotteryandthengettingstruckbyacarthenextday,rare
andthefirstoneismuchlesslikely,
eventsoccurfrequently,aslongasyouhaveenoughevents. Thereare
becauseitwouldbeoddtohavea
millionsofpeopleeachdayplayingthelottery,andmillionsgetting clotandnothaveaverycommon
struckbycarseachday. WewillexplorethisproblemlaterinSec- symptomassociatedwithit.The
doctor’sprobabilityassessmentis
tion2.5,butoneimmediateconsequenceisthatwinningthelottery
absolutelycorrect:bothsymptoms
andgettingstruckbyacarthenextdayprobablyhappenssomewhere togetheraremorelikelythanjust
one.The“fallacy”arisesbecause
fairlyregularly.
theEnglishlanguageissloppier
thanmathematicallanguage.

introduction to probability 45
Sum Rule
NowweconsiderthestatementsoftheformAorB.Forexample,
inthecardgame,whatisthefractionofcardsthatarejacksorare
hearts. Bycountingwegetthe13heartsand3morejacksthatarenot
containedinthe13hearts,or F(jackor♥) = 13+3 = 16/52. Now,if
52
wetriedtoseparatetheterms,anddo:
4 13 17
F(jack)+F(♥) = + =
52 52 52
thenwegetanumberthatistoobig! Itistoobigbecausewe’ve
double-countedthejackofhearts. Adjustingforthis,bysubtracting
onecopyofthisfraction,weget
4 13 1 16
F(jack)+F(♥) F(jackand♥) = + = = F(jackor♥)
− 52 52 − 52 52
Ingeneral
SumRule SumRule
P(A or B) = P(A)+P(B) P(A and B) (1.10) P(AorB)=P(A)+P(B) − P(AandB)
−
SumRuleforExclusiveEventsIftwoeventsaremutuallyexclusive SumRuleforExclusiveEventsIf
thesumrulereducesto twoeventsaremutuallyexclusivethe
sumrulereducesto
P(A or B) = P(A)+P(B) (1.11) P(AorB)=P(A)+P(B)
because P(A and B) =0forsuchevents. becauseP(AandB) = 0forsuch
events.
Sotheprobabilityofrollinga1ora2ononedieis2/6.
OnemorevariantontheSumRuleiswherewehave3propo-
sitions. Itcanbeabittedioustowriteitallout,buttheendresult
looksalotliketheoriginalSumRule. Allwedoisbreakupthe
termsinpieces,andthenapplytheSumRuletoeachpiece.
P(A or B orC) = P(A or [B orC])
= P(A)+P(B orC) P(A and [B orC])
−
= P(A)+P(B)+P(C) P(B andC)
− −
P(A and B or A andC)
= P(A)+P(B)+P(C) P(B andC)
− −
[P(A and B)+P(A andC)
−
P(A and B and A andC)]
whichleadsfinallyto
SumRuleforThreeEvents SumRuleforThreeEvents
P(A or B orC) = P(A)+P(B)+P(C)
P(AorBorC) = P(A)+P(B)+P(C)
−
− P(AandB)
P(A and B) P(B andC) P(A andC)+ −
− − P(BandC)
−
P(A and B andC) (1.12) P(AandC)+
P(AandBandC)

46 statistical inference for everyone
Inwords,whenyou’relookingforthesumofseveralevents,we
addtheprobabilities(i.e. P(A)+P(B)+P(C)),thensubtractthe
doublecounting(i.e. P(A and B))asbefore. Finally,weneedto
addbackinthetriplecount(i.e. P(A and B andC))becauseitwas
takenouttoomanytimeswiththedoublecount. Theaccounting
herecanbesomewhatpronetoerror,buttheconceptsarealwaysthe
same: whenyouaddprobabilitiesofevents,say A and B,together
theterm P(A) includestheprobabilityofboth P(A and B) andthe
term P(B) includestheprobabilityofboth P(A and B),soyou’ve
includedthatprobabilitytwiceandneedtosubtractoneofthemto
balancethebooks. Likewise(althoughitishardertoshow),thefirst
sixtermsinEquation1.12endupsubtractingonetoomanycopiesof
P(A and B andC),andweneedtoaddoneinattheend.
Marginalization
Anotherconsequenceofthesumruleandtheproductruleisapro-
cesscalledmarginalization.
Example1.5 MarginalizationandCardSuit
Imaginewehaveanumberofconditionalstatements,like:
1
P(jack ♥) =
| 13
1
P(jack ♦) =
| 13
1
P(jack ) =
|♠ 13
1
P(jack ) =
|♣ 13
butweareinterestedinjusttheprobabilityofdrawingajack,regard-
lessofthesuit,orinournotation
P(jack)
Themarginalizationprocedureforthisproblemlookslike:
allpossibilities
(cid:122) (cid:125)(cid:124) (cid:123)
P(jack) = P(jack ♥) P(♥)+
| ×
P(jack ♦) P(♦)+
| ×
P(jack ) P( )+
|♠ × ♠
P(jack ) P( )
|♣ × ♣
1 1 1 1 1 1 1 1
= + + +
13 × 4 13 × 4 13 × 4 13 × 4
4
=
52

introduction to probability 47
MarginalizationIfwehaveacompletesetofconditionalstate- MarginalizationIfwehaveacom-
ments,like pletesetofconditionalstatements,
like
P(A
|
B
1
) P(A
|
B
1
),P(A
|
B2 ),P(A
|
B3 ),P(A
|
B
4
),
···
P(A B ) thentheunconditionalprobability
2
| isfoundbymarginalizingoverall
P(A B 3 ) possiblevaluesoftheconditional
|
events,like
P(A B )
4
|
allpossibleBs
.
. . (cid:122) (cid:125)(cid:124) (cid:123)
P(A)=P(A
|
B
1
)P(B
1
)+P(A
|
B2 )P(B2 )+
···
thentheunconditionalprobabilityisfoundbymarginalizingoverall
possiblevaluesoftheconditionalevents,like
allpossible Bs
(cid:122) (cid:125)(cid:124) (cid:123)
P(A) = P(A B )P(B )+P(A B )P(B )+P(A B )P(B )+ (1.13)
1 1 2 2 3 3
| | | ···
Bayes’ Rule
Inthe1700’sReverendBayes
Oneofthemostconsequentialrulesofprobabilityiswhatisknown provedaspecialcaseofthisrule,
asBayes’Rule,sometimescalledBayes’Theorem. Wewillusethis andrediscoveredinthegeneral
formbyPierre-SimonLaplace.
rulethroughoutthisbook,andseeitsmanyapplications. Itcomesas
Laplacethenappliedtherulein
adirectresultoftheproductrule(Equation1.8) alargerangeofproblemsfrom
geology,astronomy,medicine,and
P(A and B) = P(A B)P(B) = P(B A)P(A) jurisprudence.
| |
Rearranging,weget
Bayes’Rule Bayes’Rule
P(A B) = P(B | A)P(A) (1.14) P(A | B)= P(B P | A (B )P ) (A)
| P(B)
Wecanverifythisagainwiththeintuitionswehaveinthesimple
cardgame.
Example1.6 Whatistheprobabilityofdrawingajack,knowingthat
you’vedrawnafacecard?
Intermsoffractions,thisshouldbe F(jack facecard) = 4/12 =
|
1/3. ApplyingBayes’Ruletothefractionsweget:
F(face jack) F(jack)
F(jack face) = | ×
| F(face)
4 4 4 1
= 4 × 52 = =
12 12 3
52
Althoughthiscalculationistrue,itisn’tparticularlyenlightening.
Itisnicertocasttheproblembackintoprobabilityterms,rather

48 statistical inference for everyone
thanfractions,andcomparetheprobabilityofdrawingajacktothe
probabilityofthesamething(i.e. drawingajack)giventhatweknow
thatwe’vedrawnafacecard. Thisis
1
P(jack) =
13
1
P(jack facecard) =
| 3
ThiscomparisonhighlightswhatBayes’Rulerepresents: learning. Alloflearningissimplyupdating
Whenyouareaskedwhattheprobabilityofdrawingajack,from onesbeliefsgiventhedata.The
datamaybewordsinabook,the
theknowledgeofthesimplecardgame,youcalculatethevalueof
resultsofanexperiment,aconver-
1/13. Onceyoulearnthatyoudrewafacecard,youupdateyour sationwithanotherperson,etc...
Thestrengthofourbeliefsarenot
knowledgetoincludethatinformation,andmodifyyourprobability
oftenthoughtofinmathematical
assignmentstoreflectthis. Thisleadstoanincreasedchanceofthe terms,butyouaredoingthemath
cardbeingajack. ofprobabilitieswheneveryouare
weighingthestrengthofyourbe-
Inanutshell,Bayes’Rulerepresentslearning:
liefs.Thus,theprobabilisticrule-
Bayes’rule-forupdatingbeliefs
InitialBelief+NewData ImprovedBelief givendataisreallythequantitative
→ specificationoflearning.Onecan
useitqualitativelyaswell,whichis
Itisusedinsciencetoinfercausesfromeffects,andcanthusbe
oftenusefulinfieldssuchashistory
written wherethedatadonottendtobe
quantitative.
P(effect cause) P(cause)
P(cause effect) = | ×
| P(effect)
Toinfertheprobabilityofaparticularcause,giventheeventsyou
observeintheworld,youfirsthavetoknowtheprobabilityofthe
causeitself(i.e. rarercauseswillreducethepriorprobability),and
howlikelythatthecauseyou’relookingatcouldhaveproduced
theeffectsyou’veobserved. Thesetwoitemsarethe P(cause) and
P(effect cause) terms,respectively. Theentirecalculationisscaled
|
by P(effect) whichisalloftheotherwaysthattheeffectscouldhavebeen
producedbyothercauses.. Thus,itisnotenoughtoshowthatgiving
aparticularmedicineisfollowedbythesymptomsdisappearingto
establishthatthemedicinewasthelikelycauseofthesymptoms
disappearing. Youhavetocalculatewhatotherpossiblecausescould
havehadthoseeffects,suchasthenormalfunctioningoftheimmune
systemortheplaceboeffect. Thisiswhycarefullycontrolledstudies
arenecessary,toeliminatealloftheotherpossiblecausesandto
determinethetruecauseoftheeffectsobserved.
WewillspendlargeportionsofseveralchaptersonBayes’Rule,to
exploreitslong-rangingconsequences.

introduction to probability 49
1.5 Venn Mnemonic for the Rules of Probability UNIVERSE UNIVERSE UNIVERSE
A and B
6
1
1/
A B A B
A
1/8 1/8
1/4 1/4
1/4
A or B
{
not A
Itisoftenusefultohaveapicturetorepresentthemathematics,so
thatitiseasiertoremembertheequationsandtounderstandtheir
meaning. ItiscommontousewhatiscalledaVennDiagramtorep-
resentprobabilitiesinanintuitive,graphicalway. Theideaisthat
probabilitiesarerepresentedasthefractionalareaofsimplegeomet-
ricshapes. Wecanthenfindapicturerepresentationofeachofthe
rulesofprobability. WestartbylookingatasampleVennDiagram,
inFigure1.2.
Figure1.2:Venndiagramofa
statement,A,inaUniverseofall
possiblestatements.Itiscustomary
tothinkoftheareaoftheUniverse
tobeequalto1sothatwecantreat
theactualareasasfractionalareas
representingtheprobabilityof
statementslikeP(A).Inthisimage,
Atakesup1/4oftheUniverse,so
thatP(A)=1/4.Alsoshownisthe
negationrule. P(A)+P(notA)=1
Wednesoday, Mray 28“, 14inside”ofA+“outside”ofA
addsuptoeverything.
UNIVERSE UNIVERSE UNIVERSE
A and B
6 1 1/
A B A B A
1/8 1/8
1/4 1/4
1/4
A or B
{
Thefractionalareaoftherectangle A representstheprobability
P(A),andcanbethoughtofasaprobabilityofoneofthestatements
we’veexplored,suchas P(♥). Thisdiagramisstrictlyamnemonic,
becausetheindividualpointsonthediagramarenotproperlyde-
fined. ThediagraminFigure1.2alsorepresentstheNegationRule
(Equation1.7),
P(A)+P(not A) =1
Inthediagramitiseasytoseethatthesumoftheareasinsideof
A (i.e. 1/4)andoutsideof A (i.e. 3/4)covertheentireareaofthe
Universeofstatements,andthusaddupto1.
not A
Figure1.3showsthediagramwhichcanhelpusrememberthe
sumandproductrules. TheSumRule(Equation1.10)
P(A or B) = P(A)+P(B) P(A and B)
−
isrepresentedinthetotalareaoccupiedbytherectangles A and B,
andmakesupallof A (i.e. 1/4)andthehalfof B stickingout(i.e.
1/8-1/16=1/16)yielding P(A or B) = 5/16. Thisisalsothearea
ofeachaddedup(1/4+1/8),butsubtractingtheintersection(1/16)
Figure1.3:Venndiagramofthe
becauseotherwiseitiscountedtwice. Addingtheareasthisway
sumandproduct.TherectangleB
directlyparallelstheSumRule. takesup1/8oftheUniverse,and
therectangleAtakesup1/4of
Conditionalprobabilities,likethosethatcomeintotheProduct
theUniverse.Theiroverlaphereis
Rule(Equation1.8)andBayesRule(Equation1.14)arealittlemore 1/16oftheUniverse,andrepresents
challengingtovisualize. InFigure1.4, P(A B) isrepresentedbythe P(AandB).Theirtotalareaof
| 5/16oftheUniverserepresents
fractionofthedarkerarea(whichwasoriginallypartof A)com-
P(AorB).
parednottotheUniversebuttotheareaof B,andthusrepresents
P(A B) = 1/2. Inaway,itisasiftheconditionalsymbol,“ ,”defines
| Wednesday, May 28, 14 |
theUniversewithwhichtomakethecomparisons. OntheleftofFig-
ure1.4,thesamedarkerareathatwasoriginallypartof B represents
P(B A) makingup1/4oftheareaof A. Thus P(B A) = 1/4. The
| |
ProductRule(Equation1.8)thenfollows,
1
P(A and B) = P(A B)P(B) = P(B A)P(A) =
| | 16
(cid:124) (cid:123)(cid:122) (cid:125)(cid:124)(cid:123)(cid:122)(cid:125) (cid:124) (cid:123)(cid:122) (cid:125)(cid:124)(cid:123)(cid:122)(cid:125)
1/2 1/8 1/4 1/4


[TABLE]


duction to probability 49
UNIVERSE UNIVERSE UNIVERSE
A and B
not A
6
1
1/
A B A B
A
1/8 1/8
1/4 1/4
1/4 {
A or B
Figure1.2:Venndiagramofa
statement,A,inaUniverseofall
possiblestatements.Itiscustomary
tothinkoftheareaoftheUniverse
tobeequalto1sothatwecantreat
theactualareasasfractionalareas
representingtheprobabilityof
statementslikeP(A).Inthisimage,
Atakesup1/4oftheUniverse,so
thatP(A)=1/4.Alsoshownisthe
negationrule. P(A)+P(notA)=1

thatP(A)=1/4.Alsoshownisthe
negationrule. P(A)+P(notA)=1
Wednesoday, Mray 28“, 14inside”ofA+“outside”ofA
addsuptoeverything. areasinsideof
ntireareaofthe
UNIVERSE UNIVERSE UNIVERSE
A and B
not A
srememberthe
6 1 1.10)
1/
A B A B A B)
1/8 1/8
1/4 1/4 ctangles A and B,
1/4 {
stickingout(i.e.
isalsothearea
A or B
ntersection(1/16)
Figure1.3:Venndiagramofthe
areasthisway
sumandproduct.TherectangleB
takesup1/8oftheUniverse,and
therectangleAtakesup1/4of
intotheProduct
theUniverse.Theiroverlaphereis
)arealittlemore 1/16oftheUniverse,andrepresents
epresentedbythe P(AandB).Theirtotalareaof
5/16oftheUniverserepresents
partof A)com-
P(AorB).
thusrepresents | thatP(A)=1/4.Alsoshownisthe
negationrule. P(A)+P(notA)=1





[TABLE]


6
1
1/
B | 1/8





[TABLE]


6
1
1/
B | 1/8




50 statistical inference for everyone
B A AB
Wecanfurtherseethespecialcaseofmutuallyexclusivestate- | |
mentsshowninFigure1.5. TheSumRuleforExclusiveEvents
(Equation1.11)issimplythesumofthetwoareasbecausethereis
A B
nooverlap
1/8
1/4
Figure1.4:Venndiagramofcon-
ditionalprobabilities,P(AB)and
|
P(B A).(Right)P(AB)isrepre-
| |
sentedbythefractionofthedarker
area(whichwasoriginallypartof
A)comparednottotheUniversebut
totheareaofB,andthusrepresents
P(AB) = 1/2.Inaway,itisasif
|
theconditionalsymbol,“,”defines
| theUniversewithwhichtomake
thecomparisons.(Left)Likewise,
thesamedarkerareathatwasorig-
inallypartofBrepresentsP(B A)
whichmakesup1/4oftheare | aof
A.ThusP(B A)=1/4.
Wednesday, May 28, 14 |
UNIVERSE UNIVERSE UNIVERSE A and B
6
1
1/
A B A B A
1/8 1/8
1/4 1/4
1/4
A or B
{
P(A or B) = P(A)+P(B)
Further,itisstraightforwardtoseefromthisdiagramthefollowing
propertiesformutuallyexclusiveevents
P(A and B) = 0
P(A B) = 0
|
P(B A) = 0
|
1.6 Lessons from Bayes’ Rule - A First Look
Bayes’Ruleisthegoldstandardforallstatisticalinference. Itisa
not A
mathematicaltheorem,provenfromfundamentalprinciples. Itstruc-
turesallinferenceinasystematicfashion. However,itcanbeused
withoutdoinganycalculations,asaguidetoqualitativeinference.
SomeofthelessonswhichareconsequencesofBayes’Rulearelisted
here,andwillbenotedthroughoutthistextinvariousexamples.
• Confidenceinaclaimshouldscalewiththeevidenceforthatclaim
• Ockham’srazor,whichisthephilosophicalideathatsimplerthe-
oriesarepreferred,isaconsequenceofBayes’Rulewhencompar- Figure1.5:Venndiagramofmu-
tuallyexclusivestatements.One
ingmodelsofdifferingcomplexity.
canseethatP(AandB) = 0
(theoverlapiszero)and
• Simplermeansfeweradjustableparameters P(AorB) = P(A)+P(B)(the
totalareaisjustthesumofthetwo
• Simpleralsomeansthatthepredictionsarebothspecificandnot areas)
overlyplastic. Forexample,ahypothesiswhichisconsistentwith
theobserveddata,andalsobeconsistentifthedataweretheop-
positewouldbeoverlyplastic.
Wednesday, May 28, 14
• Yourinferenceisonlyasgoodasthehypotheses(i.e. models)that
youconsider.
7
• Extraordinaryclaimsrequireextraordinaryevidence. 7CarlSagan. Demon-Haunted
World:ScienceasaCandleintheDark.
• Itisbettertoexplicitlydisplayyourassumptionsratherthanim- RandomHouseLLC,1996
plicitlyholdthem.
• Itisagoodthingtoupdateyourbeliefswhenyoureceivenew
information.
• Notalluncertaintiesarethesame.


[TABLE]


B A AB
| |
A B
1/8
1/4
Figure1.4:Venndiagramofcon-
ditionalprobabilities,P(AB)and
|
P(B A).(Right)P(AB)isrepre-
| |
sentedbythefractionofthedarker
area(whichwasoriginallypartof
A)comparednottotheUniversebut
totheareaofB,andthusrepresents
P(AB) = 1/2.Inaway,itisasif
|
theconditionalsymbol,“,”defines
|
theUniversewithwhichtomake
thecomparisons.(Left)Likewise,
thesamedarkerareathatwasorig-
inallypartofBrepresentsP(B A)
whichmakesup1/4oftheare | aof

thesamedarkerareathatwasor |
inallypartofBrepresentsP(B A
whichmakesup1/4oftheare | a
A.ThusP(B A)=1/4. es’ Rule - A First Look
Wednesday, May 28, 14 |
UNIVERSE UNIVERSE UNIVERSE A and B andardforallstatisticalinference. Itisa
not A
rovenfromfundamentalprinciples. Itstruc-
6 stematicfashion. However,itcanbeused
1
1/
ations,asaguidetoqualitativeinference.
A B A B A hareconsequencesofBayes’Rulearelisted
1/8 1/8 roughoutthistextinvariousexamples.
1/4 1/4
1/4 {
shouldscalewiththeevidenceforthatclaim
A or B isthephilosophicalideathatsimplerthe-
aconsequenceofBayes’Rulewhencompar- Figure1.5:Venndiagramofmu-
tuallyexclusivestatements.One
complexity.
canseethatP(AandB) = 0
(theoverlapiszero)and
djustableparameters P(AorB) = P(A)+P(B)(the
totalareaisjustthesumofthet
atthepredictionsarebothspecificandnot areas)
ple,ahypothesiswhichisconsistentwith
alsobeconsistentifthedataweretheop-
plastic. | thesamedarkerareathatwasor
inallypartofBrepresentsP(B A
whichmakesup1/4oftheare | a





[TABLE]


B | |
1/8





[TABLE]


sed6
1
1/
ce.
listBe
s. | d
1/8




introduction to probability 51
Thereisnotauniversalagreementforthetranslationofnumerical
probabilityvaluestoqualitativetermsinEnglish(i.e. highlyunlikely,
somewhatunlikely,etc...). OneroughguideisshowninTable1.1. I
willbefollowingthisconventionthroughoutthebook,butrealize
thatthespecificprobabilitydistinctionsareabitarbitrary.
term probability Table1.1:Roughguideforthe
conversionofqualitativelabelsto
virtuallyimpossible 1/1,000,000
probabilityvalues.
extremelyunlikely 0.01(i.e. 1/100)
veryunlikely 0.05(i.e. 1/20)
unlikely 0.2(i.e. 1/5)
slightlyunlikely 0.4(i.e. 2/5)
evenodds 0.5(i.e. 50-50)
slightlylikely 0.6(i.e. 3/5)
likely 0.8(i.e. 4/5)
verylikely 0.95(i.e. 19/20)
extremelylikely 0.99(i.e. 99/100)
virtuallycertain 999,999/1,000,000



2 Applications of Probability
Inthischapterwegothroughanumberofexamplesoftheusesof
probability,andpresentseveralusefulmathematicaltoolsalongthe
way.
2.1 Cancer and Probability
Thisisperhapsthemostimportantprobabilityquestiontolearn,so
wewillspendsometimecoveringithereandthencoveritagain,ina
slightlydifferentway,inSection5.1onpage109. Imaginewehavea
populationof10000peoplewhohavebeentestedforcancer,andwe
getthefollowinghypotheticaldata:
Numberof NegativeTest PositiveTest Total
Individuals
Doesn’tHave 9200 700 9900
Cancer
HasCancer 20 80 100
9220 780 10000
Wemaybeinterestedinanumberofrelatedprobabilities.
Example2.1 Whatistheprobabilityofbothhavingcancerandgettinga
positivetestforit?
Wecandeterminethisbysimplydividingthepersoncountsfrom
thetable
#ofpeoplewithbothcancerandpositivetest
P(cancerandpositivetest) =
total#ofpeople
80
= =0.008
10000
Doingthisprocessforeverypartofthetableyieldsaposterior
probabilitytable,givingtheprobabilityforeverycombinationof
variables(i.e. withcancerandpositivetest,withoutcancerandposi-
tivetest,etc...)


[TABLE]


Numberof
Individuals | NegativeTest | PositiveTest | Total

Doesn’tHave
Cancer | 9200 | 700 | 9900

HasCancer | 20 | 80 | 100

9220 | 780 | 10000




54 statistical inference for everyone
PosteriorProb- NegativeTest PositiveTest Total
ability
Doesn’tHave 0.92 0.07 0.99
Cancer
HasCancer 0.002 0.008 0.01
0.922 0.078 1.0
Example2.2 Whatistheprobabilityofbothnothavingcancerandgetting
apositivetestforit?
Readingoffofthetable,wehave
P(nocancerandpositivetest) = 0.07
Thisquestion,itturnsout,isanotveryinterestingquestion. The
typeofquestionthatactuallyarisesinlifeisthefollowing,
Example2.3 Whatistheprobabilityofhavingcancergivenapositivetest
forit?
Herewecanperformthecalculationinacoupleofdifferentways,
togivethe(unintuitive)result.
1 Countingtheindividuals.
#ofpeoplewithbothcancerandpositivetest
P(cancer positivetest) =
| #ofpeoplewithapositivetest
80
= =0.103
780
Althoughthosewithcancernearlyalwaystestpositive,outofthe
poolofallpeoplewhotestpositive-includingalargenumberof
false-positives-thoseactuallyhavingcancerareasmallminority.
Itisbecausetherearemanymorepeoplewithoutcancer,soeven
ifasmallfractionofthosemistakenlytestpositiveitwilloutweigh
thesmallfractionofthosepeoplewiththedisease. Thisiswhy
weinsistonsecondopinionsandwhytherarityofadiseaseoften
mattersevenmorethantheaccuracyofthetest.
2 ApplyingProductRule
UsingtheProductRule(Section1.4onpage42),wehave
P(positivetest) = P(nocancerandpositivetest)+P(cancerandpositivetest)
= =0.07+0.008=0.078


[TABLE]


PosteriorProb-
ability | NegativeTest | PositiveTest | Total

Doesn’tHave
Cancer | 0.92 | 0.07 | 0.99

HasCancer | 0.002 | 0.008 | 0.01

0.922 | 0.078 | 1.0




applications of probability 55
P(cancerandpositivetest)
P(cancer positivetest) =
| P(positivetest)
0.008
= =0.103
0.078
wherewehaveusedthesumofthePositiveTestcolumnfor P(positivetest).
Thisissimplyashortcuttothemarginalizationprocess(Section1.4
onpage46)-determinetheprobabilityofaneventbyaddingup
allofthepossibleconditionalsituations.
2.2 Weather
Example2.4 IftheprobabilitythatitwillrainnextSaturdayis0.25and
theprobabilitythatitwillrainnextSundayis0.25,whatistheprobability
thatitwillrainduringtheweekend?
First Solution - Independence
IfweassumethatSundayandSaturdayweatherareindependentthen
thesum-rule(Section1.4)applies:
P(rainSaturdayorrainSunday) =
P(rainSaturday)+P(rainSunday) P(rainSaturdayandrainSunday)
−
= P(rainSaturday)+P(rainSunday) P(rainSaturday) P(rainSunday)
− ×
= 0.25+0.25 0.25 0.25=0.4375 (2.1)
− ×
ThediagramsinFigure1.3areusefulinmakingthiscalculation
moreintuitive,especiallythetermwherewesubtract P(rainSaturday)
×
P(rainSunday) becauseotherwiseweovercountthedouble-rain
weekends. Anotherwaytothinkofthisterm
canbeseeninansweringadifferent
question-whatisthetotalnumber
Second Solution - Correlation ofweekendswithrain?.Imaginewe
have,inayear,40Saturdayswith
IsitreallyreasonablethatrainonSaturdayandSundayareindepen- rain(bysimplygoingthrough
alloftheSaturdaysandcounting
dentevents? Probablynot! It’sprobablythecasethatknowingthat
themifitrainsonthatday)andwe
itrainedonSaturday,thenrainonSundayismorelikely. Itmayalso alsohave40Sundayswithrain.If
bethatifitdidn’trainonSaturdaythenitwillbelesslikelyforrainon wewanttoknowthenumberof
weekendswithrainwecanadd
Sunday. Sowe’dhaveinformationpossiblylike:
theSaturdayswithrainandthe
Sundayswithrain(comingto80!)
P(rainSunday rainSaturday) = 0.35 anditbecomesclearthatwe’veover
|
countedthoseweekendswhereit
P(rainSunday notrainSaturday) = 0.15
| rainedbothdays-ayearcanonly
have52(orpossibly53)weekends.
Knowingthischangestheequationas
Weneedtosubtractthosedouble-
countstogetareasonableanswer.
P(rainSaturdayorrainSunday) = Thesamelogicappliestothe
calculationofprobabilities.
= P(rainSaturday)+P(rainSunday) P(rainSaturdayandrainSunday)
−

56 statistical inference for everyone
Notice,however,thatwedon’thaveadirectexpressionfor P(rainSunday)
anymore. Weonlyhavetheconditionalordependentforms,like P(rainSunday rainSaturday).
|
Wecanusethemarginalizationprocedure(Equation1.13onpage47),
andsumoveralloftheconditionalexpressions
P(rainSunday) = P(rainSunday rainSaturday)P(rainSaturday)+
|
P(rainSunday notrainSaturday)P(notrainSaturday)
|
= 0.35 0.25+0.15 (1 0.25) =0.2
× × −
andthenwehave
= P(rainSaturday)+P(rainSunday) P(rainSaturday) P(rainSunday rainSaturday)
− × |
= 0.25+0.2 0.25 0.35=0.3625 (2.2)
− ×
whichmakesitlesslikelytorainontheweekendiftheSundayrain
iscorrelatedwiththeSaturdayrain(Equation2.2)thaniftheyare
independent(Equation2.1). Whyisthat?
Onewaytothinkofitisthat,althoughtheprobabilityofrainon
SundayisincreasedduetorainonSaturday,itismorelikelythatSat-
urdayisnotrainy. Inthosecases,whicharemorefrequent,Sunday
islesslikelytoberainyaswell. Whenthetwodaysareindepen-
dent,Sunday’srainisthesameprobabilityregardlessofSaturday’s
weather. Whentheyaredependent,thenthemoreoftenclearSatur-
dayweathermakesitalittlelesslikelyfortheSundayrain,andthus
lowersthechanceofweekendrainbyalittlebit.
2.3 Adding Dice
Example2.5 Whatistheprobabilityofthesumoftwodicegettinga
particularvalue,say,7?
Allpossibleresultsfromrolling
Inthiscase,wesimplyoutlineeverysinglepossibility,andcount twodice:
sum (die1,die2)
thefractions. Inamorecomplexcasewemayneedtofindabetter 2 (1,1)
methodofcounting,buttheideawillbethesame.
3 (1,2),(2,1)
Wefindimmediatelythattheprobabilityofgettingasumof7 4
5
(
(
3
1
,
,
1
4
)
)
,
,
(
(
1
4
,
,
3
1
)
)
,
,
(
(
2
3
,
,
2
2
)
),(2,3)
isthelargest,becausetherearemorearrangementsofthetwodice 6 (1,5),(5,1),(4,2),(2,4),(3,3)
whichyieldasumof7thanforanyothersum. Eachprobability
7 (1,6),(6,1),(5,2),(2,5),(4,3),(3,4)
8 (3,5),(5,3),(6,2),(2,6),(4,4)
ofaparticularsumisjustthenumberofarrangementstogetthat 9 (5,4),(4,5),(3,6),(6,3)
particularsumdividedbythetotalnumberofarrangementsofatwo
10 (4,6),(6,4),(5,5)
dice(i.e. 36). 1 1 1 2 ( ( 6 6 , , 5 6 ) ) ,(5,6)
(36arrangmentstotal)

applications of probability 57
0.18
0.16
0.14
0.12
0.10
0.08
0.06
0.04
0.02
0.00
2 4 6 8 10 12
Sum of Two Dice
)eciD
owT
fo
muS(P
1 5
P(2) = =0.028 P(8) = =0.139
36 36
2 4
P(3) = =0.055 P(9) = =0.111
36 36
3 3
P(4) = =0.083 P(10) = =0.083
36 36
4 2
P(5) = =0.111 P(11) = =0.055
36 36
5 1
P(6) = =0.139 P(12) = =0.028
36 36
Example2.6 Whatistheprobabilityofrollingasummorethan7with
twodice?
Inournotationthisis
P(8or9or10or11or12)
whichareallexclusiveevents,soweusetheSumRuleforexclusive
events(Equation1.11)andobtain
P(8or9or10or11or12) = P(8)+P(9)+P(10)+P(11)+P(12)
= 0.139+0.111+0.083+0.055+0.028
= 0.416
Example2.7 Whatistheprobabilityofrollingvarioussumswithtwodice
eachwith20sides?
20-sideddicearecommoninsomekindsofgames,andprovidea
nicealternativetothestandard6-sidedvariety. Thefigurecomparing
the6-sidedand20-sideddicecanbeseeininFigure2.1onpage57.
0.18
0.16
0.14
0.12
0.10
0.08
0.06
0.04
0.02
0.00
2 4 6 8 10 12
Sum of Two Dice
)eciD
owT
fo
muS(P
0.05
0.04
0.03
0.02
0.01
0.00
5 10 15 20 25 30 35 40
Sum of Two 20-Sided-Dice
)eciD-dediS-02
owT
fo
muS(P
Figure2.1:Probabilityforrolling
varioussumsoftwodice.Shown
aretheresultsfortwo6-sideddice
(left)andtwo20-sideddice(right).
Thedashedlineisforclarity,but
representsthefactthatyoucan’t
rollafractionalsum,suchas2.5.


[TABLE]
























[TABLE]
























[TABLE]

















58 statistical inference for everyone
2.4 The Birthday Problem
1
Thisisafamousprobleminprobability ,whichweaddressherein 1
stages. Weintroduceasimpleversion,andmakeitmorecomplexin
stepsuntilwecantacklethegeneralproblem.
Two People on April 3
Example2.8 Let’simaginewehavethecasewheretwopeoplemeetonthe
street. WhatistheprobabilitythattheybothhaveApril3astheirbirthday?
Thiscanbesolvedwithastraightforwardapplicationoftheprod-
uctrule,Equation1.8onpage42.
A Person1hasabirthdayon,say,April3
≡
B Person2hasabirthdayon,say,April3
≡
P(A and B) = P(A B)P(B)
|
Eachofthesetermscanbecalculated. Firstly, P(A B) istheproba-
|
bilitythatperson1hasacertainbirthdaygiventhatperson2hasthe
samebirthday. However,knowingthebirthdayofthesecondperson
doesn’ttellusanythingaboutthebirthdayofthefirstperson,thus
theyareindependentand P(A B) = P(A).
|
Secondly,theprobabilityofhavinganyparticularbirthdayissim-
ply P(A) =1/365. Finally,wehave Thisisthesimplestassumption-
thateachdayisequallylikelytobe
A Person1hasabirthdayon,say,April3 bornon.However,thisisprobably
≡ nottrue-therearesomedaysthat
B Person2hasabirthdayon,say,April3 aremorelikelythanothers.In
≡
1 1 1 addition,onceyoustartincluding
P(A and B) = = =0.0000075 February29,thenthingsobviously
365 × 365 133,225
change.
whichisextremelyunlikely(seeTable1.1onpage51)!
Two People
Example2.9 Twopeoplemeetonthestreet,andweaskwhatistheproba-
bilitythattheybothhavethesamebirthday?
Howisthisdifferentthanthepreviousquestion,wherewespec-
ifiedwhichbirthdaytheyhad? Ourintuitionimmediatelysuggests
thatthisprobabilitymustbehigherthanthepreviousone,because
therearemorepossibilities-ratherthanApril3,theycouldbeborn
onJanuary1orMay3oranyotherday. Usingournotationwehave
thefollowingdefinitions: Inalloftheseexamplesweare
notconsideringleapdays,which
occurapproximatelyonceevery
fouryears.Theseextradaysdo
C Person1andPerson2bothhaveabirthdayonJanuary1
1 ≡ notchangeanyofthequalitative
results,andreallyonlyserveas
asmallextracorrectiontoany
analysis.However,itdoesaddafair
amountofbookkeepingwithvery
littleincreaseinenlightenment,so
wechoosetoavoidthisproblemin
ourexamples.

applications of probability 59
C Person1andPerson2bothhaveabirthdayonJanuary2
2
≡
.
.
.
C Person1andPerson2bothhaveabirthdayonDecember31
365
≡
andtheprobabilitywearelookingforis
P(C orC or orC )
1 2 365
···
Inthissituationwecannotethattheseareexclusivestatements.
Forexample,itcan’tbetruethatbothC andC aretrue-youcan’t
1 2
havemorethanonebirthday. Thus,theSumRule(Equation1.10on
page1.10)reducestotheLimitedSumRule(Equation1.11). Further,
eachterminthatruleisthesame
1 1
P(C ) = P(C ) = = P(C ) =
1 2 365
··· 365 × 365
sowehave
P(C orC or orC ) =
1 2 365
···
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
1 1 1 1 1 1
+ + +
365 × 365 365 × 365 ··· 365 × 365
(cid:124) (cid:123)(cid:122) (cid:125)
365terms,oneforeachday
1
= =0.0027
365
Anotherwaytothinkofthisistoimaginethatperson1randomly
“chooses”theirbirthday, D ,andperson2randomly“chooses”their
1
birthday, D ,andthentheycomparetoseeifthedaysarethesame,
2
or D = D . Ingeneral,wecanthinkoftheproblembrokenupin
1 2
thisway: Herewefindanotherexample
ofthegeneralrequirementthat
equivalentstatesofknowledge
P(D = D ) = giverisetoequivalentprobability
1 2 assignments.Inthiscaseitmeans
(cid:18) (cid:19) (cid:18) (cid:19)
D 1 isaspecificdayand numberofpossible thatifthereismorethanoneway
P
D isthesameday × specificdays toarriveataconclusion,theyeach
2
mustgivethesameanswer.We
Inthisway,weget canthenchoosethewaythatis
easiesttocalculate,simplyoutof
(cid:18) (cid:19)
1 1 convenience.
P(D = D ) = (365)
1 2
365 × 365 ×
1
= =0.0027
365
whichisextremelyunlikely(seeTable1.1onpage51),butnotnearly
asunlikelyasthembothhavingthesameApril3birthday.
Three People
Example2.10 Whatistheprobabilitythatthreerandompeoplehavethe
samebirthday?

60 statistical inference for everyone
Goingthroughthesamelogic,wehave
(cid:18) (cid:19)
1 1 1
P(D = D = D ) = 365
1 2 3
365 × 365 × 365 ×
1
= =0.0000075
133,225
whichisevenmoreextremelyunlikely(seeTable1.1onpage51)
thantheprevioustwo-personexample. Itisinterestingtonotethat
thisisthesameanswerwereceivedwhenweaskedfortheprobabil-
ityoftwopeoplewithaspecificbirthday. Onecanthinkofthethree
peoplehavingthesame,unspecified,birthdayinthefollowingwayif
ithelps. Thefirstperson’sbirthdayspecifiesthenecessarybirthday
fortheothertwo,soitisthesameasthecasewherewespecifya
singlebirthdayfortwopeople.
Two People...Out of Three
Usually,wedon’thaveasituationwherewehaverandompeople
meetingandallagreeingonbirthdays. Whatwehaveisagroupof
peopletalking,andtwopeopleinthegroupendupsaying“Hey,
mybirthdayisApril3too!” Thisisquiteabitdifferent,andleadsto
someunintuitiveconsequences. Let’sgothroughthesituationwith
threepeople,andweaskthequestion
Example2.11 Whatistheprobabilitythatatleasttwohavethesame
birthday?
Writingthepossibilitiesoutlike
Writingthisoutweget(somewhatmessily) thisisquitetedious,andcan
leadtoerrors.Directlyafterthis
calculationwefindanequivalent,
P(atleasttwooutofthreehavethesamebirthday) =
andmucheasier,wayofwriting
= P(exactly2thesameorexactly3thesame) thesamecalculation.However,itis
importanttonotethatallwaysof
= P(exactly2thesame)+ writingthesameinformationmust
leadtothesameanswer.
P(exactly3thesame) P(exactly2andexactly3thesame)
−
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
( 1 )3 365 0
365 ×
Theterm P(exactly2thesame) canbebrokenuplike
 
numberof
P(exactly2thesame) = P(aspecific2arethesame) possibilitiesof
×
2thesame
 
numberof
= P(D 1 = D 2 andnot D 1 = D 3 ) possibilitiesof
×
2thesame
Applyingtheproductruleweget I’msureyou’rewishingforthe
easierwayaboutnow...it’scoming
inExample2.12.

applications of probability 61
P(exactly2thesame) =
 
numberof
= P(D 1 = D 2 andnot D 1 = D 3 ) possibilitiesof
×
2thesame
 
numberof
= P(D 1 = D 2 not D 1 = D 3 )P(not D 1 = D 3 ) possibilitiesof
| ×
2thesame
 
numberof
= P(D 1 = D 2 )P(not D 1 = D 3 ) possibilitiesof
×
(cid:124) (cid:123)(cid:122) (cid:125)(cid:124) (cid:123)(cid:122) (cid:125) 2thesame
1 364
365 365
Notingthatthereare3waysofgettingaspecific2thesame,we These3waysare“person1and2
obtainforthissingleterm
match”,“person1and3match”,
“person2and3match.”
1 364
P(exactly2thesame) = 3
365 × 365 ×
Puttingitalltogetherwehave
P(atleasttwooutofthreehavethesamebirthday) =
= P(exactly2thesameorexactly3thesame)
(cid:18) (cid:19)3
1 364 1
= 3+ 365
365 × 365 × 365 ×
= 0.0082
Example2.12 Whatistheprobabilitythatatleasttwohavethesame
birthday? Aclevershortcut.
Acleverwayofrethinkingthisproblem,whichsignificantlyre-
ducesthecalculations,isfoundbyaskingthefollowingquestion: ina
groupofpeople,whatistheprobabilitythatnoneofthepeoplehave
thesamebirthday? Thiscanbeapproachedinastep-wisefashion.
Person1“chooses”abirthday,outof365theyhaveall365possibili-
ties. Person2“chooses”theirbirthday,withprobability P = 364/365
ofnotbeingthesameasPerson1. Person3nowhas363“choices”
outof365toavoidbothotherbirthdays,etc... Sotheprobabilityof
usingthisprocessandgettingtoPerson3andnothaveanyoverlap-
pingbirthdaysissimply
365 364 363
P(nonethesamein3people) =
365 × 365 × 365
Now,ifwe’reinterestedintheprobabilitythatatleasttwoarethe
same,thenthisistheexactoppositeoftheprobabilitythatnoneare
thesame. UsingtheNegationRule(Equation1.7onpage41)wehave
not“none 
(cid:18) (cid:19)
nonethesame
P in3people +Pthesamein3  = 1
people”

62 statistical inference for everyone
atleast2the 
(cid:18) (cid:19)
nonethesame
P in3people +Psamein3  = 1
people
whichleadsto
atleast2the 
(cid:18) (cid:19)
nonethesame
Psamein3  = 1 − P in3people
people
364 363
= 1
− 365 × 365
= 0.0082
Two People...Out of Thirty
Example2.13 Whenyouhaveagroupof30people,likestudentsina
classroom,andyouaskwhattheprobabilityoffindingtwointheroomwith
thesamebirthday,wouldyourintuitionsayitisgreaterorlessthan50%?
Manypeoplefindthattheirintuitionsuggestsreasonablystrongly
thatitwouldbelessthan50%. Wecannowdothisproblemquite
easily,andwefindthatourintuitiondoesnotmatch. Followingthe We’veoftenusedourintuitionto
sameprocedureaswith3people,weimagineeachperson“choos- verifytheresult,butnowwe’ve
reachedastatewheretheproblems
ing”theirbirthdaywithadwindlingselectionaswegoontoavoid
getsubtleenoughthatourintuition
“choosing”onethathasalreadybeentaken. Theprobabilitythatno fails.Itisgoodtouseones’intu-
itiononthe“easy”problems,but
oneintheroomhasthesamebirthdayasanyotheris
nowthatwe’veestablishedthepro-
cesswecantackleproblemswhere
ourintuitionisnotgoodenoughto
365 364 363 336
P(nonethesamein30people) = confirmaresult.
365 × 365 × 365 ×·× 365
(cid:124) (cid:123)(cid:122) (cid:125)
30terms
= 0.29
Sotheprobabilityofhavingatleast2peopleintheroomhaving
thesamebirthdayis
atleast2the 
Psamein30  = 1 0.29
−
people
= 0.71
whichis71%! Comparethislikelyoutcometotheextremelyrareout-
comeofhavingtworandompeoplehavingmatchedbirthdays,from
page58. SeeFigure2.2toseeaplotofthisunintuitiveobservation.
2.5 The Lottery Problem or Rare Things Are Common
Thisproblemisidenticaltothebirthdayproblemmathematically,with
theonlydifferencethattheprobabilitynumbersaremuchsmaller

applications of probability 63
1.0
0.8
0.6
0.4
0.2
0.0
0 10 20 30 40 50 60 70 80 90
Number of People
)yadhtrib
emas
htiw
2
tsael
ta(P
Figure2.2:Probabilityofhavingat
leasttwopeopleinagroupwith
thesamebirthdaydependingon
thenumberofpeopleinthegroup.
The50%markisexceededoncethe
50% mark
groupsizeexceeds23people.
reached at
23 people
andthenumberofparticipantsismuchlarger. Westartwithastory
2
aboutsomeonewinningthelotterytwiceinthesameday! 2
Canyouimaginewinningthelotterytwiceinoneday?
AngeloandMariaGallinadon’thavetoimagine-theyhittwiceon
Nov. 20.
ThemarriedcouplefromBelmont,Calif.,hadseparatelyboughttick-
etsintwodifferentCaliforniastatelotterygames,andbothcould
hardlybelievetheireyesasall11winningnumbersovertwogames
cameup....Beforetaxes,theirwinningsamountedto$126,000forthe
Fantasy5and$17millionfortheSuperLottoPlus,accordingtoThe
AssociatedPress....Orkinarrivedatthenumberbymultiplyingthe
roughly41-million-to-oneoddsofwinningtheSuperLottogameand
the575,000-to-oneoddsofwinningtheFantasy5gametoarriveat
oddsof23,575,000,000,000-to-one.
Prettyamazing! That’ssomethinglike
1
P(winningtwotickets) = 5 10− 14 (2.3)
2 1013 ∼ ·
·
whichtrulyisquiteimprobableasasingleevent,butisittrulyan
improbableeventtohappensomewhere? Theassumptionstatedin
thequoteisthatonlytwoticketswerepurchased. Weallknowthat
manylotteryticketsarepurchaseddaily,whichshouldincreasethe
chancethatsomewherethiswilloccur. Eventhiswinningcouplepur-
chasedticketseverydayfor20yearsbeforewinningthis.


[TABLE]


50% mark

reached at
23 people










64 statistical inference for everyone
Likethebirthdayproblem,youhavetosetuptheproblemin
thenegative,andaswhattheprobabilityofnoonewinningtwo
lotteries. Ifweassume5millionpeopleplayingdailyfor20years,
thisprobabilityis:
 (cid:12)5million 
(cid:12)
P   n w o in o n n i e ng (cid:12) (cid:12) (cid:12) playsdaily   = (cid:18) 1 1 (cid:19)5 · 106 × 365 × 20 (2.4)
 (cid:12)for20  − 2 1013
twotickets (cid:12) ·
(cid:12)years
(1 5 10− 14)5 · 106 × 365 × 20
∼ − ·
= 0.998 (2.5)
yieldinga0.2%chanceofthishappeningsometimeinthose20years
-stillprettyrare,butnotoutrageouslyso. Ifwefurtherimaginethat
thisisoccurringacrossthe50states,thisincreasesto10%chanceof
thishappeningsometimeinthose20years. Ifwefurtherimaginethat
thereareasmanyas5differentlotteries(thereareusuallymore)that
couldbeplayedperstate,thisjumpsupto40%.
Whatweseeasaninitiallyhighlyunlikelyeventstartstobecome
likelyandinfactcommonwhenconsideringallofthepossibleways
thateventcouldbeproduced.
2.6 Monty Hall Problem
OneofthemostpopularprobabilityproblemsiscalledtheMonty
Hallproblem,andisbasedonthetelevisiongameshow“Let’sMake
3
aDeal.” Itcantakeonmanyforms,butacommonformisasfol- 3
4
lows 4
Example2.14 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: behindonedoorisacar;behindtheothers,goats. Youpicka
door,sayNo. 1(butthedoorisnotopened),andthehost,whoknowswhat’s
behindthedoors,opensanotherdoor,sayNo. 3,whichhasagoat. Hethen
saystoyou,"DoyouwanttochangeyourchoicetodoorNo. 2?"Isitto
youradvantageordisadvantagetoswitchyourchoice,ordoesitmatter
whetheryouswitchyourchoiceornot?
Theresultisthatitisalwaysbettertoswitch,wheretheprobability
ofgettingthecarmovesupfrom1/3to2/3byswitching! Because
thisproblemisparticularlyunintuitive,wewillbreakitupinto
smallerpieces. Thecriticalaspectofthisisthatachangeinouras- Mostpeoplewillstatethat,because
signmentofprobabilitytoaneventmustbesomehowtiedtoachangeinour
weareleftwith2choices,itmust
be50-50.Howeverthereisadded
informationaboutthatevent. Inordertounderstandtheproblem,we
informationinthesystemwhich
mustthenunderstandwheretheextrainformationiscomingfrom. movesusfromknowingnothing
aboutthetwochoices(i.e.50-50
Wewillstepuptothefullproblemlisted,butfornowweexplore
chance)toknowingalittlebitmore
somesimplerversionsoftheproblem. aboutthetwochoices(i.e.not50-50
chance).

applications of probability 65
Two Doors with Information
Example2.15 Imaginewehaveagamewithtwodoors: Behindonedoor
isacar;behindtheotherisagoat. Youpickadoor,sayNo. 1(butthedoor
isnotopened),andthehost,whoknowswhat’sbehindthedoors,saysthat
thereisa90%chancethatthecarisbehinddoorNo. 2. Isittoyouradvan-
tagetoswitchyourchoice?
Initiallythereisatwo-doorchoice,withnoinformationaboutei-
therchoice,soweassignequalprobabilitiestothechoices: P(carbehindNo. 1) =
P(carbehindNo. 2) = 0.5(i.e. a50-50chance). Afterthehostgives
information,thischanges. Althoughthisisstillatwo-doorchoice,it
isnolongera50-50chance. Byhavingaknowledgablepersongive
youinformationsuddenlychangesthesituationtoa10-90chance,
anditismuchbetterforyoutoswitch.
Whatifthehostwerealittlelessdirect? Perhapssomethinglike
Example2.16 Thehost,whoknowswhat’sbehindthedoors,pointstoa
door,choosingthecorrectdoor90%ofthetimeandtheincorrectone10%.
Youpickadoor,sayNo. 1,andthehostpointstodoorNo. 2. Isittoyour
advantagetoswitchyourchoice?
Thisamountstoanidenticalsituationasthepreviousone-thehost
isgivingyoucorrectinformation90%ofthetime,andweareina
muchbetterpositionswitching.
Three Doors with Information
Wereturntothethree-doorcasewithaslightvariation
Example2.17 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: Behindonedoorisacar;behindtheothers,goats. Youpicka
door,sayNo. 1(butthedoorisnotopened),andthehost,whoknowswhat’s
behindthedoors,saysthatanotherdoor,sayNo. 3,hasa0%chanceof
havingacar,andthattheremainingdoor(thatyouhaven’tchosen-i.edoor
No. 2)hasa66%ofhavingthecar. Hethensaystoyou,"Doyouwantto
pickdoorNo. 2?"Isittoyouradvantagetoswitchyourchoice?
Inthiscase,switchingtodoorNo. 3wouldberidiculous-we
knowthecarisn’tthere,becausethe(honest)hostknowsthatitisnot
there. Thehostalsohastoldusthatthereisa66%chanceofthecar
behinddoorNo. 2,andthuswehave P(carbehindNo. 1) = 0.34
and P(carbehindNo. 2) = 0.66anditisbettertoswitchtodoorNo.
2.
Itisn’tthenumberofchoicesthatisimportant,itistheinforma-
tionwehaveaboutthosechoices. Whenyouhavenoinformation,we
assignequalprobabilities. Whenwehaveinformation,wecanassign
non-equalprobabilities.

66 statistical inference for everyone
Three Doors Down To Two
Backtoouroriginalproblem,wehave
Example2.18 Supposeyou’reonagameshow,andyou’regiventhechoice
ofthreedoors: behindonedoorisacar;behindtheothers,goats. Youpicka
door,sayNo. 1(butthedoorisnotopened),andthehost,whoknowswhat’s
behindthedoors,opensanotherdoor,sayNo. 3,whichhasagoat. Hethen
saystoyou,"DoyouwanttochangeyourchoicetodoorNo. 2?"Isitto
youradvantageordisadvantagetoswitchyourchoice,ordoesitmatter
whetheryouswitchyourchoiceornot?
Thekeypartisthat,nomatterwhathappens,
1 thehostneveropensyourdoor
2 thehostalwaysopensadoorwithagoat
Anotherwaytolookatthisisto
Giventhatyourfirstchoice,withthreeequalprobabilitychoices imagineagamewith1000doors,
carbehindonlyone,andthehost
(i.e. youhavenoinformationaboutanyofthechoices),weexpectto
hastoopenup998doors(notyours
becorrectonlyabout33%ofthetime. Ifwehappenedtogetlucky andnottheprize-iftheprizeis
withourfirstchoice,thenthehosthasapickoftwodoorswithgoats differentthanyours).Onceyou
pick,saydoornumber1,andthe
andhassomefreedom. Ifwehappenedtogetunluckywithourfirst
hostopenseverydoorexceptdoor
choice(andthereisagoatbehindit),thenthehosthasnofreedomat 576,andgivesyoutheopportunity
toswitchisitagoodchoice?Of
all,becausethereisonlyoneremainingdoorwithagoat. So,about
course!Onesintuitionrealizesthat
66%ofthetimethehostisforcedtorevealsomeofhisinformation, myinitial1/1000chanceofgetting
becausethedoorheleavesclosed(otherthanyourdoor)musthave itright(andthushavetheother
thecar. Thus,66%ofthetimethehostistellingyouwherethecaris, d th o e o 9 r 9 h 9 a / v 1 e 0 a 00 g c o h a a t) n i c s e s o w f a g m et p ti e n d g b i y t
justalittleindirectly. wrong,andthehostbeingforcedto
openeverydoorwithouttheprize.
Formally,weneedtoinvolvemodelcomparison,sowepostpone
thisparticularanalysisuntilSection5.4.
2.7 Exercises
Exercise2.1 Whatistheprobabilitythatatleast3peoplehavethesame
birthdayinagroupof50?
Exercise2.2 ExaminethecaseofMontyHallwith4doors,thehostopen-
ingonedoorwithagoat,andleavingyouwithachoiceof3. Shouldyou
switch? Doesitmatterwhichoftheothertwoyouchoose?
Exercise2.3 Whatistheprobabilityofrollingvarioussumsfromtwo
9-sideddice?
Exercise2.4 Whatistheprobabilityofrollinganoddsumwithtwodice?
Exercise2.5 Whatistheprobabilityofrollingmorethan7fromtwo20-
sideddice?

applications of probability 67
Exercise2.6 Giventhetableabove,determinethefollowingquantities,and
describewhattheymean:
1 P(cancerandnegativetest)
2 P(cancer negativetest)
|
3 P(notcancer)
4 P(notcancer)+P(cancer)
2.8 Some Philosophical Applications
Doctors’ Claims - English Language and Probability
InSection1.4weintroducedworkbyTverskyandKahnemandoc-
umentingsupposedfailuresinproperreasoning. Intheexample
surveyofmedicalinternists,theinternistswereasked
Whichismorelikely: thevictimofanembolism(clotinthelung)will
experiencepartialparalysisorthatthevictimwillexperienceboth
partialparalysisandshortnessofbreath?
and91percentofthedoctorschosethattheclotwaslesslikelyto
causetherareparalysisratherthantocausethecombinationofthe
rareparalysisandthecommonshortnessofbreath.
Thismaynotbeafailureofreasoning,buta(correct!) failureof
thedoctorstotranslatetheEnglishlanguageliterallyintological
language. Itislikelythatwhendoctorsareasked: “Whichismore
likely: thatthevictimofanembolismwillexperiencepartialparal-
ysisorthatthevictimwillexperiencebothpartialparalysisand
shortnessofbreath?” theyinterpretitas:
1 someoneisclaimingthatthepatienthasanembolism
2 thepatientisclaiming,orsomeonehasmeasured,thatshehas
partialparalysis
3 thepatientisclaiming,orsomeonehasmeasured,thatshehas
shortnessofbreath
Thedoctorsareseparatingtheanalysisoftheclaimoftheclot,
whichisgiveninformation,fromtheotherclaims. Anotherwayof
lookingatitistoincludetheknowledgeofthemethodofreporting.
Someonewhoisreportinginformationaboutanailmentwilltendto
reportalloftheinformationaccessibletothem. Byreportingonlythe
paralysis,therearetwopossibilitiesconcerningthepersonmeasuring
thesymptomsofthepatient:

68 statistical inference for everyone
1 theyhadthemeanstomeasureshortnessbreathinthepatient,but
therewasnone
2 theydidnothavethemeanstomeasureshortnessofbreath
Inthefirstcase,thedoctor’sprobabilityassessmentisabsolutely
correct: bothsymptomstogetheraremorelikelythanjustone. Inthe
secondcase,thedoctorsarealsocorrect: oneofthesetsofdiagnostic
results(i.e. justparalysis)islessdependablethantheotherset(i.e.
bothsymptoms),thusthesecondoneismorelikelytoindicateaclot
orisconsistentwiththeknownclot.
Itisn’tthatthedoctorsarereasoningincorrectly. Theyareinclud-
ingmoreinformation,anddoingamoresophisticatedinferencethan
thestrict,formal,minimalisticinterpretationofthestatementswould
leadonetodo. Thisanalysisworkswellforotherexamplesstatedin
thebookADrunkard’sWalkbyMlodinow[?],like“Isitmoreprobable
thatthepresidentwillincreasefederalaidtoeducationorthathe
orshewillincreasefederalaidtoeducationwithfundingfreedby
cuttingotheraidtostates?”
Allofthisunderscorestheneedtobecarefultranslatingstate-
mentsofprobabilityintoplainEnglishandviceversa.
Diverging Opinions
Isitpossibletohavepeopleinformedbythesameinformation,and
reasoningproperly,tohavedivergingopinions? Itmightseemin-
tuitivethatpeoplegiventhesameinformation,reasoningproperly,
wouldtendtocometoagreement,howeverthisisnotalwaysthe
case. Whatisinterestingisthatitturnsonthepriorprobabilitiesfor
claims.
ThisexamplecomesfromJaynes,20035
. Wehavethefollow- 5E.T.Jaynes. ProbabilityTheory:
ingpieceofinformation: TheLogicofScience. Cambridge
UniversityPress,Cambridge,2003.
EditedbyG.LarryBretthorst
(cid:26)
“Mr N. hasgoneonTVwithasensationalclaim
D :=
thatacommonlyuseddrugisunsafe”
andwehaveobservers A, B,andC withdifferentpriorassignments
tothereliabilityofMr N andofthesafetyofthedrug. Theseprior
assignmentsmayhavebeentheresultofpreviousinferencebythese
observers,inadifferentcontext,orpossiblyduetoexpertknowledge.
Observers A andC believe,beforetheannouncement,thatthedrug
isreasonablysafe. Observer B doesnot. Wehavetheprobability
assignmentsthen:
P (Safe) = 0.9
A
P (Safe) = 0.1
B
P (Safe) = 0.9
C

applications of probability 69
Theyallagreethatifthedrugisnotsafe,thenMr N wouldan-
nounceit,sowehave
P (D notSafe) = 1
A
|
P (D notSafe) = 1
B
|
P (D notSafe) = 1
C
|
Finally,wehavetheperceptionsfromtheobserversaboutthereli-
abilityofMr N ifthedrugisactuallysafe. Inthiscase,observer A is
trustingofMr N,observerC isstronglydistrustful,andobserver B is
mildlydistrustful. By“distrustful”wearereferringtotheprobabili-
tiesthatMr N wouldmaketheannouncementthatthedrugisunsafe
evenif thedrugwereactuallysafe. Sowehave
P (D Safe) = 0.01
A
|
P (D Safe) = 0.3
B
|
P (D Safe) = 0.99
C
|
Wewanttoknowhoweachobserverthendetermineswhetherthe
drugissafe,giventheannouncement,or P(Safe D) foreachobserver.
|
ApplyingBayes’Rulewehave
P (D Safe)P (Safe)
P (Safe D) = A | A
A | P (D Safe)P (Safe)+P (D notSafe)P (notSafe)
A A A A
| |
0.01 0.9
= · =0.083
0.01 0.9+1 0.1
· ·
Followingthesamecalculationfortheothers,wegettheobservers
updatingtheirprobabilityassignmentsaftertheannouncement, D,as
P (Safe) =0.9 P (Safe D) =0.083
A A
→ |
P (Safe) =0.1 P (Safe D) =0.032
B B
→ |
P (Safe) =0.9 P (Safe D) =0.899
C C
→ |
Observer A changedtheirmind,Observer B hadtheirassessment
confirmedabit,andObserverC barelybudged.
Althoughyou’dthinkthathearingtheannouncementoftheun-
safenatureofthedrugwouldhavemovedalloftheprobabilitiesby
thesameamount,buttheinformationisn’tthatthedrugisunsafe,
butthesomeoneisclaimingthatthedrugisunsafe. Thus,onesprior
informationaboutboththedrugandwhoismakingtheclaimcomes
intoplay.
A problem of independence
AssaidinthebeginningofChapter1(IntroductiontoProbability),
in1968ajuryfounddefendantMalcolmRicardoCollinsandhiswife

70 statistical inference for everyone
defendantJanetLouiseCollinsguiltyofseconddegreerobbery. The
prosecutorfocussedonthethedistinctivefeaturesofthedependence,
6
andassignedaprobabilitytoeachasfollows : 6J.Sullivan. Peoplev.Collins,
68cal.2d319,1968. URLhttp:
1 Partlyyellowautomobile1/10
//scocal.stanford.edu/opinion/
people-v-collins-22583
2 Manwithmustache1/4
3 Girlwithponytail1/10
4 Girlwithblondhair1/3
5 Negromanwithbeard1/10
6 Interracialcoupleincar1/1000
Hethenfollowedwiththecalculationapplyingtheproductrulefor
independentevents(Section1.4onpage43),tofindtheprobability
thatallthesethingscouldhavebeenobserved:
1 1 1 1 1 1 1
=
10 × 4 × 10 × 3 × 10 × 1000 12,000,000
Theinitialconvictionwasoverturnedfortwoprimaryreasons,
onelegalandonemathematical. Thelegalargumentwasthatthe
prosecutionhadnotestablishedthattheseinitialprobabilitieswere
supportedbytheevidence. However,thereallydevastatingpartof
theargumentwasmathematical. Asyoumayrecall,theproductrule
usedinthiswayassumestheindependenceoftheterms(Section1.4on
pageSection43).
Example2.19 BeardandMustache-AnExaminationofIndependence
Foranexample,theproperproductrulefortwooftheterms
abovewouldlooklike:
P(ManwithbeardandManwithmustache) =
P(Manwithmustache Manwithbeard)P(Manwithbeard)
|
Whattheprosecutorwasassumingisthatthesetwoitemswere
independent,fromwhichitwouldfollowthat
P(ManwithbeardandManwithmustache) =
1
P(Manwithmustache)P(Manwithbeard) = =0.025
40
However,withaverybriefthought,wenoticethatthisisequiva-
lenttosaying
Knowingthemanhasabeardtellsusnothingabouttheprobabilityof
himhavingamustache!

applications of probability 71
Clearly,itisnotnearlyascommontohaveabeardwithnomus-
tachethanwithone,soknowingthatthemanhadabeardwould
nearlycertainlyimplythathehadamustacheor,
P(ManwithbeardandManwithmustache) =
1
P(Manwithmustache Manwithbeard)P(Manwithbeard)
| ∼ 10
(cid:124) (cid:123)(cid:122) (cid:125)
1
∼
andtheprobabilitycalculated,justfromthesetwoterms,ismuch
higherthantheprosecutorwascommunicating.
Similarsortsofabsurditiesoccurwithotherterms,like“blond
hair”and“ponytail”,aswellasothers. Finally,evenifitwasthe
casethatthisisasomewhatrarecombination,giventhenumberof
peopleinLosAngeles,onemightbeabletocalculatetheprobability
thatthereisatleastonemorecouplesatisfyingthesecharacteristics.
Justlikethelotteryproblem(Section2.5onpage62),itbecomes
likelythattherearemorecouplesinthearealikethis,andthusthe
rulingwasoverturned.
Another problem with independence
AnotherproblembroughtupintheopeningofChapter1(Intro-
ductiontoProbability)isthecaseofSallyClark. SallyClarkwas
convictedin1999ofthemurderofhertwoyoungsons 7 . Inthecase, 7LordJusticeKay. RvsSally
thestatisticalargumentwas Clark,April2003. URLhttp:
//www.bailii.org/ew/cases/EWCA/
ProfessorMeadowwasaskedifafigureof1in8,543reflectedtherisk
Crim/2003/1020.html
oftherebeingasingleSIDSwithinsuchafamily. Heagreedthatit
was. AtablefromtheCESDIreportwasplacedbeforethejury. Hewas
thenaskedifthereportcalculatedtheriskoftwoinfantsdyingofSIDS
inthatfamilybychance. Hisreplywas: ‘‘Yes,youhavetomultiply1in
8,543times1in8,543andIthinkitgivesthatinthepenultimateparagraph.
Itpointsoutthatit’sapproximatelyachanceof1in73million.”
Whathewasdoingwasequatingthefollowingintheproductrule
(Section1.4onpage1.4):
P(secondchilddyingofSIDS firstchilddyingofSIDS) = P(secondchilddyingofSIDS)
|
whichisequivalenttosaying
Knowingthatthechilddiesofa[notwellunderstood]diseasetellsus
nothingabouttheprobabilityofthesecondchilddyingofthesame[not
wellunderstood]disease.
Clearlythisisridiculous,becauseifthereisacommonsourceto
thedisease,theonedeathcertainlyincreasestheprobabilityofthe
second. Suchacommonsourcecouldbesomethingsharedinthe
environmentalorperhapsageneticdispositioninthefamilyforthe
disease.

72 statistical inference for everyone
Prosecutor’s Fallacy
Bothofthecasesaboveareexamplesofwhatiscalledtheprosecu-
tor’sfallacy. Itoccurswhensomeoneassumesthatthepriorprob-
abilityofaneventisequaltotheprobabilitythatthedefendantis
innocent. Asimpleexampleisthat“ifaperpetratorisknowntohave
thesamebloodtypeasadefendantand10%ofthepopulationshare
thatbloodtype;thentoargueonthatbasisalonethattheprobability
ofthedefendantbeingguiltyis90%makestheprosecutors’sfallacy,
8
inaverysimpleform.” 8
Essentiallytheprosecutorisignoringthenumberofpeoplewho
matchtherareevent. Also,althoughdouble-deathsbySIDSarerare,
theyaremuchmorecommonthandouble-murders! Onereallyhasto
lookat
P(innocence evidence)
|
whichisnotthesameas
P(evidence)
2.9 Computer Examples
Coin Flips
from sie import *
Generateasmalllistofdata...
data=randint(2,size=10)
print data
[1 0 0 1 0 0 0 1 0 0]
Generateaslightlylargerlistofdata...
data=randint(2,size=30)
print data
[1 1 1 0 0 0 0 1 1 1 1 0 1 1 0 1 1 0 0 1 1 1 0 1 0 0 1 1 0 0]
data=randint(2,size=(2000,10))
data
array([[1, 0, 1, ..., 1, 0, 0],
[1, 1, 1, ..., 0, 1, 0],
[0, 0, 1, ..., 0, 0, 0],
...,
[0, 0, 0, ..., 1, 1, 0],


[TABLE]




from sie import *







[TABLE]




data=randint(2,size=10)

print data







[TABLE]




data=randint(2,size=30)

print data







[TABLE]




data=randint(2,size=(2000,10))

data






applications of probability 73
[0, 1, 0, ..., 0, 1, 1],
[0, 1, 1, ..., 1, 0, 1]])
Wehaveherealargecollectionofnumbers(20000ofthem!),organizedin2000rowsof10columns.
Wecansumallofthe20000values,orwecansumacrosscolumnsoracrossrows,dependingonwhat
wewant.
sum(data) # add up all of the 1’s
9988
sum(data , axis=0) # sum up all of the columns
array([1011, 1010, 1001, 1051, 1001, 1008, 962, 990, 976, 978])
sum(data , axis=1) # sum up all of the rows
array([3, 7, 3, ..., 5, 4, 6])
Typicallythehistcommandmakesitsownbins,whichmaynotcenterontheactualcountvalues.
That’swhywecallcountbins(N),tomakebinscenteredonthecounts.
N=sum(data , axis=1) # number of heads in each of many flips
hist(N,countbins(10))
xlabel( ’Number of Heads’)
ylabel( ’Number of Flips ’)
<matplotlib.text.Text at 0x10856e990>
Togetaprobabilitydistribution,wedividethehistogramresultby N.
ThisdistributionisBernoulli’sequation,orinotherwords,thebinomialdistribution.
(cid:18) (cid:19)
10
p(h,10) = 0.5h 0.510
−
h
h ·


[TABLE]




sum(data) # add up all of the 1’s







[TABLE]




sum(data , axis=0) # sum up all of the columns







[TABLE]




sum(data , axis=1) # sum up all of the rows







[TABLE]




N=sum(data , axis=1) # number of heads in each of many flips

hist(N,countbins(10))

xlabel( ’Number of Heads’)

ylabel( ’Number of Flips ’)






74 statistical inference for everyone
h=array([0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10])
# or ...
h=arange(0,11)
(recallthat**isexponentiationinPython,becausethecaret(ˆ)wasalreadyusedforacomputer-
sciencyrole.) Thespacesintheequationbelowarenotneeded,buthighlightthethreepartsofthe
binomialdistribution.
p=nchoosek(10,h)* 0.5 **h * 0.5 **(10 h)
−
hist(N,countbins(10) ,normed=True)
plot(h,p, ’ o’)
−−
xlabel( ’Number of Heads, $h$’)
ylabel( ’$p(h|N=10)$’)
<matplotlib.text.Text at 0x108560290>
Exercise2.7 Youflipacoinfivetimes...
1 Whatistheprobabilityofflipping0,1,2,3,4,and5headseachinthese
5flips?
2 Showinasimulationthatthismatchestheseprobabilitiesyoujustfound.


[TABLE]




h=array([0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10])



# or ...



h=arange(0,11)







[TABLE]




p=nchoosek(10,h)* 0.5 **h * 0.5 **(10 h)

−





[TABLE]




hist(N,countbins(10) ,normed=True)

plot(h,p, ’ o’)

−−
xlabel( ’Number of Heads, $h$’)

ylabel( ’$p(h|N=10)$’)






3 Random Sequences and Visualization
Nowthatweunderstandtherulesofprobability,andhowtheyare
appliedinanumberofpracticalexamples,weexploretheuseof
theserulestosequencesofrandomevents. Thiswillproduceseveral
interestingandunintuitiveobservations,failuresofinference,and
theproperwaystohandlethem. Finally,weexaminehowvisual-
izebothdataingeneralandwhatwecancommunicatewithsuch
visualization.
3.1 Coin Flipping
We’llstartwithsomesimpleexamplesofcoinflipping,askingsome
simplequestions,andmovetomorecomplexobservationsandunin-
tuitiveconclusions.
Example3.1 Whatistheprobabilityofflippingthreeheadsinarow,with
afaircoin?
Wecanapproachthisproblemintwodifferentways. Thefirstway,
isabrute-forcecountingmethodwiththedefinitionofprobabilityfor
exclusiveevents(usingEquation1.2)andthesecondwaymakesuse
oftheotherrulesofprobability. Inthefirstway,wesimplyoutline Allpossibleresultsfromthreecoin
everypossiblecombinationofthreeflips,seehowmanyare“three flips:
1 TTT
headsinarow”,asweshowinthemargin. 2 TTH
Becausethereisonlyonecaseof“HHH”inalleight,theproba- 3 THT
4 THH
bilityofthreeheadsinarowis
5 HTT
6 HTH
P(threeheadsinarow) =1/8 7 HHT
8 HHH
whichisanunlikelyoutcome,butnotextremelyso(seeTable1.1on
page51).
Intermsoftheruleofprobability,wehave
P(threeheadsinarow) = P(H and H and H )
1 2 3
where H isheadsonthefirstflip, H isheadsonthesecondflip,
1 2
etc... Becausetheseareindependentevents(Section1.4),theprobabil-
ityisjusttheproductoftheprobabilitiesoftheindividualevents

76 statistical inference for everyone
(Equation1.9)
P(threeheadsinarow) = P(H and H and H )
1 2 3
= P(H ) P(H ) P(H )
1 2 3
× ×
1 1 1
=
2 × 2 × 2
1
=
8
thesameanswerasbefore. Yetagain,weseethatifthere
aremultiplewaysofarrivingat
Example3.2 Whatistheprobabilityofflippingthirtyheadsinarow,with ananswer,thatitmustyieldthe
afaircoin? sameanswer-equivalentstates
ofknowledgeyieldequivalent
probabilityassignments.
Ourintuitionwillclearlyinsistthatthiswillbeaverysmallnum-
ber,buthowsmall? Ourfirstmethod,oflistingallofthepossibilities
getsquiteabitcumbersomewiththisquestion. Thesecondmethod
isquitestraightforward
P(thirtyheadsinarow) = P(H and H and and H )
1 2 30
···
= P(H ) P(H ) P(H )
1 2 30
× ×···×
30times
(cid:122) (cid:125)(cid:124) (cid:123)
1 1 1
=
2 × 2 ×···× 2
(cid:18) (cid:19)30
1
=
2
= 0.000000001(oneinabillion!)
Thisisvirtuallyimpossible(Table1.1).
Example3.3 Whatistheprobabilityofflippingtwoheadsinthreeflips,
withafaircoin?
Ourintuitionsuggeststhatthisshouldbeareasonablycommon
occurrence. Weaddressthisprobleminexactlythesametwoways:
first,bycounting,thesecondwiththerulesofprobability. Inthe
firstmethod,weobservefromthetablethattherearethreewaysof
gettingtwoheads: “THH,”“HTH,”and“HHT.”Thus,
3
P(twoheadsinthreeflips) =
8
Inthesecondmethodwewrite
P(twoheadsinthreeflips) =
P((T and H and H ) or (H and T and H ) or (H and H and T ))
1 2 3 1 2 3 1 2 3
fromwhichwecanapplythesumruleforexclusiveevents(Equa-
tion1.11)and,likebefore,theproductruleforindependentevents
(Equation1.9),

random sequences and visualization 77
P(twoheadsinthreeflips) =
P(T and H and H )+P(H and T and H )+P(H and H and T )
1 2 3 1 2 3 1 2 3
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
1 1 1 1 1 1 1 1 1
= + +
2 × 2 × 2 2 × 2 × 2 2 × 2 × 2
1 1 1 3
= + + =
8 8 8 8
whichisabouta38%chance,slightlyunlikely(Table1.1).
Example3.4 Whatistheprobabilityofflippingtenheadsinthirtyflips,
withafaircoin?
Oncethenumbersstartgettinglarge,ourintuitionfails,andwe
can’tlistallthepossibilities. Inordertoproceed,weneedtodevelop
asystematicwayofapproachingthesesortsofproblems. Essentially
itcomesdowntotwoparts:
1 Whatistheprobabilityofoneparticularsequencebeingconsidered?
2 Howmanywayscanthistypeofsequenceappearintheprocess
describedinthequestion?
Point1isasking,whatistheprobabilityofthisparticularse-
quence:
HHHHHHHHHHTTTTTTTTTTTTTTTTTTTT
orthissequence:
TTHTTTTHHHHTTTTTHTTHTTTTTTHHTH
Althoughitisunintuitive,mathematicallybothofthesespecificse-
quenceshaveexactlythesameprobability: eachheadortailhasequal
probability,isnotrelatedtotheothers,andtherearethesamenum-
berofthem. Sowehave
P(HHHHHHHHHHTTTTTTTTTTTTTTTTTTTT) =
P(TTHTTTTHHHHTTTTTHTTHTTTTTTHHTH)
(cid:18) (cid:19)30
1
=
2
= 0.000000001(oneinabillion!)
Everysinglespecificlength-thirtysequenceofheadsandtailshasthe
sameprobability,oneinabillion.
Point2isasking,howmanysequencesarethereofthirtyheads
andtailswheretenofthemareheads? Anotherwayofphrasingitis,
givenasequencelike:
HHHHHHHHHHTTTTTTTTTTTTTTTTTTTT
howmanydifferentwayscanIrearrangethissequenceandgeta
uniquesequence?

78 statistical inference for everyone
Counting the Rearrangements
Wearegoingtodeterminetheanswertoourquestioninsmallsteps. Symbols:ABCD
First,weask, Boxes:
Example3.5 HowmanywayscanwerearrangetheuniquesymbolsA,B, Choices RemainingSymbols
A BCD
C,andD?
B ACD
C ABD
Tomakethisintuitive,wesetupfouremptyboxesandweimagine
D ABC
placingoursymbolsintheboxes,oneatatime. Howmanychoices
dowehave? Forthefirstbox,wehavefourchoices. Foreachofthese
choices,we’veremovedoneofthesymbols,andoneoftheboxes.
Choices RemainingSymbols
Thus,weareleftwiththreeremainingsymbolsforeachchoice,and
AB CD
threeremainingboxes. Foreachoftheoriginalfourchoices,wenow
AC BD
havethreechoicesforthesecondbox. Thisimmediatelyleadsto AD BC
4 3=12possibilitiesbythetimewe’vefilledtwoboxes. Foreachof
× BA CD
thesetwelvepossibilities,therearetwosymbolsremainingandtwo BC AD
boxes. Continuingthislogic,wehavetwochoicesforthethirdbox, BD AC
andthenonlyonechoiceforthefinalbox. Insummary,foreachof
CA BD
thefourchoicesforthefirstboxwehavethreechoicesforthesecond, CB AD
CD AB
twochoicesforthethird,andoneforthefinalbox. Thuswehave
numberofrearrange-  DA BC
DB AC
mentsoffourdifferent  =4 3 2 1=24 DC AB
× × ×
symbols
Ingeneralwehave
NumberofRearrangementsof N UniqueSymbols NumberofRearrangementsofN
UniqueSymbols
C(N) = N (N 1) 2 1
× − ×···× × C(N) = N × (N − 1) ×···× 2 × 1
= N! (3.1) = N!
wherewe’veintroducedthenotationforthefactorialof N as N!.
Example3.6 HowmanywayscanwerearrangethesymbolsA,A,A,and
D?
Symbols:AAAD
Byeyewecanseethatthereareonlyfourrearrangementsofthese Rearrangements
DAAA
symbols. Howisthisdifferentfromthepreviousquestionwithfour
ADAA
symbols? Wecanimaginegoingfromthefirstquestion,withfour AADA
uniquesymbols“ABCD,”andreplaceboth“B”and“C”with“A” AAAD
togetit. “BC”and“CB”aredifferentsequencesofuniquesymbols.
However,ifwereplace“B”withan“A”and“C”withan“A”,both
sequencesbecomethesamesequence,namely“AA”.Ifwetryto
blindlyapplyEquation3.1,theoneforthenumberofrearrangements
ofuniquesymbols,tothecasewherethereareduplicates,wewill
overestimatethenumberofrearrangements-weareovercounting
duplicatesubsequences. Further,wecanbespecificabouthowmuch


[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]








[TABLE]







random sequences and visualization 79
weareovercountingandthusfindanewequationwhichincludes
thepossibilityofduplicates.
Forexample,ifwehavethreeduplicatesinasequence,thenum-
berofovercountingswillbethenumberofpossiblerearrangements
ofthreeuniquesymbols,becausealloftheserearrangementsresultin
thesamesequenceofduplicatesymbols. Thus,ourprocedureshould
be,
numberofrearrange- 
  mentsoffourunique 
numberofrear-
symbols
rangementsof“A  =
numberofrearrange- 
AAD”
mentsoftheover- 
 
countedduplicatethree 
symbols
4!
=
3!
4 3 2 1
= × × ×
3 2 1
× ×
= 4
Example3.7 Howmanywaysarethereofrearrangingthesymbols“AA
ADD”?
Followingthesamelogic,wehave
5! waysof
rearranging
5unique
symbols
(cid:122) (cid:125)(cid:124) (cid:123)
AAA DD
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124)(cid:123)(cid:122)(cid:125)
3! waysof 2! waysof
rearranging rearranging
3duplicates 2duplicates
Allpossibleresultsofrearranging
  thesymbols“AAADD”:
numberofrear- 5! 1 AADDA
rangementsof  = 2 DAADA
3!2! 3 ADADA
“AAADD”
4 DAAAD
= 5 × 4 × 3 × 2 × 1 5 DADAA
(3 2 1) (2 1) 6 AADAD
12 × 0 × × × 7 DDAAA
= 8 ADDAA
6 2 9 AAADD
×
= 10 10 ADAAD
Sequences of Heads and Tails
Nowwecanreturntoouroriginalquestion,

80 statistical inference for everyone
Example3.8 Whatistheprobabilityofflippingtenheadsinthirtyflips,
withafaircoin?
Webrokeitdownintotwoparts:
 
numberofre-
 onesequenceof    arrangements  
ofalength-30 
P(h =10,N =30) = P10headsand20 



×sequencewith 
tails  
10“H”and20 
“T”
1 Whatistheprobabilityofoneparticularsequencebeingconsidered?
 
onesequenceof (cid:18) (cid:19)10 (cid:18) (cid:19)20
1 1
P10headsand20 =
2 × 2
tails
(cid:18) (cid:19)30
1
=
2
= 0.00000000093(oneinabillion!)
2 Howmanywayscanthistypeofsequenceappearintheprocess
describedinthequestion?
Becausewehavealength-thirtysequenceof“H”and“T”with
10duplicate“H”symbolsand20duplicate“T,”wehavethefol-
lowingnumberofwaysthatthiscouldoccur(i.e. thenumberof
rearrangementsofthesesequences):
 
numberofre-
arrangements 
 
ofalength-30  30!
  =
 
sequencewith  10!20!
 
10“H”and20 
“T”
= 30045015
Sotheprobabilityofflipping10headsin30flipsis
(cid:18) (cid:19)30
30! 1
P(h =10,N =30) =
10!20! 2
= 30045015 0.00000000093
×
= 0.028
whichisextremelyunlikely(Table1.1).
Ingeneralwehave

random sequences and visualization 81
Probabilityofflipping h headsand t tails Giventheprobability Probabilityofflippinghheads
offlippingasingleheadsas1/2,andthetotalnumberofflipsis andttails Giventheprobability
offlippingasingleheadsas1/2,
N = h+t,wehavethefollowingequivalentforms:
andthetotalnumberofflipsis
N = h+t,wehavethefollowing
P(h,t) = (h+t)! (cid:18) 1 (cid:19)h (cid:18) 1 (cid:19)t (3.2) probabilityforhheadsandttails:
h!t! × 2 × 2 (h+t)! (cid:18) 1 (cid:19)h (cid:18) 1 (cid:19)t
N! (cid:18) 1 (cid:19)h (cid:18) 1 (cid:19)N − h
P(h,t)=
h!t! × 2 × 2
P(h,N) =
h!(N h)! × 2 × 2
−
(cid:32) (cid:33) (cid:18) (cid:19)h (cid:18) (cid:19)N h
N 1 1 −
P(h,N) =
h × 2 × 2
wherewehaveintroducedthenotationthatissometimesused,called
choose,readas“Nchooseh,”
(cid:32) (cid:33)
N N!
h ≡ h!(N h)!
−
ShowninFigure3.1istheprobabilityofflipping h headsin30
flips,foreachvalueof h from h = 0(noheadsor,inotherwords,30
tails)upto h = 30(all30heads). Clearlythemostlikelyvalueis15,
butallofthenumbersfrom12upto18havesignificantprobability.
0.16
0.14
0.12
0.10
0.08
0.06
0.04
0.02
0.00
0 5 10 15 20 25 30
Number of heads
)03=N,h(P
Figure3.1:Probabilityofgetting
hheadsin30flips.Clearlythe
mostlikelyvalueis15,butallof
thenumbersfrom12upto18have
significantprobability.
Example3.9 Whatistheprobabilityofgetting17ormoreheadsin30
flips?
Becausetheseareindependentevents,wecansimplysumupthe
termsfor P(h = 17,N = 30), P(h = 18,N = 30),etc... yielding


[TABLE]





















82 statistical inference for everyone
thefollowing,eitherthroughdirectcalculation,orbyreadingthe
Figure3.1.
P(h 17,N =30) = 0.11+0.08+0.05+0.028+0.013+0.005+0.002+ (tinynumbers)
≥ (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124)(cid:123)(cid:122)(cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
h=17 h=18 h=19 h=20 h=21 h=22 h=23 h=23,24,25,26,27,28,29,30
=0.29
whichisquitelikely!
3.2 Binomial Distribution
Thedistributionofthepossiblenumberofheads,given N flipswith
acoinwithprobability p offlippingheads,isreferredtoastheBino-
mialDistribution. IthastheformofEquation3.3,withthe“faircoin”
probability,1/2,replacedwith p:
N!
P(h
|
N,p) =
h!(N h)! ×
ph
×
(1
−
p)N
−
h (3.3)
−
Probabilityofflipping h headsand t tailswithanunfaircoin Probabilityofflippinghheadsand
Giventheprobabilityofflippingasingleheadsis,say, p andthetotal ttailswithanunfaircoin Given
theprobabilityofflippingasingle
numberofflipsis N = h+t,wehavethefollowingequivalentforms:
headsasp,andthetotalnumber
offlipsisN = h+t,wehavethe
P(h,t) = (h+t)! ph (1 p)t (3.4) followingprobabilityforhheads
h!t! × × − andttails:
N! (h+t)!
P(h,N) =
h!(N h)! ×
ph
×
(1
−
p)N
−
h P(h,t)=
h!t! ×
ph
×
(1
−
p)t
−
(cid:32) (cid:33)
N
P(h,N) = ph (1 p)N
−
h
h × × −
wheretheprobabilityoftailsis1 p.
−
3.3 Some Philosophical Applications
Streaks
Intheprevioussectionwelookedattheprobabilityofgettingacer-
tainnumberofheadsinanumberofflips. Lookatthefollowingtwo
sequences:
1 HTTHTHHTTHTHTTHHHTHHTTHHTHHTTHTHHTHHTTHTTHHHTHTHTT
2 HHTHHHTTTTTTTHTHTTHTTTHTHTHHTHTTHTTTHHTTTHHHHTHHHH
Oneofthesesequenceswasgeneratedfromactuallyflippingacoin
50times. Theotheroneisfromapersonpretendingtoflipacoin,and

random sequences and visualization 83
0.25
0.20
0.15
0.10
0.05
0.00
0 5 10 15 20 25 30
Number of heads
)03=N,h(P
Figure3.2:Probabilityofgettingh
headsin30flipsgivenapossible
unfaircoin.Onecoinhasp =0.1,
p=0.1 wherethemaximumisfor3heads
p=0.5 (or1/10ofthe30flips),but2
p=0.8 headsisnearlyaslikely.Another
hasp = 0.5,andisthefaircoin
consideredearlierwithamaximum
at15heads(or1/2ofthe30flips).
Finally,anothercoinshownas
p=0.8where24heads(or8/10of
the30flips)ismaximum.
writingdownasequencethattheythoughtwouldlooklikearandom
flippingofacoin. Whichoneiswhich? Whilemanypeoplethink
thatsequence1looksmore“random”(i.e. itseemstofliparounda
lot),sequence2isactuallytherandomsequence.
Oneofthetrulyunintuitivethingsaboutrealrandomsequences,
asopposedtodesignedsequences,isthattherearelongrunsor
streaks. Whyisthis? Thegeneralsolutionisbeyondthisbookbut
wecanthinkaboutitthisway. Althoughasequenceof,say,5heads
inarowisveryunlikely(P(5headsinarow) = (1/2)5 = 0.03),
therearemanyopportunitiesforsuchasequencesomewherewithina
sequenceof50. Becauseofthesemanyopportunities,thisraisesthe
probabilityfrom3%(theprobabilityof5headsinarowin5flips),to
over55%,theprobabilityoffinding5headsinarowsomewherein50
flips. Streaksof6headsinarowoccurnearlyonethirdofthetimein
50flips,oroverhalfthetimeifyouconsideraruntobeeitherheads
ortails. Evenstreaksof9headsortailsinarow,in50flips,arenot
extremelyunlikely!
Gambler’s Fallacy
Whenwelookatasequenceofrealcoinflips,like:
• HHTHHHTTTTTTT
andweaskabouttheprobabilityofflippingheadsinthenextflip,it
iscommonto(mistakenly!) reasonthat,becausewe’veseen7tailsin


[TABLE]


p=0.1
p=0.5
p=0.8

p=0.1
p=0.5
p=0.8












84 statistical inference for everyone
arow,thenthenextflipismorelikelytobeheads. However,thisis
notthecasefortworeasons:
1 longstreaksarecommonincompletelyfairandrandomsequences
-soobservingastreakof7tailsdoesnotcontributemuchtoone’s
confidencethatwearelookingatariggedcoinoronethathas
changeditsprobabilityproperties.
2 theprocessofflippingacoinisindependenteachtime,nearlyby
definition,andthustheresultofoneflipcannotinfluencethe
1
resultofthenextflip. 1Onecanimagineaflippingpro-
cedurewheretheflipsarenot
Thefaulty,butintuitive,reasoninggoesbythenameoftheGam- independent.Say,youalwaysplace
theresultingface(headsortails)
bler’sFallacyandappearsinmanyplaces. Wecanaskaquestion:
initiallyupinaflip,andtheyou
donotflipparticularlyvigorously.
Howcouldwetellthedifferencebetweenarandom,independent
Thus,theresultofoneflipwould
sequenceandonewheretheeventsarenotindependent,wherethe berelatedtotheresultofthenext
nextflipdependedonapreviousflip? flip.However,innearlyallreal
cases,peoplegotogreatlengthsto
We’llhavetoreturntothisquestionlater,whenweconsidermodel avoidthissortofprocedure.
comparison,butroughly,onewouldhavetolookatallpairsofevents
toseeifonepair(sayheads-tails)occursmorefrequently(evenif
onlybyalittle)thananotherpair(sayheads-heads).
Inatotalfitofirony,casinoslotmachinesdonotproduceindepen-
dentwinnings-theyareprogrammedsothatifyou’velostmany
times,thenthatmachineisalittlelesslikelytolosethenexttime. In
effect,atgamblinghousestheytrainthegamblersintheGambler’s
Fallacy!
The Hot Hand - Correlations in Random Sequences
2
SomeworkbyTverskyandGilovich looksatthefollowingissuein 2A.TverskyandT.Gilovich. The
thesportofbasketball: therearetimeswhenitseemsasifbasketball coldfactsaboutthe"hothand"in
basketball. Anthologyofstatisticsin
playershavea“hothand”-theyareonashootingstreak. Tversky sports,16:169,2005
andGilovichlookedathowbasketballfansperceivedstreaks,byhav-
ingthemratesequencesofshotsasrandomshootingorstreakshooting.
Most(65%)oftherespondentsclassifiedartificiallygenerated,purely
randomsequencesasstreakshooting. Inrealdata,theydiscoveredthat
theactualprobabilityof“makingagivenshot(i.e. aplayer’sshoot-
ingpercentage)isunaffectedbytheplayer’spriorperformance.” We
examinethiseffectinalatersection(seeExample9.11onpage172)
whereweexplorethequantitativeprocedureforassessingthiscon-
clusion. Itisenoughheretonotethelargedifferencebetweenthe
perceptionofthesequenceandthelikelycauseofthesequence,and
thustheneedtoalwaysbevigilantagainstfaultyperceptions. Tver-
skyandGilovichinsistthat“theirobservationsdonottellusany-
thinggeneralaboutsports,butitdoessuggestageneralizationabout

random sequences and visualization 85
people,namelythattheytendto’detect’patternsevenwherenone
exist.”
Whatwehavehere,again,isthegeneralperceptionthatlongse-
quencesaresomehownot“random,”wheninfacttheoppositeisthe
case. Peoplehaveanaturaltendencytoseepatternsinrandomdata,
toinferorderwherethereisnone,andtoascribeimportancetothe
appearanceofpattern. Itistheroleofstatisticalinferenceingen-
eraltoprovidethetoolstoproperlyhandlethedistinctionbetween
randomeffectsandpatterns,andtoretuneourintuitions.
Regression Toward the Mean
Thereisapeculiarphenomenonreferredtoasregressiontowardthe
mean,whichoftenismisinterpretedandleadstofailuresofproper
statisticalinference. Itcanbeseeninasimpleexample. Imaginethat
we“test”anumberofstudentsbyhavingthemguesstheresultsofa
coinflip. Clearlythiswillbeentirelyluck,becausethecoinfliphas
nopattern. Ifastudentguessestheresultsof50flips,therewillbean
expectationofgetting25correct. Herewesimulate20studentseach
“predicting”theresultof50flips,theresultsshowninTable3.1. The
testisdonetwice,andwewilllookataparticularsubsetpresently.
Onecan,byeye,seethatmostofthestudentsgetaround25correct-
exactlyasexpectedfromrandomperformance.
Now,imaginethatwelookatthetopfivecoinflippredictorson
thefirstround. Willtheydobetterorworseinthethesecondround?
Whataboutthebottomfivecoinflippredictors? Theresultsofthese
twocasesaresummarizedinTable3.2. Thepattern,eveninthis
smallsample,isquiteclear:
1 Thosethatdidthebestthefirsttimedidworsethesecond(on
average)
2 Thosethatdidtheworstthefirsttimedidbetterthesecond(on
average)
Onemightbetempted(hadyounotknownthatthisisartificialdata,
andcompletelyrandom)tointerpretthisasacausalpattern,e.g.
“thestudentsthatdidbetterthefirsttime,grewover-confidentthe
secondtime,”“thestudentsthatdidworsethefirsttime,worked
hardertoimprovethesecondtime,”etc... Thisinterpretationofthe
3
resultsbystudentshasbeenobservedintheclassroom. However,it 3
runsintoserioustroublewhenthedataissomethingliketheheights
ofchildrencomparedtotheirparents-thetallestparentstendto
havechildrenshorterthantheyare,theshortestparentstendtohave
childrentallerthantheyare,apatternfirstquantifiedbyGaltonin
18694
. Henotedthatclearlythechildrenarenottryingtobetall,so 4

86 statistical inference for everyone
Student TotalCorrect TotalCor-
Table3.1:TotalCorrectGuesses
fromStudents“Predicting”the
FirstRound rectSecond Resultsof50CoinFlips.Shownare
Round theresultsofafirstroundanda
secondroundofguessing.
1 23 24
2 23 29
3 19 23
4 26 27
5 28 29
6 26 22
7 23 26
8 30 28
9 24 21
10 27 23
11 25 31
12 30 21
13 20 22
14 28 29
15 24 25
16 25 22
17 23 24
18 20 28
19 20 29
20 28 25
Table3.2:PerformanceintheSec-
ondRoundofStudents“Predicting”
theResultsof50CoinFlips.Shown
TopFivetheFirstTime BottomFivetheFirstTime aretheresultsforthosestudents
whoperformedbestinthefirst
round(left),andthosethatper-
Student Performancethe Student Performancethe formedworstinthefirstround
SecondTime SecondTime (right).
8 Worse 3 Better
12 Worse 13 Better
14 Better 18 Better
5 Better 19 Better
20 Worse 1 Better

random sequences and visualization 87
effortisnotagoodexplanationforthepattern.
Whatishappeninghereisthat,iftheprocessisdominatedbyluck
orsimplerandomvariation,thenoutliersoccur,butarerare. Thus
aparticularlyhighvaluewilllikelybefollowedbyalowervalue-
closertothemean. Thetendencyistoregresstowardthemeaninpro-
cessesdominatedbyluck. ThiscanbeconfusedwiththeGambler’s
Fallacydiscussedearlier,whereflipping3headsinarowdoesn’t
giveyouanyinformationaboutflippinganotherheads-itisnot
morelikelytobetails. Partofthedifferenceisthatwearedealing
withaprocessthathasmanypossiblevalues,notjusttwo,andthuswe
canhaveameanvalue,andoutliers.
Wheneachoftheseideasisappliedtosports,theweather,or
businesstherearesomeinterestingconclusions.
1 evenwhentheprocessisentirelyrandom,longstreaksoccur-and
areoftenmisinterpretedasanincreaseintheprobabilityofthe
event.
2 whenapersonperformsverywellattheirjob(anumberofsuc-
cessfulbusinessdecisions,ahighbattingaverage,etc...) theywill
oftendoworsethenextyear-andagainmanyaresurprised,and
interprettheresultastheperson“losingtheirtouch”-whenin
fact,theymayjusthavebeenluckyforabit,andarenowperform-
ingclosertotheirtypicalaveragelevel.
3 whenonehasaparticularlybadwinter,itmaybemorelikelythat
thenextwinterwon’tbequitedobad-dueentirelytoregression
tothemean. Itmay,however,bepartofalargerpattern(e.g. a
large-scaleclimateoscillation,suchasElNiño)andtheprobability
ofanotherbadwintermightbehigher. Inordertotellthediffer-
ence,weneedtoconstructreasonablemodelsofthephenomena,
testthosemodelswithpredictions,andapplythosemodelsinto
thefuture. Ateachstep,weneedtobecarefulnottojumptothe
conclusionoftheexistenceofapatterntooquickly.
3.4 Visualization of Data
Therearetwomainmethodsofvisualizingdata,andseveralothers
thatarerelatedtothesemethods. Inthissectionweintroducejust
two,histogramsandscatterplots,andwewillusethesethroughout
thetext.
Histograms
Histogramsareawayofsummarizingdata,whenpresentingthe
entiredatasetisimpractical,orwheresomeunderstandingofthe

88 statistical inference for everyone
dataismadeclearerbysummarizing. Thehistogramplotisdone
withthefollowingsteps: Anotheradvantagetolearning
tounderstandhowtogenerate
histogramsisthatitalertsyou
tothepossibleabusesofthese
1 Chooseanumberofbinstodividethedata. plots.Theseabusescanbesimple
mistakes,whichendupgivinga
misleadingmessage,oradeliberate
deception.Eitherway,aproper
understandingoftheprocesshelps.
2 Countupthedatathatfallintoeachbin
3 Makeabarplot,orascatterplottopresentthedata.
Thefollowingisanexamplewithasmalldataset. Theprocessof
binningandcountingisoftendonebycomputer,butitisinstructive
toperformtheprocessbyhandafewtimesinordertounderstand
whattheresultsare.
Table3.3showsacollectionof106heights(incentimeters)ofthe
5
malestudentsinaclass . Asacollectionofnumbersitisrelatively 5
opaque,butasahistogramitisclearer.
177.8 160.0 165.0 182.88 175.0 167.0 Table3.3:106MaleStudentHeights
(incm)fromaSurvey.
182.88 190.5 177.0 190.5 180.34 180.34
184.0 172.72 175.26 167.0 180.0 180.0
190.0 182.5 185.0 171.0 172.0 180.34
180.0 170.0 200.0 190.0 170.18 179.0
182.0 171.0 177.8 175.26 187.0 183.0
180.0 176.0 185.42 176.5 167.64 179.0
183.0 179.0 190.0 165.0 187.0 170.0
180.0 180.34 190.5 185.0 193.04 184.0
177.0 180.0 175.26 180.34 178.5 187.96
178.0 175.26 189.0 182.88 170.0 180.0
185.0 187.96 185.42 195.0 172.72 180.34
173.0 187.96 187.0 168.0 191.8 177.0
189.0 180.34 182.88 172.72 172.0 170.0
175.0 168.0 165.0 173.0 196.0 179.1
180.0 176.0 154.94 174.0 179.1 160.0
165.0 165.0 170.0 185.0 188.0 171.0
185.0 185.0 180.34 183.0

random sequences and visualization 89
30
25
20
15
10
5
0
150 160 170 180 190 200 210
Height [cm]
elpoeP
fo
rebmuN
Fromthishistogram,wecanimmediatelyobserveseveralquantities
whichsummarizetheirdata:
1 Theaveragevalue(aroundthemiddle)shouldbearound175cm.
Theactualvaluecanbecalculatedfromthedata,as
177.8+160.0+ +180.34+183.0
x¯ = ··· =178.83
106
2 Therangeofthedataisaround155cmuptoabout205cm. Again
wecanbemoreprecise,andfindtheminimumofthedata(154.94
cm)andthemaximum(200cm)butthehistogrampictureyields
anapproximatevalueinstantly.
3 Thevaluesareroughlysymmetricaboutthemean(i.e. average)
value. Thiscangiveusaclueconcerninghowtomodelthedata.
Whatisquiteclearisthatitisfareasiertodealwithahistogram,as
above,thanfindthesameinformationfromthetableofnumbers.
TooFewBins Plottingthesamehistogramwithtoofewbinsmight
looklike:


[TABLE]































90 statistical inference for everyone
90
80
70
60
50
40
30
20
10
0
140 150 160 170 180 190 200 210
Height [cm]
elpoeP
fo
rebmuN
Clearlyalltheinformationiswashedout.
TooManyBins Plottingthesamehistogramwithtoomanybins
mightlooklike:
16
14
12
10
8
6
4
2
0
150 160 170 180 190 200 210
Height [cm]
elpoeP
fo
rebmuN
Weloseanyofthesummaryinformationhere,whereweessen-
tiallyhaveonebarforeachdata-point.
Scatter Plots
Ascatterplotisusedtoexploretherelationshipbetweentwovalues.
Forexample,inthesurveyofmalestudents,inadditiontoheightthe
studentsalsomeasuredthewidthoftheirwritinghandviewedasa
histogram,here


[TABLE]




























[TABLE]





















random sequences and visualization 91
14
12
10
8
6
4
2
0
16 17 18 19 20 21 22 23 24
Writing Hand Span [cm]
elpoeP
fo
rebmuN
However,duetothepossibilitythatthesetwovariablescouldbe
related,itmakesmoresensetomakeascatterplot. Insuchaplot,one
designatesonevariableas“x”andanotheras“y,”andplacesasingle
dotforeachpairofvaluesinthedataset. Thus,eachdotontheplot
correspondstoheightandhand-widthforasinglestudent.
24
23
22
21
20
19
18
17
16
15
150 160 170 180 190 200 210
Height [cm]
]mc[
napS
dnaH
gnitirW
Whatwecanseehere,whichwasobscuredwithahistogram,is
therelationshipbetweenthesevalues-forthetallerstudents,their
handsarewider. Wewillexplorequantifyingthisrelationshiplater,
butmuchcanbedonebyeyeusingascatterplot.


[TABLE]






























[TABLE]























92 statistical inference for everyone
3.5 Computer Examples
Thissectionsummarizeshowtomakehistogramsandscatterplots
withthecomputersoftware.
Histograms
from sie import *
Loadasampledataset,andselectonlytheMaledata...
data=load_data( ’data/survey.csv ’)
male_data=data[data[ ’Sex’]==’Male’]
selectonlytheheightdata,anddropthemissingdata(na)...
male_height=male_data[ ’Height’ ].dropna()
makethehistogram
hist(male_height ,bins=20)
xlabel( ’Height [cm] ’)
ylabel( ’Number of People’)
<matplotlib.text.Text at 0x1085728d0>
Scatter Plot
from sie import *
Loadasampledataset,andselectonlytheMaledata...


[TABLE]




from sie import *







[TABLE]




data=load_data( ’data/survey.csv ’)

male_data=data[data[ ’Sex’]==’Male’]







[TABLE]




male_height=male_data[ ’Height’ ].dropna()







[TABLE]




hist(male_height ,bins=20)

xlabel( ’Height [cm] ’)

ylabel( ’Number of People’)







[TABLE]




from sie import *






random sequences and visualization 93
data=load_data( ’data/survey.csv ’)
male_data=data[data[ ’Sex’]==’Male’]
selectonlytheheightandthewidthofwritinghanddata,anddropthemissingdata(na)...
subdata=male_data[[ ’Height’ , ’Wr.Hnd’ ]].dropna()
height=subdata[ ’Height’]
wr_hand=subdata[ ’Wr.Hnd’]
plotthedata
plot(height ,wr_hand, ’o’)
ylabel( ’Writing Hand Span [cm] ’)
xlabel( ’Height [cm] ’)
<matplotlib.text.Text at 0x1085774d0>


[TABLE]




data=load_data( ’data/survey.csv ’)

male_data=data[data[ ’Sex’]==’Male’]







[TABLE]




subdata=male_data[[ ’Height’ , ’Wr.Hnd’ ]].dropna()

height=subdata[ ’Height’]

wr_hand=subdata[ ’Wr.Hnd’]







[TABLE]




plot(height ,wr_hand, ’o’)

ylabel( ’Writing Hand Span [cm] ’)

xlabel( ’Height [cm] ’)








4 Introduction to Model Comparison
1
Amodel asweusetheterminthisbookisaspecificdescriptionofa 1Asimilartermishypothesis,and
possiblestateofnature. Thisisincontrasttoanactualstateofnature, modelcomparisonwouldthenbe
hypothesistesting.Wedon’tchoose
whichwepracticallyneverhaveaccessto. Wecanneverknowany-
tousethatterm,partlybecauseof
thingwith100%certainty,andmustthereforebeopentoalternate thecolloquialuseofhypothesisas
akindof“guess,”butalsobecause
possibleexplanations,ormodels,describingourobservations. For
hypothesistestinginsometreat-
example,inmedicinesuchmodelscouldinclude“Ihavelungcan- mentsfocusontrue/falsetestsof
cer,”“Ihavepneumonia,”and“Ihaveacold.” Inphysics,models hypotheseswhichcanleadtosome
significantmisunderstandings.The
couldinclude“theEarthmovesaroundtheSun”and“theSunmoves
useofmodelsimpliesthepossibil-
aroundtheEarth.” Wecanimaginemanypossiblemodelsthatare ityofmultiple(i.e.morethantwo)
models.
consistentwiththeobserveddata,andourjobindoingstatisticalin-
ferenceistodeterminetheprobabilitiesofourmodelsgiventhedata
weobserve. Inournotation,whatwearealwayslookingforis
P(model data) (4.1)
|
Wewillexploremodelcomparisonthroughaseriesofexamples.
4.1 The High/Low Deck Game
Inthisexampleweuseasimplecardgameasaplatformfordis-
cussingmodelcomparisoningeneral. Westartwithtwoatypical
decksofcardscalledtheHighDeckandtheLowDeck(Figures4.1
onpage96and4.2onpage96respectively). Thegamegoesasfol-
lows.
You’rehandedoneofthetwodecks,butyoudon’tknowwhich. First,
youdrawthetopcardandnotethevalue. Second,youreplacethe
2
cardandreshufflethedeck . Yourepeatthisprocedureofdrawing, 2Althoughwecouldmakeagame
noting,andreshufflingforasmanyturnsasyouneed. Thegoalisto withoutreplacement,whichmaybe
simplertoimplement,theversion
determinewhichofthethetwodecks(HighorLow)youareinfact
ofthegamewithreshufflingwill
holdinginyourhand.
helpwithanexamplelater.
What does our intuition say?
Westartbyexploringourintuitions,beforewedoanythingmath-
ematically. Thus,weareinapositiontochecktoseeifthemathis

96 statistical inference for everyone
Figure4.1:HighDeck-55Cards
withten10’s,nine9’s,etc...down
tooneAce.Acesareequivalentto
thevalue1.
Figure4.2:LowDeck-55Cards
withtenAces,nine2’s,etc...upto
one10.Acesareequivalenttothe
value1.

introduction to model comparison 97
reasonablebeforeweusethesamemathinareaswhereourintuition
isnotasstrong. Imaginewedrawonlyonecard,anditisa9. Intu-
itionsuggeststhatthisconstitutesreasonablystrongevidencetoward
thebeliefthatwe’reholdingtheHighDeck. Ifwethen(asthepro-
cedurestates)placethe9backinthedeck,reshuffleandthendraw
a7wecanbemorestronglyconvincedthatweareholdingtheHigh
Deck. Repeatingthereshuffle,andthendrawinga3wouldmake
usalittlelessconfidentinthisconclusion,butstillquitecertain. In
thiswaywecansensehowdrawingdifferentcardspushesourbelief
around,dependingonhowoftenthatcardcomesupinthedifferent
decks.
Before the data - the prior
Beforewetakeanydata,weneedtoquantifyourstateofknowledge
concerningallofthemodelsthatweareconsidering. Inthiscaseit
isquitesimple,becausetherearetwomodels(HighDeckandLow
Deck),andwehavebeengivennoinformationaboutwhethereither
ismorecommon. Withnosuchinformation,itisequivalenttoacoin
flip-weassignequalprobabilitiestobothmodelsbeforeweseedata,
3
alsoknownasthepriorprobabilities . 3Thepriorissometimesmischar-
acterizedassimplyourguess,or
P(H) = 0.5 someothercompletelysubjective
assessmentofourknowledge.In
P(L) = 0.5 factinthisexample,andmany
others,wecanmakethepositive
Surelythisassessmentwillchangeafterweseedata,butthatisthe caseforequalprobabilitiesgiven
thestateofourknowledge.This
restoftheproblem.
canbequantifiedwiththeconcept
ofentropy,whichisbeyondthis
chapter.
The “easy” question - the likelihood
Althoughourultimategoalistoinferthetypeofdeckfromthecards
thatwedrawfromit,wecanstartlookingataneasierpartofthis
questionwhichservesasafirststeptowardthemorechallenging,
andinterestinggoal. Thatquestionisthefollowing,
Example4.1 Whatistheprobabilityofdrawinga9,giventhatweknow
thatwe’reholdingtheHighDeck?
Thisrelatedquestioniswritten
P(data=9 H)
|
wheredata = 9meansthatwehaveobserved(i.e. drawn)one9.
Thisquestionis“easy”inthesensethatitissimplyrelatedtothe
propertiesoftheHighDeck: thenumberof9’sandtotalnumber
ofcards. Ifyouknowthatyouhavethehighdeck,thenyouknow
therearenine9’sinthatdeckoutof55cards,andthuswehavethe

98 statistical inference for everyone
probabilityofdrawingone9,giventhatweareholdingtheHigh
Deck,is
9
P(data=9 H) =
| 55
4
Wegivethisthenamelikelihood ,andissimplytheprobabilitythat 4Thetermlikelihoodisapoorly
thedatacouldbetheresultofaknownmodel. Itisalsothefirstpart chosenword.InEnglish,thisword
isnearlysynonymouswiththe
ofthetopofBayes’Rule,Equation1.14onpage47.
wordprobabilityandthuseasily
leadstoconfusion.Wecouldtryto
useadifferentterm,likeconsequent
Applying the Bayes’ recipe
probabilityorgenerativelikelihood
tostresstheideathatthelikelihood
Hereweintroduceforthefirsttimearecipewewillfollowforall istheprobabilitythatthedatawe
modelcomparisonexamples. observecouldbegeneratedorcould
beaconsequenceoftheparticular
Nowthatwehaveourintuition,andwehavethelikelihoods,we
model.However,we’dbegoingup
canaddressthemath. Thetwomodelsare: againsttwocenturiesofcontinued
useofthetermlikelihoodandthus
H “We’reholdingtheHighDeck” wouldprobablyincreaseconfusion
≡ ratherthandecreaseit.
L “We’reholdingtheLowDeck”
≡
andtheinitialdatais
data “We’vedrawnonecard,anditisa9”
≡
AccordingtoEquation4.1onpage95wearelookingforthetwo
probabilities:
P(H data=9)
|
P(L data=9)
|
whicharerelatedtothepriorandthelikelihoodviaBayes’Rule(Equa-
tion1.14):
P(data=9 H)P(H)
P(H data=9) = |
| P(data=9)
P(data=9 L)P(L)
P(L data=9) = |
| P(data=9)
Tocalculateactualnumbers,weapplytheBayes’Recipetothis
problem,
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(H) = 0.5
P(L) = 0.5
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data=9) P(data=9 H)P(H)
| ∼ |
P(L data=9) P(data=9 L)P(L)
| ∼ |

introduction to model comparison 99
whereweareusingthesymbol todenoteproportionalityorre-
∼
latedto. Essentially,bycalculatingthetopofBayes’Rulefirst,the
numbersarenotequaltothefinal(i.e. posterior)probabilitiesbut
mustberescaledtomakesurethattheyaddupto1. Thisisdone
inthefinalstep. Upuntilthatrescaling,weusethesymbol and
∼
thinkofitasrelatedto.
3 Putinthelikelihoodandpriorvalues
9
P(H data=9) 0.5=0.082
| ∼ 55 ×
2
P(L data=9) 0.5=0.018
| ∼ 55 ×
4 Addthesevaluesforallmodels
K =0.082+0.018=0.1
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
P(H data) =0.082/0.1=0.82
|
P(L data) =0.018/0.1=0.18
|
Fromwhichwecanconcludethatdrawinga9doesindeedconsti-
tutereasonablystrongevidencetowardthebeliefthatwe’reholding
theHighDeck-theprobabilityofusholdingtheHighDeck,given
thedata,is0.82.
Drawing the next card
So,whenwedrawa7next(afterreshuffling),ourintuitionsuggests
thatwe’dbemoreconfidentthatwe’reholdingtheHighDeck. Re-
peatingourrecipewehave
Thetwomodelsare:
H “We’reholdingtheHighDeck”
≡
L “We’reholdingtheLowDeck”
≡
anddatais
(cid:26) “We’vedrawnonecard,anditisa9,replaced
data
≡ andreshuffled,andthendrawna7”
AccordingtoEquation4.1wearelookingforthetwoprobabilities:
P(H data=9thena7)
|
P(L data=9thena7)
|

100 statistical inference for everyone
whicharerelatedtothepriorandthelikelihoodviaBayes’Rule(Equa-
tion1.14):
P(data=9thena7 H)P(H)
P(H data=9thena7) = |
| P(data=9thena7)
P(data=9thena7 L)P(L)
P(L data=9thena7) = |
| P(data=9thena7)
Tocalculateactualnumbers,weapplytheBayes’recipetothis
problem,
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(H) = 0.5
P(L) = 0.5
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data=9thena7) P(data=9thena7 H)P(H)
| ∼ |
P(L data=9thena7) P(data=9thena7 L)P(L)
| ∼ |
3 Putinthelikelihoodandpriorvalues Asareminder,weareperforming
thisnextdrawhavingshuffled
9 7 thefirstdrawbackintothedeck.
P(H data=9thena7) 0.5=0.0104
| ∼ 55 × 55 × Althoughsomewhatartificial,itis
usefulforalaterexample.Ifwe
2 4
P(L data=9thena7) 0.5=0.0013 hadsimplysetthefirstcardasside,
| ∼ 55 × 55 × thevalueofthelikelihoodwould
4 Addthesevaluesforallmodels accountfortheremovalofonemore
card,andwouldthusbe 9 7 for
55×54
thehighdeckand 2 4 forthe
K =0.0104+0.0013=0.0117 lowdeck.Notethe 5 d 5 e × no 5 m 4 inators.
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
P(H data=9thena7) =0.0104/0.0117=0.889
|
P(L data=9thena7) =0.0013/0.0117=0.111
|
whichagainmatchesourintuition-we’remoreconfidentthat
we’reholdingtheHighDeck,nowwithprobability0.889increased
from0.82whenwejustobservedthe9.
Prior information or not?
Intheaboveexample,westartedwithapriorprobabilityofholding
theHighDeckat P(H) = 0.5,becausewehadnoinformationother
thanthatthereweretwopossibilities. Wethenobserveda9,and
updatedtheprobabilityto0.82,andthenobserveda7,andfurther
updatedtheprobabilityto0.889-makingitmorelikelythatwewere

introduction to model comparison 101
holdingtheHighDeck. Oneofthebasictenetsofprobabilitythe-
oryisthatifthereismorethanonewaytoarriveatananswer,one
5
shouldarriveatthesameanswer. Intheabove,wecalculatedthe 5E.T.Jaynesusestheprinciplethat
probabilityofholdingtheHighDeckgiventheobserveddata “ifthereismorethanonewayto
arriveatananswer,oneshould
(cid:26) “We’vedrawnonecard,anditisa9,replaced arriveatthesameanswer”tohelp
data derivetherulesofprobability
≡ andreshuffled,andthendrawna7”
fromfirstprinciples.Failuresof
thisprincipleresultinparadoxes.
Thisprincipleisalsoapplied
andpriorinformation inSection2.4forthebirthday
problem.
prior “Weknowthereareonlytwodecks.”
≡
Anequivalentsituationisfoundafterourfirstdraw,afterwe’ve
observedthe9,andwe’reabouttodrawoursecondcard. Inthiscase
wehavethepriorinformation:

“Weknowthereareonlytwodecks,andthen

prior wedrawonecardanditisa9,replaceitand
≡ 
reshuffle.”
andobserveddata:
data “We’vedrawnonecardanditisa7”
≡
Mathematically,weapplytheBayes’recipe,butwiththedifferent
priorinformation
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(H,9) = 0.82
P(L,9) = 0.18
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data=9thena7) P(data=7 H)P(H,9)
| ∼ |
P(L data=9thena7) P(data=7 L)P(L,9)
| ∼ |
3 Putinthelikelihoodandpriorvalues
7
P(H data=9thena7) 0.82=0.104
| ∼ 55 ×
4
P(L data=9thena7) 0.18=0.013
| ∼ 55 ×
4 Addthesevaluesforallmodels
K =0.104+0.013=0.117

102 statistical inference for everyone
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
P(H data=9thena7) =0.104/0.117=0.889
|
P(L data=9thena7) =0.013/0.117=0.111
|
yieldingthesameresult.
Inotherwordsourupdatedprobabilitiesfromthefirstdrawcanbe
seenasourpriorprobabilitiesforthesubsequentdraws. Thus,Bayes’
Ruledescribeshowweupdateourknowledgewithnewevidence,or
inotherwords,learning.
4.2 Multiple Hypotheses
Westartthissectionwithanexample.
Example4.2 Whatistheprobabilitythatyouareholdingoneofeitherthe
HighortheLowDeckhavingdrawnfive9’sinarowfromthatdeck?
Wehaveobservedthefollowingdata:
“We’vedrawnonecard,anditisa9,replaced
andreshuffled,redrawnandobservedanother
data
≡  9
m
,
o
r
r
e
e
pe
9
a
’s
t
,
ed
fo
t
r
h
a
is
to
p
t
r
a
o
l
c
o
e
f
d
fi
u
v
re
e
a
9
n
’s
d
in
ob
a
se
ro
rv
w
e
.
d
”
three
Technically,drawing59’sinarowshouldgiveusreallystrongcon-
fidencethatyouaredrawingfromtheHighDeck,becausewewould
have
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(H) = 0.5
P(L) = 0.5
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data=59’sinarow) P(data=59’sinarow H)P(H)
| ∼ |
P(L data=59’sinarow) P(data=59’sinarow L)P(L)
| ∼ |
3 Putinthelikelihoodandpriorvalues
9 9 9
P(H data=59’sinarow) P(H)
| ∼ 55 × 55···55×
(cid:124) (cid:123)(cid:122) (cid:125)
5times
(cid:18) (cid:19)5
9
0.5
∼ 55 ×
= 0.0000587
(cid:18) (cid:19)5
2
P(L data=59’sinarow) 0.5
| ∼ 55 ×
= 0.0000000318

introduction to model comparison 103
4 Addthesevaluesforallmodels
K =0.0000587+0.0000000318=0.0000587318
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
0.0000587
P(H data=59’sinarow) = =0.99946
| 0.0000587318
0.0000000318
P(L data=59’sinarow) = =0.00054
| 0.0000587318
whichisfantasticallyonthesideofthehighdeck,eventhoughwe
mightstartgettingsuspiciousinthissituation.
Example4.3 Whatistheprobabilitythatyouareholdingoneofeitherthe
HighortheLowDeckhavingdrawnm9’sinarowfromthatdeck,wherem
standsforanumber(m =1,2,3, )?
···
Ingeneral,ifwelookat m 9’sinarow,where m couldbe1,2,3,
etc...,wecanseethisfollowingtheBayes’Recipe
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(H) = 0.5
P(L) = 0.5
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data= m 9’sinarow) P(data= m 9’sinarow H)P(H)
| ∼ |
P(L data= m 9’sinarow) P(data= m 9’sinarow L)P(L)
| ∼ |
3 Putinthelikelihoodandpriorvalues
9 9 9
P(H data= m 9’sinarow) P(H)
| ∼ 55 × 55···55×
(cid:124) (cid:123)(cid:122) (cid:125)
mtimes
(cid:18) (cid:19)m
9
0.5
∼ 55 ×
(cid:18) (cid:19)m
2
P(L data= m 9’sinarow) 0.5
| ∼ 55 ×
4 Addthesevaluesforallmodels
(cid:18) (cid:19)m (cid:18) (cid:19)m
9 2
K = 0.5+ 0.5
55 × 55 ×
5 Divideeachofthevaluesbythissum, K,togetthefinalproba-
bilitiesThisstepiseasiestdoneinatable(Table4.1),becausethe
resultingexpressionisprettymessy.

104 statistical inference for everyone
m P(H data) P(L data) Table4.1:Drawingm9’sinarow,
| |
fromeitheraHighDeckorLow
1 0.81818 0.18182
Deck.
2 0.95294 0.047059
3 0.98915 0.010855
4 0.99757 0.0024327
5 0.99946 0.00054163
6 0.99988 0.00012041
7 0.99997 0.000026761
8 0.99999 0.0000059470
ItisclearfromTable4.1thatafterdrawingfive9’susingourpro-
cedure,itshouldbeextraordinarilylikelythatweareholdingthe
HighDeck. However,afteracertainnumberof9’sobserved,some-
thingstartstobotherus. Perhapsnotafterfive9’s,butwhatifthe
procedurewererepeatedandwedrewten9’sinarow? Orperhaps
twenty9’s. Atsomepoint,we’drefusetobelievethisistheHigh
Deckbecause,althoughitwastruethattherearemore9’sinthe
HighDeck,therearemanymoreothercardsintheHighDeckthatwe
shouldsee. Whatdowedointhiscase?
Example4.4 Whatistheprobabilitythatyouareholdingoneofeitherthe
High,Low,orNinesDeckhavingdrawnm9’sinarowfromthatdeck?
Theproperthingtodoistointroduceanewmodel,say,aNines
deck. Clearlythismodelshouldhaveaverylowpriorprobability, Whatisinterestinghereisthat
becausewedidn’tevenconsideritbeforewesawthestreakof9’s. onceweadmitthattherearemany
possiblemodelswecouldconsider,
Let’ssaythatweassignthepriorprobabilityfortheNinesdeckto
werealizethatwehavethese
beaoneinamillion. Tomakeallofthepriorprobabilitiesaddupto modelsinourheadallthetime,
1,thenthepriorprobabilitiesfortheHighandLowDeckmustbea orweconstructthemasweneed
them.Everymodelcomparison
littlelessthan0.5. Afterthat,wesimplyapplytheBayes’Recipeas isamultiplemodelcomparison,
before withmostofthemodelswithvery
lowpriorprobabilitiesthatour
brainnaturallysuppressesuntil
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered needed.Mathematically,weneedto
unsuppressthemasneeded.
1
P(N) = =0.000001
1,000,000
P(H) = 0.4999995
P(L) = 0.4999995
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(N data= m 9’sinarow) P(data= m 9’sinarow N)P(N)
| ∼ |
P(H data= m 9’sinarow) P(data= m 9’sinarow H)P(H)
| ∼ |
P(L data= m 9’sinarow) P(data= m 9’sinarow L)P(L)
| ∼ |

introduction to model comparison 105
3 Putinthelikelihoodandpriorvalues
P(N data= m 9’sinarow) 1 P(N) =0.000001
| ∼ ×
9 9 9
P(H data= m 9’sinarow) P(H)
| ∼ 55 × 55···55×
(cid:124) (cid:123)(cid:122) (cid:125)
mtimes
(cid:18) (cid:19)m
9
0.4999995
∼ 55 ×
(cid:18) (cid:19)m
2
P(L data= m 9’sinarow) 0.0.4999995
| ∼ 55 ×
4 Addthesevaluesforallmodels
(cid:18) (cid:19)m (cid:18) (cid:19)m
9 2
K =0.000001+ 0.4999995+ 0.4999995
55 × 55 ×
5 Divideeachofthevaluesbythissum, K,togetthefinalproba-
bilitiesAgain,thisstepiseasiestdoneinatableor,evenbetter,a
picture(Figure4.3).
1.0
0.8
0.6
0.4
0.2
0.0
0 2 4 6 8 10 12 14
Number of 9's in Drawn in a Row
ytilibaborP
roiretsoP
ledoM
Figure4.3:Drawinganumberof
9’sinarow,possiblyfromaHigh,
Low,andNinesdeck.
Low Deck
High Deck
Nines Deck
WehaveaclearpicturehereinFigure4.3. Asweinitiallydraw
9’s,ourconfidencethatwe’reholdingtheHighDeckgoesup,at
theexpenseofourconfidencethatwe’reholdingtheLowDeck. At
acertainpoint(aroundsix9’sinourexample),ourconfidencein
theHighDeckstartstodropandwebecomemoreconfidentthat
somethingoddishappening,andourpreviouslyignoredmodelof


[TABLE]








Low D
High D
Nines | eck
eck
Deck










106 statistical inference for everyone
theNinesdeckbecomesmorelikely. Eventually,thisnewmodelis
theoneinwhichwearethemostconfident.
Imaginefurtherthatif,afterdrawingten9’sinarowwedrawa1.
Whatdowedothen? ThelikelihoodfortheNinesdeckgoestozero
instantly-theprobabilityofdrawinga1fromaNinesdeckiszero,
P(1 N) = 0. Areweleftagainwiththeoriginaltwomodels,High
|
andLowDeck? No! Wewouldthenintroduceothermodels,perhaps
somethinglikeaMostlyNinesDeck,orperhapsaHighDeckwitha
weirdshufflingprocedure,orperhapsothers. Nomatterhowmany Thecreativepartofscienceisnot
modelsonehas,therecipeisstillthesame. Itisimportanttorealize inthecalculationsperformed,but
inthegenerationofnewanduseful
thatinanymodelcomparisoncase,therearealwaysothermodels
models.Untilwecomeupwitha
thatcouldbebroughttobearontheproblem,perhapswithlowprior bettermodelforourdatawemake
dowiththeonesthatwehave,all
probability. Simplyshowingthatamodelisconsistentwithasetof
thewhilebeingawarethatabetter
datadoesnotinsureagainstthepossibilitythatanothermodelcould modelmaycomeintoplaylater.
bebetter,ifwecouldonlythinkofit. Newton’sTheoryofGravitywas
usedforover200years,evenwhen
Exercise4.1 Completetheexampledemonstratingtheupdatedprobabil- therewasknowndatathatmade
itlesslikely,untilitwasreplaced
itiesfortheHighandLowDeck,havingdrawna9,7,anda3. Compare byEinstein’sTheoryofGravity.
withthecaseofdrawingjustthe9andthe7,anddiscusshowitmatches Newton’sLaws,however,arestill
usedinnearlyallgravitational
yourintuition.
calculationsbecauseitis“good
enough”andisaloteasiertowork
Exercise4.2 Repeattheanalysisofthesequenceof9’sdrawninarow withpractically.
withanaddedhypothesisofadeckwithonehundred9’sandone8. Discuss
theresults. Demonstratewhathappenstotheprobabilitiesforallofthe
hypothesesafterdrawingone8,afterten9’sinarow. Discuss.
Exercise4.3 ItellyouthatIhaveacointhatcouldhavebothsidesheads,
bothsidestails,oranormalsingle-headssingle-tailscoin.
1 Beforeseeingthedata,whatwouldbeareasonablepriorprobabilityfor
thethreehypotheses H (no-heads), H (onehead),and H (twoheads)?
0 1 2
2 Wouldthishavebeendifferentifyouhadsimplybeengivenacoinbya
friendtofliptoseewhohastodothedishes? Whyorwhynot?
3 NowIflipthecoinonce,andgetaheads. Writedownthelikelihoodof
thisdatagiveneachofthemodels. Inotherwords,whatarethevaluesof:
• P(data=1heads H )
0
|
• P(data=1heads H )
1
|
• P(data=1heads H )
2
|
4 ApplyBayes’Recipe,anddeterminetheprobabilityofeachofthesethree
modelsgiventhisdata. Inotherwords,whatarethevaluesof:
• P(H data=1heads)
0
|
• P(H data=1heads)
1
|

introduction to model comparison 107
• P(H data=1heads)
2
|
5 Applythisrecipeforthecaseofobserving3headsinarow.



5 Applications of Model Comparison
Thischapterpresentsseveralapplicationsofthemodelcomparison
conceptsintroducedinChapter4(IntroductiontoModelComparison).
5.1 Disease Testing
Let’simaginethereisarare,oneinamillion,diseasethatislethal
butdoesnothavemanyoutwardsymptomsatfirst. Anewtest
boasts99.9%accuracy,soyougotogettested,andreceivethebad
newsthatyoutestpositiveforthedisease. Shouldyoubedevastated
bythenews? Whatistheprobabilitythatyouactuallyhavethedis-
ease? Wearelookingattwo,quitedifferent,probabilitieshere. Inthe
firstcase,wehavetheclaimsofthetestwhichstatethatifyouhavethe
disease,theprobabilitythatthetestwillbepositiveis0.999,or,ifyouhave
thedisease,testwilldiscoverthatfact99.9%ofthetime. Inthesecond
casewehaveyourconcernwhichis,ifyoutestpositiveforthetest,what
istheprobabilitythatyouhavethedisease. Inournotationthisis:
P(positivetest disease) = 0.999(claimfromtest)
|
P(disease positivetest) = ? (yourconcern)
|
ThesetwoarerelatedbyBayes’Rule(Equation1.14).
TheBayes’Recipeproceedsasfollows
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
Themodelswehavearesimply“havethedisease”and“don’t
havethedisease”. Thepriorprobabilitiesforthesetwocomefrom
theprevalenceofthediseaseinthepopulation,beforeyouget
tested. Sincethisisa“oneinamillion”disease,wehave
1
P(disease) =
1,000,000
999,999
P(nodisease) =
1,000,000
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered

110 statistical inference for everyone
ThetopofBayes’Rulecomesdownto,giventhetruthofthe
model(i.e. eitherwithorwithoutthedisease),whatistheproba-
bilityofgettingthedata(i.e. thepositiveornegativetestresult).
Thisismeasuredbyhowgoodthetestis. Inmanymedicalapplica-
tions,thefalsepositiverate
(P(positivetestnodisease))isnot
|
alwaysequaltothefalsenegative
P(positivetest disease) = 0.999 rate(P(negativetestdisease)),soto
| saythatatestis99.9% | accurateis
and actuallyincomplete-oneneedsto
specifybothratesofeffectiveness.
Inthiscase,weareassumingthat
P(positivetest nodisease) = 0.001
| theyarethesame.
SothetopofBayes’Rulelooksforbothmodelslookslike:
P(disease positivetest) P(positivetest disease) P(disease)
| ∼ | ×
1
0.999 =9.99 10− 7
∼ × 1,000,000 ·
P(nodisease positivetest) P(positivetest nodisease) P(nodisease)
| ∼ | ×
999,999
0.001 =9.99 10− 4
∼ × 1,000,000 ·
3 Addthesevaluesforallmodels
K =9.99 10− 7+9.99 10− 4 =0.000999999
· ·
4 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
9.99 10 7
P(disease positivetest) = · − =0.1%
| 0.000999999
P(nodisease positivetest) = 99.9%
|
Whichmeansthat,overwhelmingly,ifyouhavearareone-in-a-
milliondisease,youareveryunlikelytohaveitevengivena99.9%
accuratepositivetestforit! Thisisaseriouslyunintuitiveresult,soitis
helpfultovisualizeitinanotherwaytobuildyourintuition.
Onewaytoseethisresultistovisualizeit,asinFigure5.1. Here,
thenumbersareabitsmaller-thediseaseis1outof200inapopu-
lationof3000,andthetestis99%accurate. Thismeansabout15sick
peopleandabout2985healthypeople. Ifallofthesickpeopletest
positive,and1%ofthehealthypeopletestpositiveduetothe99%
accuracy,wewouldhave15sickand29healthypeoplewhoalltest
positive. Eveninthiscase,withmuchsmallernumbers,weseethat
gettingapositivetestalonedoesnotimplythatitislikelyyouhave
thedisease. Itdependsontherarityofthedisease(themorerare,the

applications of model comparison 111
lesslikely)andthefalsepositiverate(thenumberofhealthypeople
whotestpositiveanyway). Thiswillvarydependingonthedisease
andthetest,butcanleadtothisunintuitiveresult,andthuscanlead
onetomakepoormedicaldecisions.
Has the Disease
Test Positive
Figure5.1:Rarediseaseandtesting.
Shownisapopulationof3000
where1inevery200peoplehave
thedisease(largecircles).Atest
Consequences
whichis99%effectiveisapplied
toeveryoneinthepopulation,and
Thissortofdiseasetestinghasseriousconsequences,especiallyfor
thepositivetestresults(i.e.the
rarediseaseswithteststhataren’tprecise. Inthebook“TheTheory testsaysthatyouhavethedisease)
areshownasksmallblackdots.
ThatWouldNotDie: HowBayes’RuleCrackedtheEnigmaCode,
Noticethatalthoughnearlyallof
HuntedDownRussianSubmarines,andEmergedTriumphantfrom thosethathavethediseasetest
TwoCenturiesofControversy”bySharonMcGraynethereisadis- positive(asmallblackdotinside
alargecircle),therearemany
cussionconcerningthe2009advicefromtheU.S.governmenttask
falsepositives(blackdotinan
forcethat“mostwomenintheirfortiesnottohaveannualmammo- emptysquare)-healthypeople
thattestpositiveforthedisease.
grams.” (emphasismine)AccordingtoMcGrayne,
Eventhoughthetestisquitegood,
therearemanymorehealthypeople
Thustheprobabilitythatawomanwhotestspositivehasbreastcancer and1outof100ofthemwill
isonly3%. Shehas97chancesoutof100tobediseasefree. Noneof erroneouslytestpositive.
thisisstatic. Eachtimemoreresearchdatabecomeavailable,Bayes’
ruleshouldberecalculated. AsfarasBayesisconcerned,universal
screeningforadiseasethataffectsonly4/10of1%ofthepopulation
maysubjectmanyhealthywomentoneedlessworryandtoadditionaltreat-
mentwhichinturncancauseitsownmedicalproblems. Inaddition,the
moneyspentonuniversalscreeningcouldpotentiallybeusedforother
worthwhileprojects. ThusBayeshighlightstheimportanceofimprov-


[TABLE]




Ha | s | t | h | e | D | is | e | as | e



T | e | s | t | Po | s | iti | v | e












































































112 statistical inference for everyone
ingbreastcancerscreeningtechniquesandreducingthenumberof
1
falsepositives. (emphasismine) 1SharonMcGrayne. TheTheory
ThatWouldNotDie:HowBayes’
Thustheproperapplicationofprobabilitytheoryallowsusto RuleCrackedtheEnigmaCode,
separatetruebutunintuitivethingsfromthiswhichonlyseemtrue HuntedDownRussianSubmarines,
andEmergedTriumphantfromTwo
andintuitivebutareinfactfalse.
CenturiesofControversy. Yale
UniversityPress,2011. ISBN
0300169698
5.2 M&M’s
FromvarioussourcesIhavefoundthefractionofchocolateM&Ms
candiesarered. Thesourcesfoundarethefollowing:
• SourceA:28%ofM&Msarered,20%ofM&Msareorange.
• SourceB:20%ofM&Msarered,10%ofM&Msareorange
• SourceC:13%ofM&Msarered,21%ofM&Msareorange.
FromactuallycountingofabagofM&MsIfoundthefollowing
data:
• 3redM&Msin17total(R =3,N =17)
Thequestionis,whichsourcecanwetrustthemost? Herewefollow
Bayes’recipe,
• Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(A) = P(B) = P(C) =1/3
• WritethetopofBayes’Rule(i.e. likelihood prior)forallmodels
×
beingconsidered
(cid:32) (cid:33)
17 1
P(A R =3,N =17) 0.283(1 0.28)17 − 3
| ∼ 3 − × 3
(cid:32) (cid:33)
17 1
P(B R =3,N =17) 0.203(1 0.20)17 − 3
| ∼ 3 − × 3
(cid:32) (cid:33)
17 1
P(C R =3,N =17) 0.133(1 0.13)17 − 3
| ∼ 3 − × 3
• Addthesevaluesforallmodels,toget K
P(A R =3,N =17) 0.05006
| ∼
+
P(B R =3,N =17) 0.07975
| ∼
+
P(C R =3,N =17) 0.07087
| ∼
K = 0.20068

applications of model comparison 113
• Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
P(A R =3,N =17) = 0.05006/0.20068=0.250
|
P(B R =3,N =17) = 0.07975/0.20068=0.397
|
P(C R =3,N =17) = 0.07087/0.20068=0.353
|
SowearemostconfidentinSourceB,althoughnoneofthem
reallychangedbyalot-thereisnoclearwinner.
Updating with other data
• 5orangeM&Msin16total(G =5,N =16)
Again,wefollowthesamerecipe,startingwithoutposteriorprob-
abilitiesfromaboveasourstartingpriorprobabilities-theyareprior
tothenewdata.
• Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(A olddata) = 0.250
|
P(B olddata) = 0.07975/0.20068=0.397
|
P(C olddata) = 0.07087/0.20068=0.353
|
• WritethetopofBayes’Rule(i.e. likelihood prior)forallmodels
×
beingconsidered
(cid:32) (cid:33)
16
P(A G =5,N =16andolddata) 0.205(1 0.20)16 − 5 0.250
| ∼ 5 − ×
(cid:32) (cid:33)
16
P(B G =5,N =16andolddata) 0.105(1 0.10)16 − 5 0.397
| ∼ 5 − ×
(cid:32) (cid:33)
16
P(C G =5,N =16andolddata) 0.215(1 0.21)16 − 5 0.353
| ∼ 5 − ×
• Addthesevaluesforallmodels,toget K
P(A data) 0.0300
| ∼
+
P(B data) 0.00544
| ∼
+
P(C data) 0.0471
| ∼
K = 0.08254

114 statistical inference for everyone
• Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
P(A data) = 0.0300/0.08254=0.363
|
P(B data) 0.00544/0.08254=0.0659
| ∼
P(C data) 0.0471/0.08254=0.5706
| ∼
Giventhisnewdata,weupdateourstateofknowledge,andwe’re
muchmoreconfidentthatSourceCisthebestone. Itisclearthat
SourceBisunlikely,withaprobabilityofonlyabout6.5%. Wecould
extendthisexamplewithmoredata,andmoremodelsifwe’dlike.
5.3 Psychic Octopi
2
TherewasaGermanoctopusnamedPaul whowasclaimedtobe 2Paultheoctopus,July2012. URL
psychicduringhislifetime. Hewasgiventhisdesignationbecause http://en.wikipedia.org/wiki/
Psychic_octopus
hewassupposedlyabletopicktheresultofWorldCupmatches
beforetheyoccurred 3 . Hisimpressiveresults,across2years,shown 3ThebasicprocedureforPaulto
inFigure5.2canbesummarizedasfollows: makea“prediction”wasforhis
trainerstopresenttwofooddishes,
labeledwithaflagrepresenting
thetwocountries,respectively,
data 12outof14correctlypredicted competing.Whicheverfooddish
≡ Paulchosefirstwashisprediction
forthewinnerofthegame.
Thequestionwehavetoaskis,isthisdatastrongevidencefora
psychicoctopus? Inordertohaveawell-posedproblemweneedthe
followingthreecomponents:
1 asetofhypotheses,ormodels,tocompare-weneedatleasttwo,
otherwisethequestionismeaningless
2 foreachmodel,anequationdenotingthelikelihood,orinother
words,howprobableisthedatagiventheparticularmodel
3 aspecificationofthepriorprobability,orinotherwords,how
likelywasourmodelbeforewesawthedata
Making a Well Posed Problem
Weareinterestedintheprobabilityofthisoctopusbeingpsychic,
giventhisdata,or
P(psychic data)
|
whichreallyisanexampleofamodelcomparison,orhypothesis
testing. Inanykindofmodelcomparison,weneedtohavemultiple

applications of model comparison 115
Figure5.2:Thefullresults
ofthepredictionsofPaul
theOctopus,reproducedfrom
en.wikipedia.org/wiki/Psychic_octopus.
modelstocomparetoinordertoproceed. Themodelsweconsider
constraintheproblem,anddefinewhichideaswearewillingto
consider. Tobespecific,asafirststep,let’sconsiderthefollowing
twomodels
H := Paulispsychic
{ }
R := Pauliscompletelyrandom,likeacoinflip
{ }
Thenextstepistobeabletoassignprobabilitiesfromthesemod-
els. Itiseasyfortherandomhypothesis
P(correctprediction R) = 0.5
|
P(incorrectprediction R) = 0.5
|
Whatdoesitmeantobepsychic? Whatistheprobabilityofget-
4
tingacorrectresultifyouarepsychic? AccordingtoJamesRandi 4J.Randi. Flim-flam!:psychics,ESP,
manyofthepsychicsanddowsersclaim100%accuracyintheirpre- unicorns,andotherdelusions,volume
342. PrometheusBooksAmherst,
dictionsbeforetheyaretested. Howeverthiswouldmeanasingle NY,1982
wronganswerwoulddrivetheprobabilityofthatmodeltozero: a
perfectpredictorcannot,logically,makeanymistakes. Forourcase
here,wechoosetobegeneroustothepsychicandallowforareason-
ablefailurerate,using90%asouraccuracy,thus
P(correctprediction H) = 0.9
|
P(incorrectprediction H) = 0.1
|

116 statistical inference for everyone
Specifyingthepriorprobabilityofthesetwomodelsisabitmore
challenging. Itseemsreasonabletoassignasmallpriorprobabilityto
apsychicoctopus-howmanypsychicoctopihaveyoueverencoun-
tered? Asmall,butstillquiteconservativevalue,wouldbe1/100,so
wehaveforthetwomodels: Itispossiblethatwecouldbe
accusedofananti-psychicbias
P(H) = 1/100 here,especiallyfromsomeonewho
isatruebeliever.Whyshouldn’t
P(R) = 99/100
thepriorbeP(H) = 1/2?Ifyou
hadnoworldexperience,thatis
whatyou’dstartwith,butthenthe
The First Model Comparison
behaviorofthefirstoctopithatyou
encounterwouldgenerallylower
Nowthatwe’vesetuptheproblem,wecanapplytheBayes’Recipe
yourassignmentoftheprobability
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered ofthenextoctopibeingpsychic.
Afterenoughworldexperience,
P(H) = 1/100 updatingyourprobabilitywith
Bayes’Rule,you’darriveatavery
P(R) = 99/100 smallpriorforPaul,thecurrent
octopusweareexamining.
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(H data=12outof14) P(data=12outof14 H)P(H)
| ∼ |
P(R data=12outof14) P(data=12outof14 R)P(R)
| ∼ |
whereweareusingthesymbol todenoteproportionalityorre-
∼
latedto. Essentially,bycalculatingthetopofBayes’Rulefirst,the
numbersarenotequaltothefinal(i.e. posterior)probabilitiesbut
mustberescaledtomakesurethattheyaddupto1. Thisisdone
inthefinalstep. Upuntilthatrescaling,weusethesymbol and
∼
thinkofitasrelatedto.
3 Putinthelikelihoodandpriorvalues
(cid:32) (cid:33)
14 1
P(H data=12outof14) 0.9120.114
−
12
| ∼ 12 × 100
= 0.00257
(cid:32) (cid:33)
14 99
P(R data=12outof14) 0.5120.514
−
12
| ∼ 12 × 100
= 0.00549
4 Addthesevaluesforallmodels
K =0.00257+0.00549=0.00806
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
0.00257
P(H data) = =0.32
| 0.00806
0.00549
P(R data) = =0.68
| 0.00806

applications of model comparison 117
andthepsychicloses! Wecontinuethisproblemdiscussingthepo-
tentialanti-psychicbiasinthepresentationoftheproblem.
Furthering the Comparison
Typically,apersonwhoissupportiveofpsychicphenomenawould
chooseapriorforourpsychichypothesis(H)thatwouldbeatleast
aslargeasthepriorfortherandomhypothesis(R). Inthiscase,the
(posterior)probabilityoftheoctopusbeingpsychicgiventhedata
of12correctoutof14wouldbemuchhigher. After“rulingout”the
randomoctopushypothesis,we’dbeleftwithpsychic. Butisthatall
thatisreallyleft? No,andtheanalysisiseasytodo.
OncepresentedwiththesuccessofPaul,mostpeopleinstantly
aresuspiciousofrandomoctopus,butdon’tadoptpsychicoctopus
astheanswer. Perhapsthekeepers,beingGerman,biasedthedata
takingalittlebit. Perhapstheoctopuschoseflagswithbrightyellow
stripes. Noticethateachofthesecasesstillresultsinsimilardata-
theoctopuswouldhavegotten11or12outof14,butthepriorprob-
abilityofthesecasesshouldbemuchhigherthanpsychic,evenif
lowerthanrandom. Weleaveitasanexercisetoperformthecalcula-
tioninthiscase,butitisdirectlyparalleltotheNinesdeckexample
ofSection4.2onpage102.
5.4 Monty Hall Problem
ThisproblemwasintroducedinSection2.6.
Example5.1 Isitbettertoswitchdoors? -MontyHallProblemrevisited
Youmayrecallthatwewerepresentedwithachoiceof3doors
whereacarisbehindoneandgoatsbehindtheothers. Having
pickedone,thehostopensupadoorwithagoat,andoffersyou
theopportunitytochangeyouranswer. Inordertoassesstheproba-
bilities,wemustrememberthat
1 thehostneveropensyourdoor
2 thehostalwaysopensadoorwithagoat
We’llgothroughaspecificexample,thatofyouchoosingdoor1
andthehostopeningdoor2. Theanalysisproceedsinidenticalways
fortheotherpossibilities. WeapplytheBayes’Recipe,wherethe
modelsunderconsiderationare
• “carbehinddoor1”
• “carbehinddoor2”

118 statistical inference for everyone
• “carbehinddoor3”
TheBayes’Recipeproceedsasfollows
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
P(car1 you1) = 0.333
|
P(car2 you1) = 0.333
|
P(car3 you1) = 0.333
|
where,forexample, P(car1 you1) representstheprobabilitythat
|
thedoorcontainsthecargiventhatyouchosedoor1. Sinceyour
choiceofdoordoesn’taddanyinformationaboutthelocationof
thecar,alloftheprobabilitiesareequal.
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
P(car1 you1,host2) P(host2 you1,car1)P(car1 you1)
| ∼ | |
P(car2 you1,host2) P(host2 you1,car2)P(car2 you1)
| ∼ | |
P(car3 you1,host2) P(host2 you1,car3)P(car3 you1)
| ∼ | |
3 Putinthelikelihoodandpriorvalues
Duetherestrictionsonthehostabove,thehostcannotopena
doorwithacar,so P(host2 you1,car2) = 0. Inthecasewhere
|
youchoosedoor1andthecarisalsobehinddoor,thehosthasthe
freedomtochooseeitherdoor2ordoor3,so P(host2 you1,car1) =
|
0.5. Wheretheinformationcomesiniswhenthecarisbehind
door3andyou’vechosendoor1. Inthatcase,thehostcannot
openyourdoor(door1)orthedoorwiththecar(door3)andmust
opendoor2. Thus, P(host2 you1,car3) =1.
|
Thefinalresultofthisstepis
P(car1 you1,host2) 0.5 0.333
| ∼ ·
P(car2 you1,host2) 0 0.333
| ∼ ·
P(car3 you1,host2) 1 0.333
| ∼ ·
4 Addthesevaluesforallmodels
K =0.5 0.333+1 0.333=0.5
· ·
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
0.5 0.333
P(car1 you1,host2) = · =0.333
| 0.5
0 0.333
P(car2 you1,host2) = · =0
| 0.5
1 0.333
P(car3 you1,host2) = · =0.666
| 0.5

applications of model comparison 119
Thus,inthecase,giventhatyouchoosedoor1andthehost
chooses2,theprobabilitythatthecarisbehinddoor1(yourdoor)
is0.333andtheotherdoor(door3)is0.666. Followingthesamesteps
throughtheothercases,wegetinsummary
Probabilityof...
YourChoice HostChoice CarBehind1 CarBehind2 CarBehind3
1 1 (hostcan’topenyourdoor)
1 2 0.333 0 0.666
1 3 0.333 0.666 0
2 1 0 0.333 0.666
2 2 (hostcan’topenyourdoor)
2 3 0.666 0.333 0
3 1 0 0.666 0.333
3 2 0.666 0 0.333
3 3 (hostcan’topenyourdoor)
Insummary,itisalwaysbettertoswitchtotheremainingdoor,
giventheserules.



6 Introduction to Parameter Estimation
Wewillintroducetheideaofwhatiscalledparameterestimationusing
asimplesystemofbentcoins. Thiswillgeneralizetomorecomplex
models,andformthebasisformuchofstatisticalinference.
6.1 Bent Coins
Imaginewehaveaseriesofcoinsbentbyvariousamounts(Fig-
ure6.1). Ifthecoinisbentcompletelyinhalf,thenwecouldhavethe
coinalwaysflipheads(i.e. P(heads) = 1)ortails(i.e. P(tails) = 1) Figure6.1:BentCoins
dependingonhowitisbent. Ifyoudon’tbendthecoinatallthen
we’dhaveafaircoin(P(heads) = P(tails) = 0.5). So,let’ssay Whydowenumberthemfromzero
thatwehaveacollectionofbentcoinswhicharebentbydifferent here?It’ssothatthenumberofthe
coin,saynumber7,corresponds
amounts. Forconveniencewewillnumberthemfrom0to10. The
theprobabilitythatthatcoinflips
Table6.1summarizestheprobabilityofeachcoinflippingheads. heads,P(heads)=0.7
CoinNumber ProbabilityforFlippingHeads(P(heads)) Table6.1:Probabilitiesforflipping
headsgivenacollectionofbent
0 0.0
coins
1 0.1
2 0.2
3 0.3
4 0.4
5 0.5
6 0.6
7 0.7
8 0.8
9 0.9
10 1.0
1
NowIhavethefollowingscenario ,withafewquestions. 1D.V.LindleyandL.D.Phillips.
Inferenceforabernoulliprocess
ImagineIhavetakenarandomcoinfrommycollection,flippeditand (abayesianview). TheAmerican
observedthefollowingdata: Statistician,30(3):112–119,1976
TTTHTHTTTTTH(i.e. 9tailsand3heads)
1 Fromthisdata,whichcoindoImostlikelyhave?

122 statistical inference for everyone
2 Canwebesignificantlyconfidentthatthisparticularcoinwillresult
inmoretailsthanheadsinthefuture?
Thewaywe’vesetupthisproblemisexactlylikethemodelcom-
parisonexamplewiththeHighandLowDeck(Section4.1),exceptin
thiscasewehave11models(oneforeachcoin). ApplyingtheBayes’
Recipewehave
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered.
Givennofurtherinformation,weselectauniformdistributionfor
theprior(i.e. allmodelsareinitiallyequallyprobable):
P(M ) = 1/11
0
P(M ) = 1/11
1
.
.
.
P(M ) = 1/11.
10
where M isthemodeldefinedby“we’reflippingcoin0,” M is
0 1
themodeldefinedby“we’reflippingcoin1,”etc...
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered:
P(M data=9T,3H) P(data=9T,3H M )P(M )
0 0 0
| ∼ |
P(M data=9T,3H) P(data=9T,3H M )P(M )
1 1 1
| ∼ |
.
.
.
P(M data=9T,3H) P(data=9T,3H M )P(M ).
10 10 10
| ∼ |
3 Putinthelikelihoodandpriorvalues. Herewearedrawingfrom
abinomialdistributionforthelikelihood:
(cid:32) (cid:33)
12
P(M data=9T,3H) 0.03 (1 0.0)9 1/11
0
| ∼ 3 × − ×
(cid:32) (cid:33)
12
P(M data=9T,3H) 0.13 (1 0.1)9 1/11
1
| ∼ 3 × − ×
.
.
.
(cid:32) (cid:33)
12
P(M data=9T,3H) 1.03 (1 1.0)9 1/11.
10
| ∼ 3 × − ×
4 Addthesevaluesforallmodels: seeTable6.2.
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties: seeTable6.2.
Whenwearedealingwiththismanymodels,itiseasiertoplotthe
results,showninFigure6.2. Wearenowinapositiontoaddressthe
questionsposedatthebeginningofthesection.

introduction to parameter estimation 123
Model P(M
i
data=9T,3H) P(M
i
data=9T,3H)/K Table6.2:Probabilityfordifferent
∼ | ∼ | bent-coinmodels,giventhedata=9
M 0 0.000 0.000 tails,3heads.Themiddlecolumn
M 0.00774 0.110 isthenon-normalizedvaluefrom
1
M 0.0214 0.306 Bayes’Rule,needingtobedivided
2 byK(thesumofthemiddlecol-
M 3 0.0217 0.310 umn)togetthefinalcolumnwhich
M 0.0128 0.184 istheactualprobability.
4
M 0.00488 0.0696
5
M 0.00113 0.0161
6
M 0.000135 0.00192
7
M 0.00000524 0.0000748
8
M 0.0000000145 0.000000208
9
M 0.000 0.000
10
K=0.0700
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 9 10
Model Number
)}H3,T9{=atad|ledom(P
Figure6.2:Probabilityfordifferent
bent-coinmodels,giventhedata=9
tails,3heads.


[TABLE]



















124 statistical inference for everyone
1 Fromthisdata,whichcoindoImostlikelyhave?
Themaximumprobabilityisforcoin3,butcoin2isaclosesec-
ond. Thuswecanbereasonablyconfidentthatwehavebeenflip-
pingoneofthosetwocoins,butcan’tnarrowourconfidenceany
morethanthat.
2 Canwebesignificantlyconfidentthatthisparticularcoinwillresult
inmoretailsthanheadsinthefuture?
Thisisanotherwayofaskingforthetotalprobabilityforcoinsless
thancoin5(thefaircoin),or
P(coin0orcoin1orcoin2orcoin3orcoin4) =
0.000+0.110+0.306+0.310+0.184=0.912
whichsaysthatthiscoinis“likely”to“verylikely”(Table1.1on
page51)tohaveaprobabilityofyieldingheadslessthanafair
coin,andthusyieldmoretailsinthefuture.
6.2 Priors versus Data
Itisinstructivetopauseandlookatthisexampleoneflipatatime,
toseehowtheprobabilityandthusourstateofknowledgeadjusts
aswecollectmoredata. InFigure6.3weseetheresultofourproce-
durewhenthereisnodata(i.e. ourinitial,priorprobabilities)and
whenwe’veflippedonceandthenagain,bothtimestails. Thecurve
for“nodata”isthesameasthepriorprobability,andinthiscaseall
modelsareequallylikely. Whenthefirsttailsisobserved,themodel
whichstatesthatheadsarecertain(i.e. coin10)goestozeroproba-
bilitybecausecoin10cannotfliptails. 2 . Atthispointweknowthatit 2Noticethattheonlymodelswith
isimpossibleforustobeflippingcoin10. Weseealsothatthehigh- probabilityequaltozeroareones
thatarelogicallyimpossible.It’snot
numberedcoins(i.e. theoneswithhighprobabilityofflippingheads)
thecolloquialusageofimpossible,
havegreatlyreducedprobabilitywhilewe’veseenonlytails. asin“itisimpossiblefortheRed
Soxtowinthisyear,”butinthe
Asmoretailsareobserved,theprobabilityforthelowermodels
strictusage,asin“itisimpossible
isincreased. Asweflipmoretailswebecomemoreconfidentinthe toflipbothheadsandtailsatthe
lower-numbermodels. Becauseatthispointwehaven’tflippedany sametime.”Thereasonthisis
thecaseisthatastatementwith
heads,themodel0stillhasnon-zeroprobability-itisstillpossible
zeroprobabilitycannotbemade
thatweareholdingacointhatcannotflipheads. possiblewithanyaboutofdata-itis
Whenwecontinuewiththenextfewflips(Figure6.4)ween- anutterlydogmaticstatement.Thus,
wereserveitonlyforthingsthatare
counterourfirstheadsonthefourthflip. Atthispointthemodel logicallyimpossible.
whichstatesthatheadsareimpossible(i.ecoin0)goestozeroproba-
bility. Finally,acrossourentiredataset(Figure6.5)weseethatthe
curvegetsnarrower,wheremoreoftheprobabilityfallsononlya
fewofthemodelsandtheothermodelsbecomelessandlesslikely.
Withonly12datapoints,thereisstillalotofuncertaintyinwhich

introduction to parameter estimation 125
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 910
Model Number
)atad|ledom(P
data={} data={T} data={TT}
0.35 0.35
0.30 0.30
0.25 0.25
0.20 0.20
0.15 0.15
0.10 0.10
0.05 0.05
0.00 0.00
0 1 2 3 4 5 6 7 8 910 0 1 2 3 4 5 6 7 8 910
Model Number Model Number
Figure6.3:Probabilityfordifferent
bent-coinmodels,givennodata
model-severalmodelshavereasonablyhighprobabilityvalues. We (left),thefirsttails(middle),and
stillcanruleoutafewmodelsconfidently(likecoins0,6,7,8,9,and thesecondtails(right).Thecurve
fornodataisthesameastheprior
10). Wearemostconfidentincoins2and3,withthemostprobabil-
probability,andinthiscaseall
modelsareequallylikely.When
ity.
thefirsttailsisobserved,themodel
whichstatesthatheadsarecertain
(coin10)goestozeroprobability.
Asmoretailsareobserved,the
probabilityforthelowermodelsis
increased.
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 910
Model Number
)atad|ledom(P
data={TTT} data={TTTH} data={TTTHT}
0.35 0.35
0.30 0.30
0.25 0.25
0.20 0.20
0.15 0.15
0.10 0.10
0.05 0.05
0.00 0.00
0 1 2 3 4 5 6 7 8 910 0 1 2 3 4 5 6 7 8 910
Model Number Model Number
Figure6.4:Probabilityfordifferent
bent-coinmodels,giventhreetails
(left),thefirstheads(middle),and
anothertails(right).Whenthefirst
6.3 Moving Toward the Continuous
headsisobserved,themodelwhich
statesthatheadsareimpossible(coin
Thereisapracticalproblemthatwefaceatthispoint,whenwe 0)goestozeroprobability.
consideragenericbentcoin. Perhapsitdoesn’tfitinoneofthe11
modelsconsidered,fallingsomewhereinbetween,forexamplewith


[TABLE]






















[TABLE]




















[TABLE]




















[TABLE]




















[TABLE]




















[TABLE]



















126 statistical inference for everyone
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 1 2 3 4 5 6 7 8 910
Model Number
)atad|ledom(P
data={} data={TTTHTH} data={TTTHTHTTTTTH}
0.35 0.35
0.30 0.30
0.25 0.25
0.20 0.20
0.15 0.15
0.10 0.10
0.05 0.05
0.00 0.00
0 1 2 3 4 5 6 7 8 910 0 1 2 3 4 5 6 7 8 910
Model Number Model Number
Figure6.5:Probabilityfordifferent
bent-coinmodels,givennodata
P(heads) = 0.132464. Ones’firstthoughtmightbetoincludeone (left),thefirsthalfofthedataset
thousandcoinsoronemillioncoinsinsteadofthe11we’veconsid- (
9
m
ta
id
il
d
s
l
a
e
n
),
d
an
3
d
he
th
ad
e
s
en
(r
t
i
i
g
re
ht
d
).
atasetof
eredsofar,sowecouldhavecoin132464,coin132465,coin132466,
etc... Althoughthiscanbedone,werunintotwoproblems
1 Becausewearedealingwithsomanymodels,theprobability
associatedwithanysinglemodelgetsverysmall-andgetssmaller
withthemoremodelsyouconsider
2 Wecan’tpracticallydistinguishbetweenmodelssuchas P(heads) =
0.132464and P(heads) =0.132465 (thelastdigitisdifferenthere)
Inordertosolvebothoftheseproblemsmathematically,wein-
troducetheconceptofacontinuousdistribution. Westartbylabeling
themodelwithacontinuousnumberratherthananinteger. Inour
presentcaseitmakessensetolabelthemodelwiththeprobability
thatthecoinflipsheads. We’llcallthislabel θ,anditwillhavea
valuebetween0(headsareimpossible)and1(headsarecertain)and
cantakeonanyvalueinbetween. Becausewenowhaveaninfinite
numberoflabels,wehavetwoconsequences:
1 Wecan’tsimplyaddupalltheprobabilitiestogetourvalueof K
tomakeeverythingaddupto1. Instead,welookatareasunderthe
curveandmakesuretheentireareaequals1.
2 Because,withdistributions,areasunderthecurve(andnotthe
valuesofthedistributionitself)aretheprobabilities,wecan
onlyspeakaboutrangesofvalues. Forexample,wecanspeak
meaningfullyabouttheprobabilityof θ between0.3and0.4(i.e.
P(0.3 < θ < 0.4)). Whenwewritedownsomethinglike P(θ) = 1
we’renottalkingaboutaprobabilityofasinglelabelbutrather
themagnitudeofthedistributionatthatlabel, θ.


[TABLE]






















[TABLE]




















[TABLE]



















introduction to parameter estimation 127
WerevisitBayes’Recipeagain,usingthedistributions. Thistime
wealsowilllookatpicturesofthedistributionsasweprogress.
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered:
1.0
0.8
P(θ) =1.
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
θ
)θ(P
=
1
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered: Area
Under
Curve
Wecanwriteoneequationforallofthemodelslabeledby θ at
onceas
P(θ data=9T,3H) P(data=9T,3H θ)P(θ).
| ∼ |
3 Putinthelikelihoodandpriorvalues.
Weusethebinomialmodel,oneequationforallmodels,remem-
beringthatforamodellabeledby θ theprobabilityforthatcoin
flippingheadsis P(heads) = θ. Thuswegetthelikelihoodand
priorvaluesas
P(θ data) P(data θ) P(θ)
| ∼ | ·
(cid:32) (cid:33)
12 0.25
P(θ data9T,3H) θ3 (1 θ)9 1 | ∼ 3 × − · 0.20
0.15
0.10
0.05
0.00 0.0 0.2 0.4 0.6 0.8 1.0
θ
)H3,T9=atadθ(P
|
∼
“
'
4 Findtheareaunderthiscurve,andcallit K.
Area
Under
Curve
NOT
1
5 Divideeachofthevaluesofthecurvebythisare, K,togetthe
finalprobabilitieswheretheareaunderthecurveis1.
3.5
3.0
2.5
2.0
1.5
1.0
0.5
0.0
0.0 0.2 0.4 0.6 0.8 1.0
θ
)H3,T9=atadθ(P
|
“
'
Usuallythesestepsaredoneforyou,foraspecificdataset,and
youaregiventhefinalposteriordistributiontouseinanswering
a
k
m
n
n
o
y
o
d
w
q
e
u
l
w
e
p
s
h
a
t
a
r
i
a
o
t
m
n
a
s
s
e
.
s
t
u
H
er
m
o
s.
w
pt
e
io
ve
n
r
s
,
h
fo
a
r
ve
an
b
y
ee
p
n
ar
m
ti
a
cu
d
l
e
ar
in
ca
th
se
e
i
c
t
h
i
o
s
ic
im
e
p
of
or
m
ta
o
n
d
t
e
t
l
o
sand
Area
Under
Curve=1
6.4 MAP and Areas
NowwerevisitthequestionsposedinSection6.1onpage121about
thebentcoin,thistimeusingthedistributionfoundabove,repro-
ducedhereinFigure6.6.
ImagineIhavetakenarandomcoinfrommycollection,flippeditand
gotthefollowingdata:
TTTHTHTTTTTH(i.e. 9tailsand3heads)


[TABLE]






r | 1
=
ve

Cu
der

Area | Un









[TABLE]






1
OT

Curve | N

Under

Area





[TABLE]








=1

Curve

Und | er

Area






128 statistical inference for everyone
1 Fromthisdata,which“coin”doImostlikelyhave? (orinthis
interpretation,whatismybestestimatefortheprobabilityofthis
coinflippingheads,denotedbyθ)
2 Canwebesignificantlyconfidentthatthisparticularcoinwillresult
inmoretailsthanheadsinthefuture?
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
Figure6.6:Posteriorprobability
3 heads and 9 tails distributionfortheθvaluesof
thebentcoin-theprobability
thatthecoinwilllandheads.The
maximum probability distributionisshownfordata3
headsand9tails,withamaximum
atθ=0.25.
Oneanswertothefirstquestioncanbeaccomplishedbylooking
atthemaximumoftheposteriordistribution,showninFigure6.6. 3 3Themaximumoftheposteriordis-
Byeye,itseemstohaveamaximumat θ = 0.25. Infactonecan tribution,whichrepresentsthemost
likelyvalueofaquantity,isoften
demonstratethatthisdistributionhasamaximumat
referredtoastheMAPestimate.It
isalsocommonlyreferredtoasthe
θ = numberofsuccesses , modeofthedistribution.
max
totalnumberofattempts
4
whereinourexample,asuccessishead,andanattemptisaflip. 4Thisdistribution,givenhow
Wetakeupthisquestionofthebestestimateof θ,giventheposterior commonitis,isgiventhenameBeta
distribution.Thereareahandful
probabilityfor θ,inmoredetailinSection6.6.
ofcommondistributionsthatare
Theanswertothesecondquestioncanbedonebylookingat givennamesforconvenience.We’ve
alreadyseentheuniformdistribution,
theareaunderthecurvefrom θ = 0,the“allheads”coin,to θ =
andtherewillbeothers.
0.5,the“fair”coin,asshowninFigure6.7. Thisarearepresentsthe
probability,giventhedata,thatthecoinisskewedtowardsheads
or,inotherwords,howconfidentarewethatthisisanunfaircoin.
Giventhevalueof P(θ < 0.5) = 0.954wecansaythatthisis“very
likely”anunfaircoin(seeTable1.1onpage51).


[TABLE]




ma | xim | um p | roba | bility












introduction to parameter estimation 129
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
Figure6.7:Posteriorprobability
3 heads and 9 tails distributionfortheθvaluesof
thebentcoin-theprobability
thatthecoinwilllandheads.The
distributionisshownfordata3
headsand9tails.Theareaunder
thecurvefromθ = 0(the“all
heads”coin)toθ =0.5(the“fair”
coin)is0.954.
area=0.954
6.5 Quartiles
Giventhatwearedealingmostoftenwithcontinuousdistributions,
andthusneedtolookatareasunderthecurvefromonepointto
another,itisusefultomakeatableforadistributionoftheseareas.
Typicallywelookatthevaluesoftheparameteratwhichwehavea
givenareaunderthecurvefromtheminimumpossiblevalueofthe
parameteruptotothatvalue. Forexample,wemightbeinterested
inthevalueof θ (i.e. howskewedthecoinis)suchthatwehavean
areaof50%from0upto θ,showninFigure6.8. Thispoint(called
themedian)representsthepointwherewewouldbejustasconfident
(givenourdata)thatthecoinismoreskewedthanthisaslessskewed.
Atableofthesevaluesforadistributioncanbeveryuseful. For
example,considerthetableandplotshowninFigure6.9. Shownare
thevariouspointswheretheareaunderthecurveuptothosepoints
isspecified. Forexample,theareaunderthecurvefrom θ = 0up
to θ = 0.11is5%. Thismeans,giventhedataof3headsand9tails,
thereisaprobability P = 5%ofthecoinhavinglessthan θ = 0.11,or
anextremeskewtowardstails.
QuartilesThetermquartilesreferstothevaluesoftheparameter QuartilesThetermquartilesrefers
whichresultinanareaof25%,50%,or75%,orone,two,orthree tothevaluesoftheparameter
whichresultinanareaof25%,
quartersofthearea. 50%,or75%,orone,two,orthree
Whenwewishtorefertoanon-quarterpercentage,thenwe’llcall quartersofthearea.


[TABLE]








are | a=0. | 954








130 statistical inference for everyone
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
Figure6.8:Posteriorprobability
3 heads and 9 tails distributionfortheθvaluesof
thebentcoin-theprobability
thatthecoinwilllandheads.The
distributionisshownfordata3
headsand9tails.Theareaunder
area=0.5 thecurvefromθ = 0(the“all
heads”coin)toθ=0.28is0.5-half
thearea.Thisrepresentsthemedian
ofthedistribution.
0.28
itapercentile.
PercentilesThetermpercentilereferstothevalueoftheparameter PercentilesThetermpercentile
whichresultinaparticulareareaunderthecurve. referstothevalueoftheparameter
whichresultinaparticularearea
Forexample,wecansayfromFigure6.9thatthe99%percentileis
underthecurve.
0.59. Thus,itisextremelyunlikelytohavethecoinskewedtowards
headsmorethan θ = 0.59giventheobservationthatweflipped3
headsand9tailswiththiscoin.


[TABLE]




a | rea= | 0.5





0 | .28






introduction to parameter estimation 131
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
3 heads and 9 tails
50%
25% Beta(heads=3,tails=9)
Value Area
0.07 0.01
75%
0.11 0.05
0.14 0.10
0.20 0.25
5%
0.28 0.50
0.36 0.75
95%
0.44 0.90
1%
0.49 0.95
99%
0.59 0.99
0.11 0.28 0.49
0.07 0.20 0.36 0.59
Figure6.9:Posteriorprobability
distributionfortheθvaluesof
6.6 Best Estimates thebentcoin-theprobability
thatthecoinwilllandheads.The
distributionisshownfordata3
Perhapssurprisingly,thereisnotasingleanswertothebestesti- headsand9tails.Thevarious
matefor θ giventheposterierdistribution,liketheoneshownin quartilesareshownintheplot,and
Figure6.9. Thereareseveralplausiblemeasures,eachwiththeirown summarizedintheaccompanying
table.
advantages. Anyspecificestimateofaparameter(e.g. θ)isdenoted
withahat(e.g. θˆ)inthedescriptionsthatfollow.
TheModeAlsoknownasthemaximuma-posterioriprobability TheModeAlsoknownasthemax-
(MAP)estimate,themodeisthemaximumoftheposteriorprobabil- imuma-posterioriprobability(MAP)
estimate,themodeisthemaximum
ity. InthecaseofaBetadistributionwith h successesin N trials,we
oftheposteriorprobability.
have
h
θˆ =
mode N
TheMeanAlsoknownastheexpectedvalueoraveragevalue,the TheMeanAlsoknownasthe
meanofadistributionofaparameter θ isdefinedtobethesumofall expectedvalue,themeanofadistri-
butionofaparameterθisdefined
ofthepossiblevaluesof θ timestheposteriorprobabilityof θ,
tobethesumofallofthepossi-
blevaluesofθtimestheposterior
θˆ mean = ∑ θ P(θ data) probabilityofθ,asin
× |
θ θˆ mean =∑ θ × P(θ | data)
Itisonemeasureofthemiddleofthedistribution. Inthespecialcase θ
ofaBetadistributionwith h successesin N trials,wehave Itisonemeasureofthemiddleof
thedistribution.
h+1
θˆ =
mean N+2


[TABLE]




25 | 50
% | %

5 | % | 75 | %

1 | % | 95 | %

99 | %

0. | 0.
0 | 11
7 0. | 0.
20 | 2 | 8
0. | 36 | 0. | 49
0. | 59




132 statistical inference for everyone
IntuitivelythisisthesameastheMAPoftheBetadistribution,with
onemoresuccessandonemorefailurethanactuallyobserved. Fur-
ther,fortheBetadistribution,themeanvalue θˆ representsthe
mean
predictiveprobabilityofasuccessfuleventonthenextobservation.
TheMedianAlsoknownasthe50%-percentile,themedianrep-
TheMedianAlsoknownasthe
resentsthemiddleofthedistributionsuchthattheprobabilityofthe
50%-percentile,themedianrepre-
sentsthemiddleofthedistribution
parameterbelowthemedianequaltotheprobabilityoftheparame-
suchthattheprobabilityofthe
terabovethemedian. parameterbelowthemedianequal
totheprobabilityoftheparameter
P(θ θˆ data) = P(θ θˆ data) =0.5 abovethemedian.
≤ median| ≥ median| P(θ θˆ data) = 0.5
≤ median|
P(θ θˆ data) = 0.5
≥ median|
“Assume2successesand2failures”medianapproximation For
“Assume2successesand2fail-
theBetadistributionthereisnosimpleformforthemedian,buta ures”medianapproximation For
5 theBetadistributionthereisno
decentapproximationwhichwewilluseisgivenby
simpleformforthemedian,but
adecentapproximationwhichwe
h+2
θˆ willuseisgivenby
median ≈ N+4
h+2
θˆ
IntuitivelythisisthesameastheMAPoftheBetadistribution,with median ≈ N+4
twomoresuccessesandtwomorefailuresthanactuallyobserved, Intuitivelythisisthesameasthe
MAPoftheBetadistribution,with
andisthusreferredtoasthe“Assume2successesand2failures”
twomoresuccessesandtwomore
medianapproximation. failuresthanactuallyobserved,and
isthusreferredtoasthe“Assume
Althougheachofthesehastheiradvantages,mostnotablyeaseof
2successesand2failures”median
computation(especiallyforthemodeandthemean),wewilltypi- approximation.
callyusethemedianofthedistributionasthebestestimateforthe 5AlanAgrestiandBrianCaffo.
Simpleandeffectiveconfidence
followingreasons:
intervalsforproportionsand
differencesofproportionsresult
1 themedianisintuitiveasliterallythemiddleofthedistribution
fromaddingtwosuccessesandtwo
failures. TheAmericanStatistician,54
2 themedianisnotassensitivetodistributionsthatarehighly (4):280–288,2000
asymmetric
Inmostpracticalexamplesitmaynotmakemuchdifference,and
forsomedistributions(suchastheNormaldistributiondescribedin
Chapter7(Priors,Likelihoods,andPosteriors))thereisnotdifference-
themeanisthemedianwhichisalsothemode.
Example6.1 Whatisthebestestimateoftheprobabilityofabentcoin
flippingheads,giventheobservationof9tailsand3heads?
Ifwetakethebestestimatetobethemedian,thenwehavefrom
the“assuming2successesand2failures”method,
h+2
θˆ
median ≈ N+4
5
= =0.313
16

introduction to parameter estimation 133
Noticethatthemaximumprobabilitywasatthesomewhatlower
value
h 3
θˆ = = =0.25
mode N 12
Onereasonwhythemedianisabetterestimateinthiscaseis
because,asshowninFigure6.9,thereismoreprobability(i.e. area
underthecurve)totherightofthemaximumthantotheleft,sothe
bestestimateshouldbegreaterthantheonegivenbythemode.
6.7 Uncertainty in the Best Estimates
Toquantifytheuncertaintyinthebestestimates,weneedavalue
whichrepresentsthewidthofthedistribution. LookingatFigure6.10
we’dliketoprovideaquickwayofsayingthattherangeofprobable
valuesliessomewherebetween θ = 0.2and θ = 0.5-anything
outsideofthiscontributesonlyasmallamounttotheprobability,
orinotherwords,wearemostconfidentthatourbestestimateof
θ liesbetweenthose0.2and0.5. Dependingontheapplication,the
symmetryofthedistribution,andotherpracticalfactorsonemaysee
afewpotentialmeasuresofthewidthofthedistribution.
Inter-QuantileRangeTheInter-QuantileRange(ICR)istherange Inter-QuantileRangeTheInter-
betweenthe25%and75%quartiles,andrepresents50%oftheproba- QuantileRange(ICR)istherange
betweenthe25%and75%quar-
bility. tiles,andrepresents50%ofthe
InFigure6.10,theInter-QuantileRangerangeis[0.29,0.40]. probability.
95%CredibleInterval(CI)The95%CredibleInterval(CI)isthe
95%CredibleInterval(CI)The
rangebetweenthe2.5%and97.5%quantiles,andthusrepresents 95%CredibleInterval(CI)isthe
rangebetweenthe2.5%and97.5%
95%oftheprobability. AccordingtoTable1.1onpage51,itis“very
quantiles,andthusrepresents95%
likely”thatourbestestimateliesinthisrange. oftheprobability.Accordingto
InFigure6.10,the95%CredibleIntervalisnearly[0.2,0.5].
Table1.1onpage51,itis“very
likely”thatourbestestimateliesin
thisrange.
StandardDeviationThestandarddeviationisameasureofthe StandardDeviationThestandard
half-widthofadistribution,mostcommonlyusedspecificallywith deviationisameasureofthe
half-widthofadistribution,most
referencetotheparticularNormaldistribution. Thiswillbedefined
commonlyusedspecificallywith
morepreciselyinSection7.2onpage140),andwillthusnotbede- referencetotheparticularNormal
distribution.Thiswillbedefined
finedingeneralhere.
morepreciselyinSection7.2on
AnapproximatevalueforthestandarddeviationfortheBeta page140),andwillthusnotbe
distributionis definedingeneralhere.
(cid:113)
σ θˆ(1 θˆ)/N
≈ −
FromFigure6.10,andusingthemedianasthebestestimate, θˆ,we
get
(cid:113)
σ 0.34(1 0.34)/30=0.09
≈ −

134 statistical inference for everyone
StandardDeviationtoUncertainty Toconvertthisnumbertoan StandardDeviationtoUncertainty
uncertainty,itisamathematicalconsequencethatabout65%ofthe Toconvertthisnumbertoan
uncertainty,itisamathematical
areaiswithin1valueof σ,95%oftheareaiswithin2valuesof σ, consequencethatabout65%ofthe
and99%oftheareawithin3values. areaiswithin1valueofσ,95%of
So,offortheapproximate95%CIforthecaseshowninFig-
theareaiswithin2valuesofσ,and
99%oftheareawithin3values.
ure6.10is
[0.34 2 0.09,0.34+2 0.09] = [0.16,0.52]
− · ·
abitmoreconservativerange(largeruncertainty)thanisgivenbythe
directmethodofquantiles,butitmucheasiertocalculate.
6.8 Marginalization
InSection1.4weintroducedtheconceptofmarginalization,andin
Section2.1weperformedadiscreteexampleofthis. Inthatsection
itwasseenassimplyaconsequenceofthesumandproductrules. It
wasawayoftakingaprobabilitythatdependedonseveralfactors,
andeliminatingallbutthesinglefactorwe’reinterestedin. Ifwe
haveacontinuousdistribution,thisprocessinvolvescalculusandwe
willnotcoveritindetail,butitisthesameprocess. Inthecaseofthe
distributionabove,wehaveadistributionoverasinglevariable,like
Beta(θ h,t). Imaginethatwehaveadistributionthatdependsontwo
|
parameters,
MyDist(θ,ξ)
whichspecifiestheprobabilityofaneventgiveneachcombinationof
theparameters, θ and ξ. We’dhavetodoathree-dimensionalplotto
visualizethis. Manytimes,however,wewantjusttheprobabilityof
oneofthesingleparameters. Inthosecaseswewillwrite
P(θ) [MyDist(θ,ξ)]
∼ marginalizeoverξ
whereweare“summing”overallthevaluesoftheotherparame-
ters,leavingthedetailstothemathematicians,andsimplyusingthe
result.
Likewisewecanmarginalizetheparameter θ togetthedistribution
oftheothervariable.
P(ξ) [MyDist(θ,ξ)]
∼ marginalizeoverθ
ThisbecomesimportantinChapter7andChapter9.
6.9 Exercises
Exercise6.1 GiventheposteriorshowninFigure6.10for10headsand20
tails,answerthefollowing:

introduction to parameter estimation 135
1 Themostlikelyestimatefortheparameterθ. Whatdoesthismean?
2 Isitlikelythatthisisafaircoin?
3 Whatis P(0 θ 0.3)approximately?
≤ ≤
4 Whatis P(0.2 θ 0.35)approximately?
≤ ≤
5 Whatisthemedianvalue? Whatarethequartiles?
5
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
θ
)θ(P
10 heads and 20 tails
50%
Beta(heads=10,tails=20)
25% Value Area
75% 0.17 0.01
0.21 0.05
0.24 0.10
0.29 0.25
0.34 0.50
5%
0.40 0.75
95%
0.45 0.90
1% 0.49 0.95
99%
0.55 0.99
0.21 0.34 0.49
0.17 0.29 0.40 0.55
Figure6.10:Posteriorprobability
distributionfortheθvaluesof
thebentcoin-theprobability
thatthecoinwilllandheads.The
6.10 Computer Examples distributionisshownfordata10
headsand20tails.Thevarious
quartilesareshownintheplot,and
summarizedintheaccompanying
from sie import * table.
Beta Distribution Example
3headsand9tails Plotabetadistributionwith3headsand9tails...
dist=beta(h=1,N=3)
distplot(dist ,xlim=[0,1],show_quartiles=False)


[TABLE]


50 | %

25 | % | 75 | %



5 | % | 95 | %

1 | % | 99 | %



0. | 0
17 | . | 21
0. | 2 | 0.
9 | 34
0. | 0.
40 | 4 | 9
0. | 55





[TABLE]




summarizedintheaccompanying
from sie import * table.







[TABLE]




dist=beta(h=1,N=3)

distplot(dist ,xlim=[0,1],show_quartiles=False)






136 statistical inference for everyone
Themedianofthisdistribution...
dist .median()
0.27527583248615201
the95
credible_interval(dist)
(0.067585986488542985, 0.38572756813238962, 0.80587955031675662)
1headsand3tails Thisshouldbeaboutthesamefractionasthepreviousexample,butbroader
dist=beta(h=1,N=4)
distplot(dist ,xlim=[0,1])
<matplotlib.figure.Figure at 0x108768cd0>


[TABLE]




dist .median()







[TABLE]




credible_interval(dist)







[TABLE]




dist=beta(h=1,N=4)

distplot(dist ,xlim=[0,1])






introduction to parameter estimation 137
credible_interval(dist)
(0.052744950526316919, 0.31381017045569742, 0.71641793611808946)


[TABLE]




credible_interval(dist)







[TABLE]











7 Priors, Likelihoods, and Posteriors
7.1 Binomial and Beta Distributions
InChapter6(IntroductiontoParameterEstimationonpage121)we
estimatedthechance, θ,thatabentcoinwouldcomeupheadsby
combiningauniformpriorfor θ (i.e. allpossiblevaluesarea-priori
equallylikely)andabinomiallikelihood(i.e. given θ,whatisthe
probabilityofthedata). ThisresultedinaBetadistributionforthe
posteriorprobabilityfor θ.
NoticewhattheprocedureofBayes’RecipeisandhowtheBayesian
inferenceworkshere.
1 Specifythepriorprobabilitiesforthemodelsbeingconsidered
Wewanttoestimateaquantity(whichwelabelasθ),butbegin
withabsolutelynoknowledgeofitsvalue-wehaveauniformprior
probability.
2 WritethetopofBayes’Ruleforallmodelsbeingconsidered
Weconstructamodelforhowdifferentpossiblevaluesofθinflu-
encetheoutcome-amodelwecallthelikelihood. Inthecaseofthe
bentcoin,thelikelihoodmodelisabinomialmodel,anddescribes
theprobabilityofflippingheadsortailsgivenhowbentthecoinis
(i.e. givenθ).
3 Putinthelikelihoodandpriorvalues
4 Addthesevaluesforallmodels
5 Divideeachofthevaluesbythissum, K,togetthefinalprobabili-
ties
Onceweobservedata,wecancombinethepriorandthemodelor
likelihoodusingtheBayes’recipe,andobtaintheposteriordistribu-
tionfortheunknownvalue,θ,givingustheprobabilityforeach
value,nowupdatedwithournewobservations.
Thelastcoupleofstepsoftherecipe,forsimplecases,isdoneby
themathematicianssowedon’thavetomanuallyaddanddivideas
wedidinthepreviouschapters. Inthecaseofthecoinflipsweget:

140 statistical inference for everyone
likelihood
(cid:122) (cid:125)(cid:124) (cid:123)
Beta(θ data) Binomial(data θ) Uniform(θ)
| ∼ | ×
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability priorprobability
FromthisBetadistribution,wecangetthemostlikelyvalues(i.e.
maximumprobabilityvalue)fortheunknownquantityofinterest,
θ,ouruncertaintyinthisquantity(i.e. thewidthoftheBetadistribu-
tion)consistentwiththeknowndata. Inotherwords,theposterior
probabilitysummarizesallofourknowledgeabouttheparameterof
interestgiventhedata.
7.2 The Normal Distribution - Properties
1
TheNormaldistribution,alsoreferredtoastheGaussiandistribution, 1Thedistributionisnamedafter
isbyfarthemostcommonlyoccurringdistributioninallofstatistical CarlFriedrichGausswhointro-
duceditin1809.However,ithas
inference,soitrequiressomespecialattention.
beencalledinthepasttheGauss-
Laplaciandistribution,duethethe
factthatPierreSimonedeLaplace
The Shape
wasthefirsttoapplyittorealprob-
lems,andprovedanumberofvery
TheshapeoftheNormaldistributionissometimesdescribedas usefulpropertiesofit.
bell-shaped,asshowninFigure7.1,andisthusreferredtoasthebell-
curve(althoughthereareseveralothermathematicalfunctionswhich
arebell-shaped). ThefunctionisreferredtoasNormal(µ,σ) where
µ and σ areparametersofthemodel. (seeAppendixB.1onpage225
forareviewofgreekletters)
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
x
)1,0(lamroN=)x(p
Figure7.1:TheNormalDistribu-
tion.


[TABLE]

















priors, likelihoods, and posteriors 141
The location parameter, µ
Thelocationparameter(seeFigure7.2)isthevalueof x forwhich
theNormaldistributionhasamaximumprobability. Inarealsense,
itisthemiddleofthedistribution,andthebestestimateof x. Forthe
Normaldistributionthelocationparameter, µ,isatoncethemean,
medianandmodeofthedistribution.
0.4
0.3
0.2
0.1
0.0
6 4 2 0 2 4 6
x
)1,µ(lamroN=)x(p
Figure7.2:TheNormaldistribution
withdifferentlocationparameters,
µ.
µ= 2 µ=0 µ=3
−
The deviation parameter, σ
AsshowninFigure7.3thedeviationparameter, σ,isameasureof
howspreadoutthedistributionis. Asthewidthincreases,theheight
goesdowntokeeptheareaunderthecurveconstant(at1). Asa
result,moreoftheprobabilitysitsatlargervaluesof x as σ getslarger.
Threeusefulpropertiesof σ fortheNormaldistributionarethe
following:
1 theNormaldistributionvalueatthemaximum(i.e. at x = µ)
isaround2.7timeslargerthanthevalueone-σ awayfromthe
maximum(at x = µ σ and x = µ+σ)
−
2 thetotalprobabilitybetweenthesetwopointsis65%. Thisistypi-
callywritten, µ σ.
±
3 95%ofthedistributionliesbetween µ 2σ and µ+2σ (seeFig-
−
ure7.3)
Forexample,writing5 2typicallyimpliesaNormaldistribution
±
withmean µ = 5anddeviation σ = 2. Oneis65%certainthatthe


[TABLE]


µ= | 2 µ | =0 | µ=3

−












142 statistical inference for everyone
rangeoftheestimatedvalueisbetween3and7,and95%certainthat
therangeisbetween1and9(i.e. meanminustwodeviationsand
meanplustwodeviations).
0.4
0.3
0.2
0.1
0.0
8 6 4 2 0 2 4 6 8
x
)σ,0(lamroN=)x(p
Figure7.3:TheNormaldistribution
withdifferentdeviationparameters,
σ.
σ=1
σ=2
σ=4
Summarizing the Distribution
WecanspecifytheNormaldistributionwithjustthetwoparameters,
µ and σ -thelocationanddeviationparameters,respectively. How-
ever,duetoitssymmetry,wecansummarizethisdistributionfor
allcasesbylookingaasinglespecialcasecalledthestandardNormal
distribution.
TheStandardNormalDistributionistheNormaldistributionin TheStandardNormalDistribution
thespecialcasewhere µ = 0(thedistributioniscenteredat x = 0) TheNormaldistributioninthe
specialcasewhereµ = 0(the
and σ =1(thedistributionhasaspreadof1). distributioniscenteredatx = 0)
ForanyNormaldistribution,theareawithin1-σ is0.68,within2-σ andσ = 1(thedistributionhasa
is0.95,and3-σ is0.99. Theselocationsarethemostprevalentlyused
spreadof1).
inanykindofstatisticaltesting,andthuswewillseethemmany
times.
Moving from a General Normal to the Standard Normal and Back
InordertousethetableofpercentilesforthestandardNormaldis-
tribution,weneedtobeabletotranslatefromtheNormaltothe
standardNormalandbackagain. Luckily,itisasimpleprocess,and
isoneofthemainreasonsforusingtheNormaldistribution-other
distributionsarenotsoeasilymanipulated.


[TABLE]


σ | =1



σ | =2

σ | =4








priors, likelihoods, and posteriors 143
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
x
)1,0(lamroN=)x(p
Figure7.4:TheStandardNormal
Distribution(theNormaldistribu-
tioninthespecialcasewhereµ=0
50.0% andσ=1).Thepercentilesshown
areforpositions1-σawayfromthe
center,2-σaway,and3-σaway.The
areawithin1-σis0.68,within2-σis
15.9% 84.1%
0.95,and3-σis0.99.Theselocations
arethemostprevalentlyusedin
area=0.68 anykindofstatisticaltesting,and
thuswewillseethemmanytimes.
2.3% 97.7%
0.1% 99.9%
-2.00 0.00 2.00
-3.00 -1.00 1.00 3.00
Tofacilitatethistranslation,wewillusethevariable x forthe
Normaldistributionand z forthestandardNormal. Sonow,weneed
tohavearecipefortranslating x to z (orviceversa),given µ and σ.
Theserecipesare:
1 x to z: subtract x by µ,anddivideby σ
2 z to x: multiply z by σ andadd µ
Example7.1 GivenaNormaldistributionwithameanofµ = 150anda
σ =20,whatisthemostlikelyvalue?
Themostlikelyvalueisthepeakoftheprobabilitydistribution,
xˆ = µ =150.
Example7.2 GivenaNormaldistributionwithameanofµ = 150and
σ =30,whatistheprobability P(x >170)
TousethetablesinSectionD.3onpage238,wefirstneedtotrans-
lateeverythingtothestandardNormalvalues.
x 150
x =170 z = − =0.67
⇒ 30
FromthetableinSectionD.3onpage238,theareatotheleftof
z = 0.67is0.7486. Becauseweareaskedtheprobabilitygreaterthan
x =170weneedtohavetheareatotherightofthecurve,or
P(x >170) =1 0.7486=0.2514
−


[TABLE]


50 | .0%

15 | .9% | 84 | .1%

area= | 0.68

2 | .3% | 97 | .7%

0 | .1% | 99 | .9%

-3. | -2.
00 | 00
-1. | 0.
00 | 00
1. | 2.
00 | 00
3. | 00




144 statistical inference for everyone
orabout1/4. Inotherwords,withamean µ = 150anddeviation
σ = 20,we’dexpectaboutaquarterofthetimethatthevalueofthe
variablewouldbegreaterthan170. Or,givenouruncertaintyofa
specificvalue,we’dassignaprobabilityofaround25%toitbeing
largerthan170.
Exercise7.1 GivenaNormaldistribution,withparametersµ = 10and
σ =2,determinethefollowingprobabilities:
1 P(x <12)
2 P(6< x <14)
3 P(2< x <12)
Exercise7.2 GivenaNormaldistribution,withparametersµ = 2and
σ = 10,answerthefollowingquestions(seeTable1.1onpage51forrefer-
ence):
1 Makeaqualitativeplotofthedistributiontohelpyouwiththeotherparts
ofthequestion
2 Islikelythat x >0?
3 Abovewhichvalueof xisitveryunlikelytoobserve?
4 Belowwhichvalueof xisitextremelyunlikelytoobserve?
Exercise7.3 GivenaNormaldistribution,withparametersµ = 2and
σ = 0.5,answerthefollowingquestions(seeTable1.1onpage51for
reference):
1 Makeaqualitativeplotofthedistributiontohelpyouwiththeotherparts
ofthequestion
2 Islikelythat x >0?
3 Abovewhichvalueof xisitveryunlikelytoobserve?
4 Belowwhichvalueof xisitextremelyunlikelytoobserve?
Sum and Differences
OnemoreconvenientpropertyoftheNormaldistributionisthat
sumsanddifferencesofvariablesthatindividuallyhaveNormal
distributionsalsohaveNormaldistributions,althougheachwith
adifferentmeananddeviationparameter. Therelationshipsare
summarizedasfollows.

priors, likelihoods, and posteriors 145
SumoftwoNormallydistributedvariablesIfwehavetwovari- SumoftwoNormallydistributed
ables, x and y,whichhaveNormaldistributions variablesIfwehavetwoNormally
distributedvariables,xandy,we
have
P(x) = Normal(µ ,σ )
P(x) = Normal(µx,σx )
x x
P(y) = Normal(µy,σy )
P(y) = Normal(µ y ,σ y ) P(x+y) = Normal(µx +µy,
(cid:113)
σ2+σ2)
x y
thentheirsum, x+y,hasameanthesumofthetwo, µ +µ anda
x y
(cid:113)
deviation σ2+σ2.
x y
Onewaytorememberthisisthatthenewsquareddeviationpa-
rameteristhesumofthetwooldones,
σ2 = σ2+σ2
x+y x y
DifferencesbetweentwoNormallydistributedvariables For DifferencesbetweentwoNormally
differences, x y,wehaveanewmeanof µ µ anddeviation distributedvariables
x y
− (cid:113) −
parameteragain σ x 2+σ y 2. Notethe“+”signinthenew σ,which P(x − y) = Normal(µx− µy,
(cid:113)
keepsthenew σ positivewhichismustbebydefinition. σ x 2+σ y 2)
Ifweareaskedforthedistributionofaquantitywithanadded (Notethe“+”signinthenewσ.)
constant,like
z = x+constant
thentheprobabilityof z isjustthesameasthatof x (i.e. Normal
distributionwiththesamedeviation),withthelocationparameter
movedbytheconstant
P(z) =Normal(µ +constant,σ )
x x
Example7.3 WehavetwoNormaldistributions P(x) = Normal(µ =
8,σ = 2)and P(y) = Normal(µ = 20,σ = 7). Whatisthedistribution
forz = y x?
−
Thedistribution P(z) isalsoaNormaldistribution,withmean
µ =20 8=12anddeviation σ = √72+22 =7.3.
z z
−

146 statistical inference for everyone
p(x)=Normal(8,2)
0.20
0.15
0.10
p(y)=Normal(20,7)
0.05
0.00
p(z)=p(y x)=Normal(12.0,7.3)
−
10 0 10 20 30 40
7.3 The Normal Distribution - Estimating From Data
Estimating the mean, µ, knowing the deviation, σ
Typicallyoneisprovidedwithaseriesofmeasurementsofaquan-
tity,andwewanttoestimatethevalueofthatquantity,andhavea
descriptionofouruncertaintyintheestimate. InChapter9(Applica-
tionsofParameterEstimationandInferenceonpage165)wegothrough
anumberofdetailedexamplesofthisprocess. Here,wesimplysum-
marizetheresult. Wearegiven:
1 Aseriesof N measurements,data= x ,x ,x ,...,x
1 2 3 N
{ }
2 Therealdeviation, σ
3 Wearemodelingthedataasatruevalue, µ,withuncertaintywith
alikelihoodfromtheNormaldistributionwithknowndeviation,
σ,asinNormal(0,σ). Further,weassumeindependencebetween
themeasurements.
Sinceinthiscasewearegiven σ,wewishthentoestimatethepa-
rameter µ. Theresultwillbeaprobabilitydistributionover µ,witha
best(i.e. mostprobable)valueandanuncertaintyinthatvalue. The
resultisthatthedistributionof µ isalsoaNormaldistribution, Inscientificapplications,this
notationisoftenshortenedto
P(µ data,σ) =Normal(x¯,σ/√N) µ = x¯ σ/√N,soitisclearwhat
| istheb ± estestimateofµ(i.e. x¯)
andwhatistheuncertaintyinthat
wherethecentervalue(andthusthemostprobablevalueof µ)is
estimate(i.e.σ/√N).
givenbythesamplemeanofthedata.
SampleMeanThesamplemeanofasetof N samples, x 1 ,x 2 , ,x N SampleMeanThesamplemeanof
···
asetofNsamples,x 1,x2,
···
,xN is
givenby
x¯
x
1
+x2 +x3 +
···
+xN
≡ N


[TABLE]


p(x)=Norm | al(8,2)





p(y)=Nor | mal(20,7)



p( | z)=p(y x)
− | =Normal(12 | .0,7.3)




priors, likelihoods, and posteriors 147
isgivenby
x +x +x + +x
x¯ 1 2 3 ··· N
≡ N
Theuncertaintyin µ isgivenby σ/√N. Asaconsequence,larger
N (i.e. moredatapoints),makesusmoreconfidentintheparticular
estimatefor µ.
Estimateoflocationparameter µ given N samplesand σ,the
knowndeviationInsummary,thebestestimateforthelocation Estimateoflocationparameterµ
parameter µ intheNormaldistributiongivenasetof N samples, givenNsamplesandσ,theknown
deviationThebestestimatefor
x ,x , ,x isgivenby
1 2 N thelocationparameterµinthe
···
Normaldistributiongivenasetof
µˆ = x 1 +x 2 +x 3 + ··· +x N σ/√N Nsamples,x 1,x2, ··· ,xN isgiven
N ± by
Example7.4 EstimatingtheTrueLengthofanObject µˆ =
x
1
+x2 +
···
+xN
σ/√N
N ±
Saywehaveanobject,and5measurementsofitslengthfromthe
samerulerbutfromdifferentpeople,
5.1[cm],4.9[cm],4.7[cm],4.9[cm],5.0[cm]
Saythatwefurtherknowthattheuncertainty(giventhisruler)of
onemeasurementhas σ = 0.5[cm]. Whatisthebestestimateofthe Inrealmeasurements,thereis
length? Thebestestimateshouldbegivenbythesamplemeanof alwaystheproblemofbiasor
systematicuncertainties,where
these5samples,
theuncertaintydoesnotfollowa
Normaldistribution.Wewillnot
µˆ = x 1 +x 2 + ··· +x N considerthisissuehere.
N
5.1[cm]+4.9[cm]+4.7[cm]+4.9[cm]+5.0[cm]
= =4.92[cm]
5
withuncertaintyrelatedtotheknownuncertaintyofasinglemea-
surement,
σ
σˆ =
√N
0.5[cm]
= =0.223[cm]
√5
yieldingafinalbestestimateof
µˆ = 4.92[cm] 0.223[cm]
±
or(with2σ range), The95%credibleinterval(CI)is
reallyatthe1.96σlevel,yielding
µˆ = 4.92[cm],95%CI= [4.474[cm],5.366[cm]]
[4.481[cm],5.358[cm]].Wewill
almostalwaysapproximateitas
2σbyhand,butthecomputerwill
generatethetrue95%credible
intervalwhenrequested.

148 statistical inference for everyone
Estimating the mean, µ, not knowing the deviation, σ
Ifwearenotsofortunatetobegiventhedeviation,asintheprevious
case,thenthisparametertoomustbeestimatedfromthedata. Asa
firststepwecanestimatethedeviationwiththesampledeviation.
SampleDeviationThesampledeviationofasetof N samples, SampleDeviationThesample
x ,x , ,x isgivenby deviationofasetofNsamples,
1 2 N
··· x 1,x2,
···
,xN isgivenby
(cid:114)
1 (cid:114) 1
S ≡ N 1 ((x 1 − x¯)2+(x 2 − x¯)2+ ··· +(x N − x¯)2) S ≡ N 1 ((x 1− x¯)2+ ··· +(xN− x¯)2)
− −
Approximateestimateoflocationparameter µ anddeviation σ
given N samples Theposteriorprobabilityfor µ and σ givenasetof Approximateestimateoflocation
N samples, x ,x , ,x canbeapproximatedwith parameterµanddeviationσ
1 2 N
··· givenNsamplesTheposterior
probabilityforµandσgivenaset
P(µ data) Normal(x¯,S/√N)
| ∼ (cid:18) (cid:113) (cid:19) a o p f p N ro s x a i m m p a l t e e s d ,x w 1 i , t x h 2, ··· ,xN canbe
P(σ data) Normal S,S2/ (N 1)/3
| ∼ − P(µdata) Normal(x¯,S/√N)
| ∼
whichworkswellifwehavemany(N >30)datapoints.
P(σ
|
data)
∼
Normal(S,
(cid:113) (cid:19)
Withasmallerdataset,thevalueof S asanestimateforthedevi- S2/ (N 1)/3
−
ationbecomestoosmall. Whentheestimatefor σ istoosmall,then
whichworkswellifwehavemany
theresultisclaimingmoreconfidenceintheestimateofthemean, µ, (N>30)datapoints.
thaniswarranted. Thisdiscrepancydependsonthenumberofdata Becausetheuncertaintyinthemean
points,andthusitmakessensethattheproperdistributionshould dependsexplicitlyonthenumberof
datapoints,itgoesbeyondthelevel
dependonthenumberofdatapoints,inadditiontothesample
ofthischaptertogiveaformforthe
meananddeviation. Theproper,althoughlessconvenient,resultis posteriorprobabilitydistribution
forthedeviation,σ.
thattheposteriorprobabilityfor µ takestheformoftheStudent’s t
distribution,
Estimateoflocationparameter µ given N samplesandunknown
σ Theposteriorprobabilityfor µ takestheformoftheStudent’s t Estimateoflocationparameterµ
distribution, givenNsamplesandunknown
σTheposteriorprobabilityforµ
takestheformoftheStudent’st
P(µ
|
data) =Student
dof=N − 1
(x¯,S/√N)
distribution,
Thisdistributionrequiresthreenumberstospecify,referredtoasthe
P(µ
|
data)=Student
dof=N − 1
(x¯,S/√N)
mean(µ),deviation(σ)andthedegreesoffreedom(dof). Thedegrees Thisdistributionrequiresthree
numberstospecify,referredtoas
offreedomisdefinedinthiscasetobethenumberofdatapointsless
themean(µ),deviation(σ)andthe
one, N 1. degreesoffreedom(dof).Thedegrees
−
offreedomisdefinedinthiscaseto
Example7.5 EstimatingtheTrueLengthofanObject...Again bethenumberofdatapointsless
one,N 1.
−
Saywehaveanobject,and5measurementsofitslengthfromthe
samerulerbutfromdifferentpeople,
5.1[cm],4.9[cm],4.7[cm],4.9[cm],5.0[cm]

priors, likelihoods, and posteriors 149
Unlikeearlier,let’ssaythatwedon’tknowtheuncertainty(giventhis
ruler)ofonemeasurementWhatisthebestestimateofthelength?
Again,thebestestimateshouldbegivenbythesamplemeanofthese
5samples,
x +x + +x
µˆ = 1 2 ··· N
N
5.1[cm]+4.9[cm]+4.7[cm]+4.9[cm]+5.0[cm]
= =4.92[cm]
5
withuncertaintyrelatedtothesampledeviation
1 (cid:16) (cid:17)
S2 = (x x¯)2+ +(x x¯)2
1 N
N 1 − ··· −
−
1 (cid:16)
= (5.1[cm] 4.92[cm])2+(4.9[cm] 4.92[cm])2+(4.7[cm] 4.92[cm])2+
5 1 − − −
− (cid:17)
(4.9[cm] 4.92[cm])2+(5.0[cm] 4.92[cm])2
− −
= 0.024[cm]2
(cid:113)
S = 0.024[cm]2 =0.155[cm]
S 0.155[cm]
= =0.069[cm]
√N √5
LookingatTableD.2onpage236with“DegreesofFreedom”equal
to4,wefindthatthe95%credibleintervalfor µ (betweenareas0.025
and0.975)falls 2.776 S/√N,thuswehave
± ·
µˆ = 4.92[cm],95%CI= [4.92[cm] 2.776 0.069[cm],4.92[cm]+2.776 0.069[cm]]
− · ·
= 4.92[cm],95%CI= [4.73[cm],5.11[cm]]
Althoughmuchofthisiseasierwiththecomputer,itisinstructive
togothroughsimpleexamplesbyhand.
7.4 Normal Approximation
TheNormaldistributionisusefulformanyreasons: itssimpleshape,
thefactthatthereareonlytwoparameterswhichdescribeit,andthe
easewithwhichonecancomparethegeneralNormaldistributionto
thesinglestandardNormal. Further,itcanbeusedasanapproxima-
tionforseveralotherdistributions,undercertainlimits.
The Beta Distribution
Wefirstsawthebetadistributionastheposteriordescriptionina
bent-coinparameterestimationproblem(seeSection6.3onpage125
inChapter6(IntroductiontoParameterEstimation)). TheNormalap-
proximationoccurswhenthenumberofflipsgetslarge,compared

150 statistical inference for everyone
tohowlikelythecoinflipsheads. Fornotation,wewillwritethe
frequencyofheadsas
h
f
≡ N
NormalApproximationtotheBetaDistribution TheNormal NormalApproximationtotheBeta
ApproximationtotheBetaDistribution,forlargenumberofflips(N) DistributionTheNormalApproxi-
mationtotheBetaDistribution,for
ofwhichafraction f h/N aresuccessfulisgivenby
largenumberofflips(N)ofwhicha
≡
fraction f h/Naresuccessfulis
≡
givenby
Beta(h,N) Normal(µ= f,
∼
(cid:113) (cid:19)
(cid:18) (cid:113) (cid:19) σ= f(1 − f)/N
Beta(h,N) Normal µ = f,σ = f(1 f)/N
∼ −
Toseehowclosethisapproximationcanbe,observethefollowing
twocases:
3.5
3.0
2.5
2.0
1.5
1.0
0.5
0.0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
3 heads and 9 tails
Beta
Normal
µ=0.25
σ=0.12
Withtentimesasmanyflips,wehave


[TABLE]




Beta

Nor | mal



µ | =0. | 25

σ | =0. | 12














priors, likelihoods, and posteriors 151
12
10
8
6
4
2
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
30 heads and 90 tails
Beta
Normal
µ=0.25
σ=0.04
andthecurvesaresocloseastobenearlyidentical! Therestillis Thisisanapproximation,andas
a(small)probabilityforgettinganegative θ,whichisproblematic suchwillcertainlygiveseriously
incorrectanswersundercertain
intheorybutnottypicallyinpractice. Tousethepropertiesofthe
circumstances.Forexample,inthis
Normaldistributionheretoquantifyouruncertaintyaboutthebent case,theNormalapproximation
coin. Given30headsand90tails,thebestestimatefor θ (i.e. the
predictsthatthereisarounda1.8%
chancethatthebentcoinmight
topofthecurve)is0.25. Ouruncertaintyisquantifiedbythewidth haveanegativeθ,orprobabilityof
ofthedistribution,givenby σ. Thus,wecanbeconfidenttoa95% flippingheads(lookatheNormal
curvetotheleftofθ = 0)!The
degreefor θ within2σ,orbetween0.17and0.33(0.25 2 0.04and
betadistributioniszeroforany
− ·
0.25+2 0.04,respectively). valuebelowzerooroverone,and
· thuswillneverleadtosuchabsurd
answers.
The Binomial Distribution
Similarly,withthe(discrete)binomialdistribution(seeEquation3.3)
wehavetheNormalapproximation.
NormalApproximationtotheDiscreteBinomialDistribution NormalApproximationtothe
DiscreteBinomialDistribution
Binomial(N,p) = Normal(µ=N p,
·
(cid:113) (cid:113)
Binomial(N,p) =Normal(µ = N p,σ = N p(1 p)) σ= N · p(1 − p))
· · −
withexamples


[TABLE]






Beta
Nor | mal



µ | =0. | 25

σ | =0. | 04












152 statistical inference for everyone
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 2 4 6 8 10 12
k
)52.0=p,01=N(laimoniB
Binomial
Normal
µ=2.50
σ=1.37
and
0.10
0.08
0.06
0.04
0.02
0.00
0 20 40 60 80 100
k
)52.0=p,001=N(laimoniB
Binomial
Normal
µ=25.00
σ=4.33
The Student’s t Distribution
Forsmallishdatasets,5 < N < 30,wecanreplacetheestimateofthe
meanfromtheStudent’s t distributiontoaNormaldistributionwith
anincreasedestimateforthedeviation. Itthenbecomespracticalto
usethemoreconvenient z-scoretoestimatecredibleintervalsrather


[TABLE]


inomial
ormal

B
N | inomial
ormal

µ= | 2.50

σ= | 1.37











[TABLE]


Binomial
Normal

µ
σ | =25.00
=4.33











[TABLE]


Binomial
Normal




priors, likelihoods, and posteriors 153
2
thanthefull t tables. Theapproximationinthisdomainlookslike 2D.Berry. Statistics:ABayesian
Perspective. Duxbury,1996
NormalApproximationtotheStudent’stDistribution For NormalApproximationtothe
smallishdatasets,5< N <30, Student’stDistribution For
smallishdatasets,5<N<30,
Student dof=N − 1 (x¯,S/√N k ) ∼ N 1+ orm 20 al(x¯,Sk/√N) Student N do o f= rm N − a 1 l( ( x x ¯ ¯ , , k S · / S √ / N √ ) N ∼ )
≡ N2 20
k 1+
Example7.6 EstimatingtheTrueLengthofanObject...YetAgain ≡ N2
Saywehaveanobject,and5measurementsofitslengthfromthe
samerulerbutfromdifferentpeople,
5.1[cm],4.9[cm],4.7[cm],4.9[cm],5.0[cm]
Unlikeearlier,let’ssaythatwedon’tknowtheuncertainty(giventhis
ruler)ofonemeasurement. Whatisthebestestimateofthelength?
Again,thebestestimateshouldbegivenbythesamplemeanofthese
5samples,
x +x + +x
µˆ = 1 2 ··· N
N
5.1[cm]+4.9[cm]+4.7[cm]+4.9[cm]+5.0[cm]
= =4.92[cm]
5
withuncertaintyrelatedtotheadjustedsampledeviation,
1 (cid:16) (cid:17)
S2 = (x x¯)2+ +(x x¯)2
1 N
N 1 − ··· −
−
1 (cid:16)
= (5.1[cm] 4.92[cm])2+(4.9[cm] 4.92[cm])2+(4.7[cm] 4.92[cm])2+
5 1 − − −
− (cid:17)
(4.9[cm] 4.92[cm])2+(5.0[cm] 4.92[cm])2
− −
= 0.024[cm]2
(cid:113)
S = 0.024[cm]2 =0.155[cm]
S 0.155[cm]
= =0.069[cm]
√N √5
20
k = 1+ =1.8
52
S
k = 1.8 0.069[cm] =0.124[cm]
· √N ·
yieldingafinalbestestimateof
µˆ = 4.92[cm] 0.124[cm]
±
or(with2σ range),
4.92[cm],95%CI= [4.672[cm],5.168[cm]]
ComparethisrangetotheoneshowninExample7.5onpage148.
Theoneherehasaslightlylargerrange,whichisabitmoreconser-
vativethanisneeded,butthecalculationisquiteabiteasier.

154 statistical inference for everyone
7.5 Summary
ItisusefultoseealloftheseresultsstemmingfromthesameBayes’
Recipe,appliedtodifferentmodelsofthedataand(possibly)differ-
entpriorprobabilities. Aswehavestated,manyofthesimplecases
havebeenworkedoutbythemathematicians,sowedon’tneedto
dotheworkofderivingthem. Itwillbeourtasktounderstandtheir
properties,tobeabletoapplythemtorealproblems,andtounder-
standtheirconsequences. Oneoftheimmediateobservationsthat
wemakeistheprevalenceoftheNormaldistribution,justifyingour
detailedexplorationofitinthischapter.
1 Proportions
ParameterofInterest: θ,thechancesofasingleevent
Applications: coinflips,votingpercentages,successinsports,
performanceontests
Formofthedata: h successesin N totalevents
Modelofthedata:
(cid:40)
success ,withprobability θ
data=
failure ,otherwise(i.e. withprobability1 θ)
−
PosteriorProbability:
likelihood
(cid:122) (cid:125)(cid:124) (cid:123)
Beta(θ data) Binomial(data θ) Uniform(θ)
| ∼ | ×
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability priorprobability
2 MagnitudewithKnownDeviation
ParameterofInterest: µ,thetruemagnitudeofaquantity,given
thedeviation,labeledby σ,fromthecentralvalue
Applications: percentageswithlargesamples,scientificmeasure-
mentssuchasweightandsizeofobjects,timescalesofevents
Formofthedata: N totaldatapoints,labeled x ,x , ,x ,and
1 2 N
···
givenknown σ
Modelofthedata:
data= µ+uncertaintywithprobabilityNormal(µ =0,known σ)
PosteriorProbability:
likelihood
(cid:122) (cid:125)(cid:124) (cid:123)
Normal(µ data,σ) Normal(data µ,σ) Uniform(µ)
2
| ∼ | ×
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability priorprobability

priors, likelihoods, and posteriors 155
3 MagnitudewithUnknownDeviation
ParameterofInterest: µ,thetruemagnitudeofaquantity,and
theunknowndeviation,labeledby σ,fromthecentralvalue
Applications: scientificmeasurementswithsmallsamples(less
thanaround30),suchasweightandsizeofobjects,timescales
ofasmallnumberofevents
Formofthedata: N totaldatapoints,labeled x ,x , ,x
1 2 N
···
Modelofthedata:
data= µ+uncertaintywithprobabilityNormal(µ =0,σ)
PosteriorProbability:
likelihood
(cid:122) (cid:125)(cid:124) (cid:123)
P(µ,σ data) Normal(data µ,σ) Uniform(µ) Uniform(logσ)
| ∼ | × ·
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability priorprobability
Student T(µ data) [P(µ,σ data)]
− | ∼ | marginalizedoverσ
(cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability
F(σ data) [P(µ,σ data)]
| ∼ | marginalizedoverµ
(cid:124) (cid:123)(cid:122) (cid:125)
posteriorprobability
7.6 Computer Examples
from sie import *
Estimating Lengths
Knowndeviation,σ
x=[5.1, 4.9, 4.7, 4.9, 5.0]
sigma=0.5
mu=sample_mean(x)
N=len(x)
dist=normal(mu,sigma/sqrt(N))
distplot(dist)
<matplotlib.figure.Figure at 0x10713c710>


[TABLE]




from sie import *







[TABLE]


x=[5.1, 4.9, 4.7, 4.9, 5.0]

sigma=0.5







[TABLE]




mu=sample_mean(x)

N=len(x)







[TABLE]




dist=normal(mu,sigma/sqrt(N))

distplot(dist)






156 statistical inference for everyone
credible_interval(dist)
(4.4817387297117088, 4.9199999999999999, 5.358261270288291)
Unknownσ
mu=sample_mean(x)
s=sample_deviation(x)
print mu,s
4.92 0.148323969742
dist=tdist (N 1,mu,s/sqrt(N))
−
distplot(dist ,xlim=[4.6 ,5.4])
<matplotlib.figure.Figure at 0x1085b5c50>


[TABLE]




credible_interval(dist)







[TABLE]


mu=sample_mean(x)

s=sample_deviation(x)

print mu,s







[TABLE]




dist=tdist (N 1,mu,s/sqrt(N))

−





[TABLE]




distplot(dist ,xlim=[4.6 ,5.4])






priors, likelihoods, and posteriors 157
credible_interval(dist)
(4.7358314667008017, 4.9199999999999999, 5.1041685332991982)


[TABLE]




credible_interval(dist)







[TABLE]











8 Common Statistical Significance Tests
Thebasicideaofcommonstatisticaltestsintheapproachwehave
takenhasbeenthefollowing:
1 Observesomedata
2 Constructamodelofthedata,withaparameterthatneedstobe
estimated,suchasthe“true”singlevalue(µ,inSection7.3),orthe
proportionoftheevent(θ,inSection7.4).
3 Calculatethefinal,posteriorprobabilityofthatparameter
4 “Test”toseeifthereisasignificant(usually95%)probabilitythat
theparameterisnotzero. Insomecaseswearenotcomparing
theparametertozerobuttosome
5 Ifthetestpasses,thenonecanbereasonablyconfidentthatthe theoreticalexpectation.Eventhere,
parameterisnon-zero-thattheeffectisreal. Ifthetestfails,then wearecomparingtheparameter
minusthetheoreticalexpectation
underthemodel,thepossibilityofazero-effectcannotbereason-
tozeroandthuswedon’tlose
ablyexcluded. anygeneralityintheprocedureby
alwayscomparingtozero.
Thesetestsareasubsetoftheparameterestimationtechniques
coveredinbothChapter6(IntroductiontoParameterEstimationon
page121)andChapter7(Priors,Likelihoods,andPosteriorsonpage139),
inthespecialcasewhereweareinterestedindeterminingifthereis
aneffectatall. Forexample,wemightbeinterestedtoseeifamed-
icaltreatmentworks,sowecomparethebefore-andafter-treatment
valuestoseeifthedifferenceisnon-zero.
Theteststhatonetypicallyemploysinsimplecasesgobyvarious
names,dependingonthemodel. Thischaptersummarizesseveralof
thecommonones,andappliesthemtosometypicalcases.
8.1 z-test
The z-testisthesimplesttesttouse,andisperhapsthemostcom-
mon. Itisusedwhenwehavethefollowingassumptions:
1 Wearemodelingthedataasatruevalue, µ,withuncertainty

160 statistical inference for everyone
2 WearemodelingtheasaNormaldistributionwithknowndevia-
tion, σ,asinNormal(0,σ).
3 Weareassumingindependencebetweenthemeasurements.
Themodelofthedatais
data= µ+uncertaintywithprobabilityNormal(µ =0,known σ)
where µ representsthe“true”value. Theposteriordistributionfor µ
alsofollowsaNormaldistribution,withasmalleruncertainty, σ/√N
where N isthenumberofdatapoints.
Tousethe z-test,weperformthefollowingsteps:
1 Calculateourbestestimatefor µ,denotedas µˆ.
2 Giventheknownuncertainty, σ ofasinglemeasurement,determine
therangeofcrediblevaluesfor µ withintheuncertaintyofthe
estimateforthe N observations, σ/√N.
3 Testtoseeifthecrediblerangeincludeszero.
4 Ifso,thenthetestpasses,andwecanbereasonablyconfidentthat
theparameterisnon-zero-thattheeffectisreal.
5 Ifthetestfails,i.e. thecrediblerangedoesnotincludezero,then
underthemodelthepossibilityofazero-effectcannotbereason-
ablyexcluded.
Thereareseveralscenarioswhereweusethe z-test,eachwith
thesameprocedure,differingonlyinthemethodofestimatingthe
“true”value µ.
1 For N independentobservations, x ,x ,...,x wehavethebest
1 2 N
estimategivenbythesamplemean,anduncertaintyrelatedtothe
single-measurementdeviation, σ,as
x +x + +x
µˆ = 1 2 ··· N σ/√N
N ±
2 Whenestimatingaproportion,foralargenumberofevents N of
whichafraction f h/N aresuccessful,wehave
≡
µˆ f
≈
(cid:113)
σ/√N f(1 f)/N
≈ −
3 Forsmallishdatasets,5 < N < 30,wheretheuncertaintyisnot
known,
x +x + +x
1 2 N
µˆ ···
≈ N
σ/√N kS/√N
≈

common statistical significance tests 161
wherewereplacetheknown σ/√N fromthepreviouscasewith
anestimateusingthesamplestandarddeviationandanadjust-
mentforsmalldatasetparameter k,
1 (cid:16) (cid:17)
S2 = (x x¯)2+ +(x x¯)2
1 N
N 1 − ··· −
−
20
k 1+
≡ N2
8.2 What it means and doesn’t mean
Forallofthesetests,weusethevocabularyof“statisticalsignifi-
cance”,whichneedstobefurtherclarified.
Significance
1
Thereisatermusedintheliteraturecalledstatisticalsignificance. 1Althoughtheword“significant”
Roughlyitmeansavaluethatisveryunlikelytobezero(seeTable1.1 occursintheterm“statistically
significant,”itdoesnotimplythat
onpage51),orinotherwords,thevalueofzeroisnotwithinthe
theresultitselfisimportant-itmay
95%percentile. Thisiswithin2standarddeviationsofthevalue,so beasmall,uninterestingeffect,but
crediblynon-zero.Perhapsaterm
thefollowingestimatedvaluesarenotstatisticallysignificant:
like“statisticallydetectable”would
bebetter,butweareunfortunately
• 5 3-thetwo-deviationrangeis[-1,11]containsthevalue0 boundtothehistoricaluseofthe
±
term.
• 7 4
±
• 3 2
− ±
butthefollowingarestatisticallysignificant:
• 5 2-thetwo-deviationrangeis[1,9]doesnotcontainthevalue0
±
• 7 3
±
• 3 1
− ±
Statisticalsignificance,attheveryunlikelylevel(i.e. 95%percentile)
isoftenusedasaroughguidelinetopublishapositiveeffect.
numberofde- Table8.1:Roughguideforthe
viationsaway conversionofdeviationsaway
term probability
fromzeroandthequalitativelabels
fromzero
forprobabilityvaluesforbeinga
significantdeviation.
1σ slightlylikely/likely 0.7(i.e. 7/10)
2σ verylikely 0.95(i.e. 19/20)
3σ extremelylikely 0.01(i.e. 1/100)
>4σ virtuallycertain >999,999/1,000,000

162 statistical inference for everyone
Anunintuitiveconsequence Oneconsequenceofthisisthattwostud-
iesthatdisplaydifferentmagnitudesforaquantitymaynotbestatis-
ticallysignificantintheirdifference. Thefollowingexampleisbased
2
onanexamplefromGelmanandHill’sbookonDataAnalysis. Say 2A.Gelman,J.Hill,andEbooks
wehavetwomeasurementswithmeansandstandarddeviations: Corporation. Dataanalysisusing
regressionandmultilevel/hierarchical
• 25 10 models,volume625. Cambridge
± UniversityPressCambridge,UK:,
2007
• 10 3
±
Further,letussupposethatweareinterestedinwhetherthemea-
surementsarezeroornot. Thefirstmeasurementshowsasignificant
effect(thetwo-deviationrangeis[5,45]doesnotcontainzero),and
thesecondonedoesaswell(thetwo-deviationrangeis[4,16]does
notcontainzero). Thedifferencebetweenthemis
(cid:112)
(25 10) 102+32 =15 10.4
− ± ±
whichisnotsignificant. Oneshouldbecarefulcomparingthemagni-
tudesanduncertaintiesofmeasurements!
8.3 Student-t-test
Whenwearenotgiventheuncertaintyofthemeasurements, σ,and
thedataareinsufficienttoestimatetheuncertainty,thenweneedto
estimateboththe“true”value, µ,andtheuncertainty. Thisleadsto
awidercrediblerangeforthe“true”value. Wecanapplythesame
testingprocedure,bylookingatthe95%credibleregiontoseeifit
includeszero,butthistimetheposteriordistributionweusecomes
fromtheso-calledStudent-t distribution. Theoddname“Student-ttest”
comesfromthefactthetestwas
1 For N independentobservations,westillhavethebestestimateof originallypublishedbyWilliam
the“true”valuegivenbythesamplemean GossetwhoworkedattheGuinness
breweryinDublinandhispen
x +x + +x namewas“Student”.
µˆ = 1 2 ··· N
N
2 Thebestestimateoftheuncertaintyofasinglemeasurementis
givenbythesamplestandarddeviation
σˆ = S
where S isthesamplestandarddeviation
1 (cid:16) (cid:17)
S2 = (x x¯)2+ +(x x¯)2
1 N
N 1 − ··· −
−
3 Thecredibleregionisdeterminedbythe95%intervaloftheposte-
rior,Student-t distribution,ofthefollowingform
Student dof=N 1 (x¯,S/√N)
−

common statistical significance tests 163
4 Testtoseeifthecrediblerangeincludeszero.
5 Ifso,thenthetestpasses,andwecanbereasonablyconfidentthat
theparameterisnon-zero-thattheeffectisreal.
6 Ifthetestfails,i.e. thecrediblerangedoesnotincludezero,then
underthemodelthepossibilityofazero-effectcannotbereason-
ablyexcluded.
8.4 Computer Examples
from sie import *
data=load_data( ’data/iris .csv ’)
x_sertosa=data[data[ ’class ’]==’Iris setosa ’][ ’petal length [cm] ’]
−
x=x_sertosa
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_sertosa=tdist (N,mu,sigma)
print "total number of data points:" ,N
print "best estimate:" ,mu
print "uncertainty:" ,sigma
total number of data points: 50
best estimate: 1.464
uncertainty: 0.0245381834898
new_length=1.7
distplot(t_sertosa , label=’petal length ’ ,xlim=[1.37 ,1.8] ,
quartiles =[.01 ,0.05 ,.5 ,.95 ,.99] ,
)
ax=gca()
ax.axvline(1.7 ,color=’r ’)
savefig( ’ ../../ figs/z_test_iris .pdf’)
<matplotlib.figure.Figure at 0x10f9d2710>


[TABLE]




from sie import *







[TABLE]




data=load_data( ’data/iris .csv ’)







[TABLE]




x_sertosa=data[data[ ’class ’]==’Iris setosa ’][ ’petal length [cm] ’]

−





[TABLE]




x=x_sertosa

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_sertosa=tdist (N,mu,sigma)



print "total number of data points:" ,N

print "best estimate:" ,mu

print "uncertainty:" ,sigma







[TABLE]




new_length=1.7







[TABLE]




distplot(t_sertosa , label=’petal length ’ ,xlim=[1.37 ,1.8] ,

quartiles =[.01 ,0.05 ,.5 ,.95 ,.99] ,

)

ax=gca()

ax.axvline(1.7 ,color=’r ’)

savefig( ’ ../../ figs/z_test_iris .pdf’)






164 statistical inference for everyone


[TABLE]









9 Applications of Parameter Estimation and Inference
9.1 Normal Model - Inference about Means
Example9.1 Irispetallengths-Bestestimate
1.4 1.4 1.3 1.5 1.4 Table9.1:Irispetallengths,in
centimeters,forIristypeSetosa.
1.7 1.4 1.5 1.4 1.5
1.5 1.6 1.4 1.1 1.2
1.5 1.3 1.4 1.7 1.5
1.7 1.5 1.0 1.7 1.9
1.6 1.6 1.5 1.4 1.6
1.6 1.5 1.5 1.4 1.5
1.2 1.3 1.5 1.3 1.5
1.3 1.3 1.3 1.6 1.9
1.4 1.6 1.4 1.5 1.4
Table9.1showsdataforthelengths(incentimeters)ofthepetals
1
ofonespeciesofIrisflower . Ifwewanttoestimatethe“true”length 1K.BacheandM.Lichman. UCI
ofthethepetalforthisspecies,givenalloftheseexamples,wewould
machinelearningrepository,2013.
URLhttp://archive.ics.uci.edu/
applythefollowingmodelofthedata:
ml
2.0
data = truevalue+Normal(mean=0,known σ)
1.5
orequivalently σ
(known deviation)
1.0
data = Normal(mean=truevalue,known σ)
0.5
Theresultingdistributionforthe“truevalue”, µ,isalsoaNormal
distribution(Section7.3), 0.0
0 µ
(unknown true value)
P(µ data,σ) =Normal(x¯,σ/√N)
|
wherethebestestimateofthetruevalue, µ isthesamplemean, x¯,
andtheuncertaintyisrelatedtothesampledeviation(whichwe’re


[TABLE]




(kno | σ
wn devia | tion)








166 statistical inference for everyone
goingtotakeasthe“known”deviation, σ 0.174)inthiscase. Thus,
∼
1.4+1.4+1.3+1.5+ +1.6+1.4+1.5+1.4
µˆ = x¯ = ···
50
= 1.464
andthefullanswer,withuncertainty,is
0.174
µˆ = 1.464[cm] [cm]
± √50
= 1.464[cm] 0.025[cm]
±
Example9.2 Irispetallengths-Adifferentspecies?
Hereweapplythe z-test(Section z-testonpage159)toanew
observationtoseeifthereisreasontobelieveittobeadifferent
species. Imaginewehaveasingleobservationofanotheririswith
petallength2.5[cm]. IsthislikelytobethesametypeastheSetosa
typeabove? AsoutlinedinSection7.2,wegetthebestestimatefor
thedifferenceas:
µ =2.5 1.464=1.036
diff −
withuncertaintythesameastheuncertaintyoftheSetosatype,sothe
finalestimatewithuncertaintyis:
1.036[cm] 0.025[cm]
±
whichis
1.036[cm]
=41deviationsawayfromzero!
0.025[cm]
whichmakesitvirtuallycertaintobeadifferenttype(seeTable8.1).
9.2 Normal Model Again - Inference about Means and Deviations
Setosa 1.4 1.4 1.3 1.5 1.4 Table9.2:Subsetofirispetal
lengths,incentimeters,foriris
Virginica 6.0 5.1 5.9 5.6 5.8
typesVirginica,Setosa,andVersi-
Versicolor 4.7 4.5 4.9 4.0 4.6 color.
Example9.3 Irispetallengths-Significantlydifferent?
Inthisexampleweapplythe t-test(SectionStudent-t-teston
page162)toasubsetoftheirissamples,toseeifthedifferentspecies
canbereasonablyseparatedusingtheirpetallengths. ShowninTa-
ble9.2isaverysmallsubsetofthefullirispetal-lengthdata. Arethe

applications of parameter estimation and inference 167
typesVirginicaandVersicolorlongerthanthetypeSetosa? IstheVir-
ginicalongerthanVersicolor? Foreachofthese,weneedtospecifythe
model,determinethebestestimatefortheparametersofthemodel,
andthencomparethedistributions.
ThemodelwewilluseisthesimpleNormalmodel,
data = Normal(mean=truevalue,unknown σ)
whichisthesameasthepreviousexample,exceptthatthedeviation,
σ,isunknown. Inadditiontobeingunknown,therearesofewdata
pointsthatthedeviationcan’tbewellapproximatedwiththesample
deviation.
Theresultingdistributionforthe“truevalue”, µ,isaStudent-t
distribution(Section7.3),
P(µ
|
data) =Student
dof=N − 1
(x¯,S/√N)
Thebestestimatesforthetruelength-valuesofeachtypeisgivenby
theirsamplemeans,
1.4+1.4+1.3+1.5+1.4
µˆ = =1.40
setosa
5
6.0+5.1+5.9+5.6+5.8
µˆ = =5.68
virginica
5
4.7+4.5+4.9+4.0+4.6
µˆ = =4.54
versicolor
5
andthesampledeviationsforeachisgivenby
(cid:114)
1
S = ((1.4 1.40)2+(1.4 1.40)2+(1.3 1.40)2+(1.5 1.40)2+(1.4 1.40)2)
setosa
5 1 · − − − − −
−
= =0.07
(cid:114)
1
S = ((6.0 5.68)2+(5.1 5.68)2+(5.9 5.68)2+(5.6 5.68)2+(5.8 5.68)2)
virginica
5 1 · − − − − −
−
= =0.36
(cid:114)
1
S = ((4.7 4.54)2+(4.5 4.54)2+(4.9 4.54)2+(4.0 4.54)2+(4.6 4.54)2)
versicolor 5 1 · − − − − −
−
= 0.34
Theposteriorprobabilitydistributions,showninFigure9.1,have
thefollowingform:
P(µ setosa
|
data) = Student dof=4 (1.40,0.07/√5)
P(µ virginica
|
data) = Student dof=4 (5.68,0.36/√5)
P(µ versicolor| data) = Student dof=4 (4.64,0.34/√5)
Itisclearfromthepicturethattheyareverywellseparated,butwe
canquantifythisbylookingattheprobabilitythatthedifference
betweentheirmeansisgreaterthanzero.

168 statistical inference for everyone
12
10
8
6
4
2
0
0 1 2 3 4 5 6 7 8
Petal Length [cm]
)atad|htgneL
lateP(P
Figure9.1:Probabilitydistributions
forthesubsetofirispetallengths.
EachdistributionfollowsaStudent-
Setosa
tform.
Virginica
Versicolor
Theprobabilityoftheirdifferenceapproximatelytakestheformof Thisapproximationiscalled
aStudent’stdistribution,withthesamecenteranddeviationshown Welch’smethod.Theexactanal-
ysisisbeyondthisbook,but
fortheNormalinSection7.2. Herewedothecalculationbetweenthe
numericallyonecancalculate
closesttwoiristypes,VirginicaandVersicolor: itanditdoesn’tdifferfrom
thisapproximateanalysisin
anysignificantway.Essentially
µ = 5.68 4.64=1.04
diff − youcalculateP(µ versicolor >
(cid:114) 0.362 0.342 µvirginica| data)byaddingupthe
σ
diff
=
5
+
5
=0.22 P(µ
versicolor|
data)
×
P(µvirginica| data)
forallpossiblelengthswhere
versicolorislongerthanvirginica.
ThedegreesoffreedomusedforthisStudent’stdistributionisap-
proximatelythesmallestonefromthetwosamples,orinthiscase
(sincebothsampleshavethesamenumberofdatapoints),dof=4.
Theresultingposteriorprobabilitydistributionforthedifferenceof
meansisshowninFigure9.2.
Weobservethatthedifferenceofthemeansisover4timesthe
deviationawayfromzero,soevenwith4degreesoffreedom,thisis
significantatthe99%level. Wecanbehighlycertainthatthesetwo
specieshavedifferentpetallengths,andthatthedifferenceobserved
isnotjustaproductoftherandomsample.
Example9.4 BallBearingSizes
2
Here’sadatadataset,measuringthesizeofballbearings from 2DavidJHand,FergusDaly,KMc-
twodifferentproductionlines. Conway,DLunn,andEOstrowski.
Ahandbookofsmalldatasets,vol-
Wecanaskquestionssuchas: ume1. CRCPress,2011
• Whatisourbestestimateofthesizeofaballbearing,givenoneof
theproductionlines?


[TABLE]


osa
ginica

Set
Vir | osa
ginica

Ver | sicolor














applications of parameter estimation and inference 169
2.0
1.5
1.0
0.5
0.0
0.0 0.5 1.0 1.5 2.0
Petal Length Difference [cm]
)atad
L
L(P
|rolocisrev
−acinigriv
Figure9.2:Probabilitydistributions
forthedifferencebetweenirispetal
50% lengthsfortheclosesttwoiris
types,VirginicaandVersicolor.The
distributionfollowsaStudent-t
form,andclearlyshowssignificant
25% 75%
probability(greaterthan99%)for
beinggreaterthanzero.
10% 90%
5% 95%
1% 99%
0.57 0.88 1.20 1.51
0.22 0.70 1.04 1.38 1.86
Firstline[microns]
Table9.3:Productionlinesarepro-
duceaballbearingwithadiameter
1.18 1.42 0.69 0.88 1.62 1.09 1.53 1.02 1.19 1.32
ofapproximately1micron.Tenball
Secondline[microns] bearingswererandomlypicked
1.72 1.62 1.69 0.79 1.79 0.77 1.44 1.29 1.96 0.99 fromtheproductionline(i.e.the
Firstline)atonetime,andthen
againforadifferentproductionline
(i.e.theSecondline).Romano,A.
• Isitreasonabletobelievethatthereisadifferenceinthesizepro- (1977)AppliedStatisticsforScience
ducedbetweenthetwolines? andIndustry.
Example9.5 Whatisthebestestimate(anduncertainty)foreachofthe
twoproductionlinesofballbearings?
UsingthenormalapproximationtotheStudent-Tdistribution
(Section7.4),wehavethebestestimatesofthetwolinesas
1.180000+1.420000+0.690000+ +1.190000+1.320000
µ = ···
1
10
= 1.194
1.720000+1.620000+1.690000+ +1.960000+0.990000
µ = ···
2
10
= 1.406
andtheiruncertaintiescalculatedbyfirstcalculatingthesample
deviations
(cid:114)
1
S = ((1.18 1.194)2+(1.42 1.194)2+ +(1.19 1.194)2+(1.32 1.194)2)
1
10 1 · − − ··· − −
−
= 0.289
(cid:114)
1
S = ((1.72 1.406)2+(1.62 1.406)2+ +(1.96 1.406)2+(0.99 1.406)2)
2
10 1 · − − ··· − −
−
= 0.428


[TABLE]


5 | 0 | %

25 | % | 75 | %



5 | 10
% | % | 90 | %
9 | 5%

1 | % | 99 | %

0. | 22 | 0. | 57
0. | 0.
70 | 88
1 | . | 1.
04 | 20
1. | 1.
38 | 51
1. | 86




170 statistical inference for everyone
andthenscalingthedeviationsbythenumberofdatapoints
σ = S /sqrt10=0.092
1 1
σ = S /sqrt10=0.135
2 2
yieldingthebestestimatesanduncertaintiesforthetwoproduction
lines
• Productionline1: 1.194[microns] 0.092[microns]
±
• Productionline2: 1.406[microns] 0.135[microns]
±
orlookingatthe95%CIforeachline
Thisisjustthe 2 σrange
± ·
• Productionline1: 1.01[microns]-1.378[microns]
• Productionline2: 1.136[microns]-1.676[microns]
Roughly,giventhattheseintervalsoverlap,thereisnotstrongevi-
dencethatthereisadifferencebetweenthetwolines.
Example9.6 Isitreasonabletobelievethatthereisadifferenceinthesize
producedbetweenthetwolines?
Usingthebestestimateofthedifference,weget
δ = µ µ =0.212
12 2 1
−
withtheuncertaintyinthedifferencefromtheindividualuncertain-
ties,
(cid:113)
σ = σ2+σ2 =0.163
12 1 2
Sothe2 σ uncertaintyrangeforthedifference,
·
[0.212 2 0.163,0.212+2 0.163] = [ 0.114,0.538]
− · · −
includesthevaluezero,whichweinterpretasastatementthatthe
differenceisnotstatisticallysignificant. Inotherwords,itisnotreason-
abletobelievethatthereisadifferenceinthesizeproducedbetween
thetwolines.
9.3 Beta Model - Inference About Proportions
Example9.7 TheSunriseProblem
Thesunriseproblem,asfirststatedbyLaplace,is“Whatisthe
probabilitythatthesunwillrisetomorrow?” We’llstartwiththeas-
sumptionthatinitiallyonehasneverseenasunrise,andthenobserve
ayearofsunriseseachmorningwithnomorningwithoutone. Thus

applications of parameter estimation and inference 171
wehavetheformofthedataas h successes(dayswithasunrise)in
N totaldays. Ourmodelofthedataisspecifiedasbeforewithabi-
nomialdistribution,resultingintheposteriorBeta,asdescribedin
Section6.6.
Afteraonly10yearsofwatchingsunrises,andnofailuresofa
sunrise,thebestestimatefortheprobabilityofasunriseis
h+2
θˆ
median ≈ N+4
3650+2
= =0.9995
3650+4
makingitvirtuallycertainforasunrise.
Example9.8 CancerRates
3
ThisexampleisfromDonaldBerry’sStatisticstextbook : 3D.Berry. Statistics:ABayesian
Perspective. Duxbury,1996
pp192: Astudy(MurphyandAbbey,CancerinFamilies,1959)ad-
dressedthequestionofwhethercancerrunsinfamilies. Theinvestiga-
toridentified200womenwithbreastcancerandanother200women
withoutbreastcancerandaskedthemwhethertheirmothershadhad
breastcancer. Ofthe400womeninthetwogroupscombined,10ofthe
mothershadhadbreastcancer. Ifthereisnogeneticconnection,then
abouthalfofthese10wouldcomefromeachgroup.
Thedataisthat7ofthedaughtershadcancerand3didnot. Isthere
strongevidenceofaconnection?
Theproperway,assumingtotalinitialignorance,istousetheBeta
distribution:
P(θ data) =Beta(h =7,N =10)
cancer
|
whichhasamedianof θˆ = 0.68,buta95%credibleintervalof
cancer
θˆ = 0.39upto θˆ = 0.89. Thismeansthereisnotstrong
cancer cancer
evidenceofaneffect.
Example9.9 CancerRates-NormalApproximation
WecanestimatethetheBetadistributionmedianandcredible
intervalswithaNormaldistribution,byusingthe“assuming2suc-
cessesand2failures”method.
h+2
θˆ =
cancer N+4
7+2
= =0.643
10+4
and
(cid:113)
σ = θˆ (1 θˆ )/(N+4)
cancer cancer
−
(cid:113)
= 0.643(1 0.643)/(10+4)
−
= 0.128

172 statistical inference for everyone
Sotheapproximate95%credibleintervalis
θˆ 2σ
cancer
±
whichisbetween0.387and0.899,againwiththesameconclusionof
nostrongevidenceofaneffect.
Example9.10 Willitrainonthe4th ofJuly?
IntheUnitedStates,the4th ofJulyisIndependenceDay,andis
knownforparades. Theoldestcontinuouslyrunningparadeisin
Bristol,RI,anditrunsrainorshine. Isitlikelytorainonthepa-
rade? ClimatedatafromnearbyProvidenceisherefromwunder-
ground.com:
WecanestimatethetheBetadistributionmedianandcredible
intervalswithaNormaldistribution,byusingthe“assuming2suc-
cessesand2failures”method.
h+2
θˆ =
rain N+4
19+2
= =0.404
48+4
around40%,lessthananevenchance(50%)ofrain,but
(cid:113)
σ = θˆ (1 θˆ )/(N+4)
rain rain
−
(cid:113)
= 0.404(1 0.404)/(48+4)
−
= 0.068
Sotheapproximate95%credibleintervalis
θˆ 2σ
rain
±
whichisbetween0.268and0.540. Thisisnotstrongevidenceagainst
apurelyfairandrandom“coinflip”forrainonthe4th ofJuly.
Example9.11 HotHandReexamined

applications of parameter estimation and inference 173
4
InTverskyandGilovich wehavethefollowingdataforLarry 4A.TverskyandT.Gilovich. The
Birdfreethrowsinbasketball: coldfactsaboutthe"hothand"in
basketball. Anthologyofstatisticsin
• Giveneachof53missedshots,LarryBirdsuccessfullyshot48of
sports,16:169,2005
thenextattempt.
• Giveneachof285successfulshots,LarryBirdsuccessfullyshot
251ofthenextattempt.
Thisdataalonealmostsuggestsananti-hot-hand(whereyou’re
lesslikelytomakeasuccessfulattemptfollowingasuccessfulshot).
However,wecandemonstratethatthesenumbersarenotinfact
statisticallydifferent. Giventherelativelylargenumberofattempts
(greaterthan30)wecanusetheNormalapproximationtoestimate
thetwoprobabilitiesofsuccess:
48+2
θ = =0.877
afteramiss 53+4
251+2
θ = =0.875
afterasuccess 285+4
andtheuncertainty,
(cid:113)
σ = 0.877(1 0.877)/(53+4) =0.044
afteramiss −
(cid:113)
σ = 0.875(1 0.875)/(285+4) =0.019
afterasuccess −
makingthe95%credibleintervalsforprobabilityofaLarryBird
successfulattempt
95%CI = 0.877 2 0.044= [0.789,0.965]
afteramiss ± ·
95%CI = 0.875 2 0.019= [0.837,0.913]
afterasuccess ± ·
Noticethattheintervalsoverlap,sothereisnosignificantevidence
foradifferenceinLarryBird’ssuccessfollowinganothersuccess
orfollowingamiss. Thus,thereisnosignificantevidenceforahot
hand,orananti-hothand.
9.4 Model Construction
Inpractice,weeitherdon’tknowwhattheoptimummodelweneed
is,ortheneedsofthemodelchangeasweobtainmoredata.
WestartwiththedatainTable9.4forthemassofpenniesofvari-
ousyears(showngraphicallyinFigure9.3) 5 : 5thisdatawasextractedfrom
Wearegoingtoignorethemeasurementuncertaintiesinthese studentmeasurementsduringa
physicslab
individualmeasurements,becausetheyarequitesmall.
Example9.12 MassofthePenny,Model1-OneTrueValue

174 statistical inference for everyone
Year Mass[g]
Table9.4:MassofPenniesfrom
1960to1974.
1960 3.133
1961 3.083
1962 3.175
1963 3.120
1964 3.100
1965 3.060
1966 3.100
1967 3.100
1968 3.073
1969 3.076
1970 3.100
1971 3.110
1972 3.080
1973 3.100
1974 3.093
3.20
3.15
3.10
3.05
3.00
1960 1962 1964 1966 1968 1970 1972 1974
year
]g[
ynneP
rep
ssaM
Figure9.3:MassofPenniesfrom
1960to1974.


[TABLE]













applications of parameter estimation and inference 175
Ifweassumeamodelthatstatesthatthereisa“true”valueand
thevariationfromthis“true”valuecausedbysomeunknownpro-
cess,butwithknownmagnitude, σ,
data = truevalue+Normal(mean=0,known σ)
orequivalently
data = Normal(mean=truevalue,known σ)
wecangetthebestestimateanduncertaintyinthatestimatefrom
thefollowingprocedure,Usingthenormalapproximationtothe
Student-Tdistribution(Section7.4):
µˆ = x¯ k S/√N
± ·
wherethesymbolsinthisequationare
1 thenumberofdatapoints, N.
2 thebestestimateforthetruevalue, µˆ,isgivenbythesamplemean,
x¯:
x +x + +x
x¯ = = 1 2 ··· N
N
3.133g+3.083g+ +3.093g
= ···
15
= 3.100g
3 Theuncertaintyisdirectlyrelatedtothesamplestandarddeviation,
S:
(cid:115)
(x x¯)2+(x x¯)2+ +(x x¯)2
S = 1 − 2 − ··· N −
N 1
−
(cid:114)
(3.133g 3.100g)2+(3.083 3.100g)2+ +(3.093 3.100g)2
= − − ··· −
14
= 0.0278g
4 Thescalefactor, k,adjustsforthesmallnumberofdatapoints-
thereismoreuncertaintyinourestimatewhentherearefewer
datapoints:
20
k = 1+
N2
20
= 1+
152
= 1.0889
Finally,wehavethebestestimateanduncertaintyforthepennies
inthisdataset:
µˆ = x¯ k S/√N
± ·
= 3.100g 1.0889 0.0278g/√15
± ·
= 3.100g 0.0078g
±

176 statistical inference for everyone
or,asa99%crediblerange(3timestheuncertaintywrittenabove),
wehave,(seealsoFigure9.4)
99%CIfor µ = 3.100g 3 0.0078g
± ×
= [3.077g,3.124g]
Example9.13 MassofthePenny,Model1-OneTrueValuewithMore
Data
Nowwecollecttheadditionaldatawithmorerecentpennies
showninTable9.5. Wecanfollowthesameprocedure,assuming
ouroriginalmodelofone“true”value,togetthebestestimateand
uncertaintyforthismodel,combiningthetwodatasets.
Year Mass[g]
Table9.5:MassofPenniesfrom
1989to2003.
1989 2.516
1990 2.500
1991 2.500
1992 2.500
1993 2.503
1994 2.500
1995 2.497
1996 2.500
1997 2.494
1998 2.512
1999 2.521
2000 2.499
2001 2.523
2002 2.518
2003 2.520
µˆ = x¯ k S/√N
± ·
wherethesymbolsinthisequationare
1 thenumberofdatapoints, N =30.
2 thebestestimateforthetruevalue, µˆ,isgivenbythesamplemean,
x¯:
3.133g+3.083g+ +2.520g
x¯ = ···
30
= 2.804g

applications of parameter estimation and inference 177
3.18
3.16
3.14
3.12
3.10
3.08
3.06
1960 1962 1964 1966 1968 1970 1972 1974
year
]g[
ynneP
rep
ssaM
Best estimate of "true" value: µˆ=3.100 0.0078
±
99% CI: [3.077,3.124]
60
50
40
30
20
10
0
3.00 3.05 3.10 3.15 3.20
µ [g]
)µ(p
Figure9.4:MassofPenniesfrom
1960to1974,withbestestimates
and99%CI(i.e.3σ)uncertainty.
Best Estimate for µ=3.100 0.0078 grams
±
99% CI for µ:[3.077,3.124]


[TABLE]




Best | estimate | of "true | " value:
99% | µˆ=3.100
±
CI: [3.07 | 0.0078
7,3.124]

















[TABLE]


Best Estima | te for µ=3.100 | 0.0078 grams

99% CI for µ | :[3.077,3.124] | ±
















178 statistical inference for everyone
3 Thesamplestandarddeviation, S:
(cid:114)
(3.133g 2.804g)2+(3.083 2.804g)2+ +(2.520 2.804g)2
S = − − ··· −
29
= 0.3024g
4 Thescalefactor, k,adjustingforthesmallnumberofdatapoints:
20
k = 1+
302
= 1.0222
Finally,wehavethebestestimateanduncertaintyforthepennies
inthisfulldataset:
µˆ = x¯ k S/√N
± ·
= 2.804g 1.0222 0.3024g/√30
± ·
= 2.804g 0.0564g
±
or,asa99%crediblerange(3timestheuncertaintywrittenabove),
wehave,
99%CIfor µ = 2.804g 3 0.0564g
± ×
= [2.634g,2.973g]
Thereareseveralthingsoneshouldnotice:
1 Thescalefactor, k,islessfor30datapointsthanitisfor15data
points. Thisisbecausetheadjustmentforsmallnumberofdata
pointsgetslessrelevantasweobtainmoredata. Thisiswhatwe
expect.
2 Despitetherebeingtwiceasmuchdata,ouruncertaintyincreased.
Thisisunusual,ifourmodeliscorrect-moredatashouldsharpen
theestimates. Althoughitispossiblethataddingmoredatain-
creasedthesystemvariabilitysomehow,itismorelikelythatsome
assumptionofourmodelisincorrect. Thisbecomesobviouswhen
welookattheresultgraphically,showninFigure9.5.
Thisshouldhighlightafewthings:
1 Alwayslookatyourdatagraphically. Whatyoumightmisslook-
ingatatableofnumbers,you’llcatchwithapicture.
2 Assumeyourmodeliswrong,andoutlineotherpossiblemodels
aheadoftimeandexplorethem. Themostobviousimprovement
inthisproblemistonoticethatwearedealingwithtwoseparate
“true”values,possiblycausedbyachangeinthemanufacturing
materials.

applications of parameter estimation and inference 179
3.2
3.1
3.0
2.9
2.8
2.7
2.6
2.5
2.4
1960 1965 1970 1975 1980 1985 1990 1995 2000 2005
year
]g[
ynneP
rep
ssaM
Figure9.5:MassofPenniesfrom
1960to2003,withbestestimates
and99%CI(i.e.3σ)uncertainty.
Best estimate of "true" value??: µˆ=2.804 0.0564
±
99% CI: [2.634,2.973]
Example9.14 MassofthePenny,Model2-TwoTrueValues
Inthismodel,weassumetherearetwotruevalues:
• µ -before1975
1
• µ -after1988
2
Therearetworoughlyequivalentwaysoftellingwhetherthereis
asignificantdifference.
OverlappingIntervals Thefirstistheeasiesttodomathematically,
andyieldsanicepicture: obtainthebestestimatesfor µ and µ ,
1 2
andseeiftheir99%credibleintervalsoverlap. Fromthisanalysis
(identicaltothepreviousexamples,howeverweleavethedetailsof
thecalculationtothestudent),weget(seeFigure9.6):
• Bestestimatefor µ
1
µˆ = 3.100 0.0078
1
±
with99%CI:[3.077,3.124].
• Bestestimatefor µ
2
µˆ =2.507 0.0029
2
±
with99%CI:[2.498,2.516]


[TABLE]




Best | estimat | e of "t | rue" va | lue??: | µˆ=2.8 | 04 0.0 | 564

±

99 | % CI: [2 | .634,2.9 | 73]
















180 statistical inference for everyone
wherethe99%credibleintervals(CI)clearlydonotoverlap,thus
thereisastatisticallysignificantdifferencebetweenthem.
3.2
3.1
3.0
2.9
2.8
2.7
2.6
2.5
2.4
1960 1965 1970 1975 1980 1985 1990 1995 2000 2005
year
]g[
ynneP
rep
ssaM
Figure9.6:MassofPenniesfrom
1960to2003,withbestestimates
forthetwotruevaluesandtheir
99%CI(i.e.3σ)uncertaintyplotted.
Thereisclearlynooverlapintheir
credibleintervals,thusthereisa
statisticallysignificantdifference
Best estimate µˆ =3.100 0.0078 betweenthem.
1 ±
99% CI: [3.077,3.124]
Best estimate µˆ =2.507 0.0029
2 ±
99% CI: [2.498,2.516]
IstheDifferenceZero? Theproperwayistoestimatethequantity
µ µ andtesttoseeifitisgreaterthanzero,asshowninSec-
1 2
−
tion7.2onpage144. Theestimateofthisquantity,whichwe’llcall
δ = µ µ isrelatedtothemeansanduncertaintiesoftwodata
12 1 2
−
sets
δˆ = x¯ x¯ σ
12 1 2 12
− ±
(cid:113)
σ = σ2+σ2
12 1 2
(cid:112)
σ = k S / N (uncertaintyfromdataset1)
1 1 1 1
(cid:112)
σ = k S / N (uncertaintyfromdataset2)
2 2 2 2
wherethesamplestandarddeviations, S and S ,andthescalefac-
1 2
tors, k and k werecalculatedearlier. Thisleadsto,forthisdataset,
1 2
δˆ = 0.593g 0.008g
12
±
withthe99%credibleinterval [0.568g,0.618g],thedistributionshown
inFigure9.7. Again,theestimatedquantitiesareclearlydifferentsta-
tistically: thevalueofzeroiswelloutsideofthe99%credibleinterval
for δ .
12
9.5 Computer Examples


[TABLE]










Best | estim | ate µˆ
1
99% C | =3.100
I: [3.07 | 0.0078
±
7,3.124]





B | est esti | mate
99 | µˆ =2.5
2
% CI: [2 | 07 0.0
±
.498,2.5 | 029
16]








applications of parameter estimation and inference 181
50
40
30
20
10
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
µ µ
1− 2
)
µ
µ(p
2
−1
Figure9.7:Differenceintheesti-
matedvaluesofthepre-andpost
1 z 9 er 7 o 5 i p s e c n le n a ie r s ly ,µ o 1 u − tsi µ d 2 e . o T f h t e he va 9 l 9 u % e in-
Best Estimate for µ µ =0.593 0.008 tervalofthedifference,thusthereis
1− 2 ± astatisticallysignificantdifference
99% CI for µ
1−
µ
2
:[0.568,0.618] betweenthetwovaluesµ1andµ2.
from sie import *
Iris Example
data=load_data( ’data/iris .csv ’)
x_sertosa=data[data[ ’class ’]==’Iris setosa ’][ ’petal length [cm] ’]
−
x_virginica=data[data[ ’class ’]==’Iris virginica ’][ ’petal length [cm] ’]
−
x_versicolor=data[data[ ’class ’]==’Iris versicolor ’][ ’petal length [cm] ’]
−
print x_sertosa [:10] # print the first 10
0 1.4
1 1.4
2 1.3
3 1.5
4 1.4
5 1.7
6 1.4
7 1.5
8 1.4
9 1.5
Name: petal length [cm], dtype: float64


[TABLE]


Be | st Estima | te for µ
1 | µ =0.5
− 2 | 93 0.008
±

99 | % CI for µ | µ :[0.
1− 2 | 568,0.618]















[TABLE]




from sie import *







[TABLE]




data=load_data( ’data/iris .csv ’)







[TABLE]




x_sertosa=data[data[ ’class ’]==’Iris setosa ’][ ’petal length [cm] ’]

−
x_virginica=data[data[ ’class ’]==’Iris virginica ’][ ’petal length [cm] ’]

−
x_versicolor=data[data[ ’class ’]==’Iris versicolor ’][ ’petal length [cm] ’]

−





[TABLE]




print x_sertosa [:10] # print the first 10






182 statistical inference for everyone
x=x_sertosa
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_sertosa=tdist (N,mu,sigma)
print "total number of data points:" ,N
print "best estimate:" ,mu
print "uncertainty:" ,sigma
total number of data points: 50
best estimate: 1.464
uncertainty: 0.0245381834898
x=x_versicolor
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_versicolor=tdist (N,mu,sigma)
print "total number of data points:" ,N
print "best estimate:" ,mu
print "uncertainty:" ,sigma
total number of data points: 50
best estimate: 4.26
uncertainty: 0.0664554477121
x=x_virginica
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_virginica=tdist (N,mu,sigma)
print "total number of data points:" ,N
print "best estimate:" ,mu
print "uncertainty:" ,sigma
total number of data points: 50
best estimate: 5.552
uncertainty: 0.078049696361
distplot2 ([ t_sertosa , t_versicolor , t_virginica ] ,show_quartiles=False)
<matplotlib.figure.Figure at 0x1058d9690>


[TABLE]




x=x_sertosa

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_sertosa=tdist (N,mu,sigma)



print "total number of data points:" ,N

print "best estimate:" ,mu

print "uncertainty:" ,sigma







[TABLE]




x=x_versicolor

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_versicolor=tdist (N,mu,sigma)



print "total number of data points:" ,N

print "best estimate:" ,mu

print "uncertainty:" ,sigma







[TABLE]




x=x_virginica

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_virginica=tdist (N,mu,sigma)



print "total number of data points:" ,N

print "best estimate:" ,mu

print "uncertainty:" ,sigma







[TABLE]




distplot2 ([ t_sertosa , t_versicolor , t_virginica ] ,show_quartiles=False)






applications of parameter estimation and inference 183
distplot(t_virginica)
credible_interval(t_versicolor)
(4.1265203051077082, 4.2599999999999998, 4.3934796948922914)
credible_interval(t_virginica)
(5.3952325713636533, 5.5519999999999996, 5.7087674286363459)
Sunrise


[TABLE]




distplot(t_virginica)







[TABLE]




credible_interval(t_versicolor)







[TABLE]




credible_interval(t_virginica)






184 statistical inference for everyone
dist=beta(h=365,N=365)
distplot(dist)
credible_interval(dist)
(0.98997171634278669, 0.99810794743679487, 0.99993082805373457)
Cancer Example
dist=beta(h=7,N=10)
distplot(dist , figsize =(8,5))


[TABLE]




dist=beta(h=365,N=365)







[TABLE]




distplot(dist)







[TABLE]




credible_interval(dist)







[TABLE]




dist=beta(h=7,N=10)







[TABLE]




distplot(dist , figsize =(8,5))






applications of parameter estimation and inference 185
credible_interval(dist)
(0.39025744042757882, 0.67619553741481253, 0.89073655618090186)
Essentiallynoevidenceofanyeffectover50percent.
Pennies
data1=load_data( ’data/pennies1.csv ’)
print data1
year ,mass=data1[ ’Year’] ,data1[ ’Mass [g] ’]
Year Mass [g]
0 1960 3.133
1 1961 3.083
2 1962 3.175
3 1963 3.120
4 1964 3.100
5 1965 3.060
6 1966 3.100
7 1967 3.100
8 1968 3.073
9 1969 3.076
10 1970 3.100
11 1971 3.110
12 1972 3.080
13 1973 3.100
14 1974 3.093
plot(year ,mass, ’o’)
xlabel( ’year ’)
ylabel( ’Mass per Penny [g] ’)
<matplotlib.text.Text at 0x1087c2d90>


[TABLE]




credible_interval(dist)







[TABLE]




data1=load_data( ’data/pennies1.csv ’)

print data1

year ,mass=data1[ ’Year’] ,data1[ ’Mass [g] ’]







[TABLE]




plot(year ,mass, ’o’)

xlabel( ’year ’)

ylabel( ’Mass per Penny [g] ’)






186 statistical inference for everyone
x=mass
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_penny1=tdist (N,mu,sigma)
distplot(t_penny1 , label=’mass [g] ’)
CI=credible_interval(t_penny1 ,percentage=99)
print CI


[TABLE]




x=mass

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_penny1=tdist (N,mu,sigma)



distplot(t_penny1 , label=’mass [g] ’)







[TABLE]




CI=credible_interval(t_penny1 ,percentage=99)

print CI






applications of parameter estimation and inference 187
(3.0790129206702002, 3.1002000000000001, 3.1213870793298)
plot(year ,mass, ’o’)
credible_interval_plot(t_penny1 ,percentage=99)
xlabel( ’year ’)
ylabel( ’Mass per Penny [g] ’)
<matplotlib.text.Text at 0x1087fcf10>
Dothe2datasets
data2=load_data( ’data/pennies2.csv ’)
print data2
year1 ,mass1=year ,mass
year2 ,mass2=data2[ ’Year’] ,data2[ ’Mass [g] ’]
Year Mass [g]
0 1989 2.516
1 1990 2.500
2 1991 2.500
3 1992 2.500
4 1993 2.503
5 1994 2.500
6 1995 2.497
7 1996 2.500
8 1997 2.494
9 1998 2.512
10 1999 2.521
11 2000 2.499
12 2001 2.523
13 2002 2.518


[TABLE]




plot(year ,mass, ’o’)

credible_interval_plot(t_penny1 ,percentage=99)

xlabel( ’year ’)

ylabel( ’Mass per Penny [g] ’)







[TABLE]


data2=load_data( ’data/pennies2.csv ’)

print data2

year1 ,mass1=year ,mass

year2 ,mass2=data2[ ’Year’] ,data2[ ’Mass [g] ’]






188 statistical inference for everyone
14 2003 2.520
x=mass1
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_penny1=tdist (N,mu,sigma)
x=mass2
mu=sample_mean(x)
N=len(x)
sigma=sample_deviation(x)/sqrt(N)
t_penny2=tdist (N,mu,sigma)
distplot2 ([t_penny1 ,t_penny2] ,show_quartiles=False , label=’mass [g] ’)
legend([r ’$\mu_1$’ ,r ’$\mu_2$’])
<matplotlib.figure.Figure at 0x1087d3f10>
<matplotlib.legend.Legend at 0x1088198d0>
plot(year1 ,mass1, ’o’)
credible_interval_plot(t_penny1 ,percentage=99)
plot(year2 ,mass2, ’ro’)
credible_interval_plot(t_penny2 ,percentage=99,xlim=[1989,2005])
xlabel( ’year ’)
ylabel( ’Mass per Penny [g] ’)
<matplotlib.text.Text at 0x10907e310>


[TABLE]




x=mass1

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_penny1=tdist (N,mu,sigma)



x=mass2

mu=sample_mean(x)

N=len(x)

sigma=sample_deviation(x)/sqrt(N)

t_penny2=tdist (N,mu,sigma)



distplot2 ([t_penny1 ,t_penny2] ,show_quartiles=False , label=’mass [g] ’)

legend([r ’$\mu_1$’ ,r ’$\mu_2$’])







[TABLE]




plot(year1 ,mass1, ’o’)

credible_interval_plot(t_penny1 ,percentage=99)

plot(year2 ,mass2, ’ro’)

credible_interval_plot(t_penny2 ,percentage=99,xlim=[1989,2005])

xlabel( ’year ’)

ylabel( ’Mass per Penny [g] ’)






applications of parameter estimation and inference 189
Distributionofthedifference,normalapproximation
N1=len(mass1)
N2=len(mass2)
mu1=sample_mean(mass1)
mu2=sample_mean(mass2)
sigma1=(1+20.0/N1
**
2)*sample_deviation(mass1)/sqrt(N1)
sigma2=(1+20.0/N2
**
2)*sample_deviation(mass2)/sqrt(N1)
delta_12=mu1 mu2
−
sigma_delta12=sqrt(sigma1
**
2+sigma2
**
2)
dist_delta=normal(delta_12 ,sigma_delta12)
distplot(dist_delta)


[TABLE]


N1=len(mass1)

N2=len(mass2)



mu1=sample_mean(mass1)

mu2=sample_mean(mass2)





sigma1=(1+20.0/N1 2)*sample_deviation(mass1)/sqrt(N1)
**

sigma2=(1+20.0/N2 2)*sample_deviation(mass2)/sqrt(N1)
**





delta_12=mu1 mu2

−
sigma_delta12=sqrt(sigma1 2+sigma2 2)
** **



dist_delta=normal(delta_12 ,sigma_delta12)

distplot(dist_delta)






190 statistical inference for everyone
clearlylargerthanzeroatwelloverthe99
Ball Bearing Sizes
data1=[1.18 ,1.42 ,0.69 ,0.88 ,1.62 ,1.09 ,1.53 ,1.02 ,1.19 ,1.32]
data2=[1.72 ,1.62 ,1.69 ,0.79 ,1.79 ,0.77 ,1.44 ,1.29 ,1.96 ,0.99]
N1=len(data1)
N2=len(data2)
mu1=sample_mean(data1)
mu2=sample_mean(data2)
print mu1,mu2
1.194 1.406
S1=sample_deviation(data1)
S2=sample_deviation(data2)
print S1,S2
0.289681817786 0.428309337849
sigma1=S1/sqrt(N1)
sigma2=S2/sqrt(N2)
print sigma1,sigma2
0.091605434094 0.135443305072
dist1=normal(mu1,sigma1)
dist2=normal(mu2,sigma2)
distplot2 ([dist1 , dist2] ,show_quartiles=False , label=’size [microns] ’)
legend([r ’$\mu_1$’ ,r ’$\mu_2$’])


[TABLE]




data1=[1.18 ,1.42 ,0.69 ,0.88 ,1.62 ,1.09 ,1.53 ,1.02 ,1.19 ,1.32]

data2=[1.72 ,1.62 ,1.69 ,0.79 ,1.79 ,0.77 ,1.44 ,1.29 ,1.96 ,0.99]

N1=len(data1)

N2=len(data2)







[TABLE]




mu1=sample_mean(data1)

mu2=sample_mean(data2)

print mu1,mu2







[TABLE]




S1=sample_deviation(data1)

S2=sample_deviation(data2)

print S1,S2







[TABLE]




sigma1=S1/sqrt(N1)

sigma2=S2/sqrt(N2)

print sigma1,sigma2







[TABLE]




dist1=normal(mu1,sigma1)

dist2=normal(mu2,sigma2)

distplot2 ([dist1 , dist2] ,show_quartiles=False , label=’size [microns] ’)

legend([r ’$\mu_1$’ ,r ’$\mu_2$’])






applications of parameter estimation and inference 191
<matplotlib.figure.Figure at 0x105d61390>
<matplotlib.legend.Legend at 0x108ca1ad0>


[TABLE]











10 Multi-parameter Models
Wehavealreadymetexamplesofmultipleparameterestimationin
thecaseofunknownuncertainty,wherewehavetoestimateboth
the“true”value, µ,andtheuncertainty, σ. Inthischapter,weintro-
ducethemodeloflinearregression,whichhasmultiple“true”value
parametersandtheiruncertainty. Inthesimplecases,wecancalcu-
latetheestimatesbyhandandapplythesametestingprocedures
asdescribedinChapter8(CommonStatisticalSignificanceTestson
page159). Inthemorecomplexcaseswewillhavetorelyonthe
computertogiveustheestimates,butwecanstillinterpretthemin
thesamewayasbefore.
10.1 Simple Linear Regression
Insimplelinearregression,wearegivendataconsistingoftwovari-
ables,typicallydenoted x and y,wherethevalueofone(y)depends
ontheother(x). Forexample,considerthefollowingdataofheights
1
(x)andshoesizes(y)ofasmallnumberofindividuals shownin 1
Table10.1andFigure10.1. Byeyewecanseeadirectcorrelation-the
tallerthepersonthelargershoesize.
Height[inches] ShoeSize Table10.1:Heights(ininches)and
shoesizesfromasubsetofMcLaren
64.0 7
(2012)data.
70.0 9
64.0 8
71.0 11
69.0 12
68.0 9
69.0 10
61.0 6
68.0 10
70.0 9
Weproposeamodelofthisdataofthefollowinglinearform:
y = mx+b

194 statistical inference for everyone
14
12
10
8
6
4
60 62 64 66 68 70 72
Height [inches]
eziS
eohS
Figure10.1:Heights(ininches)and
shoesizesfromasubsetofMcLaren
(2012)data.
where m istheslopeand b istheintercept. Clearlythisdatadoesn’t
formaperfectline,sothereissomeuncertaintyintheslope,inter-
cept,andpredicted y values. WeassumeaNormaldistributionfor
theuncertaintiesinthedata,sothestatisticalmodellookslike,for
eachdatapoint,
y = mx +b+Normal(0,σ)
i i
wherewewanttoobtainestimates, mˆ and bˆ,ofthe“true”valuesof
theslopeandintercept,respectively,aswellastheiruncertainties.
Thisisobtainedbygettingtheposteriorprobabilityoftheparame-
ters,
P(m,b data)
|
Followingourstandardprocedure,
1 Specifythepriorprobabilitiesfortheparametersbeingconsidered.
Formostsimplecaseswebeginwithabsolutelynoknowledgeof
itsvalue,andthususeauniformpriorprobabilityforeachparame-
ter.
2 WritethetopofBayes’Rule,
P(m,b data) P(data m,b) P(m,b)
| ∼ | ×
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
Normaluncertainties uniformprior


[TABLE]















multi-parameter models 195
3 Addupthevalues,anddividebythissumtogetthefinalpos-
teriorprobabilities. Thisisdonebythemathematicians,andwe
simplysummarizetheresultshere.
weobtaintheposteriordistributionsfortheparameters m and b.
Thecalculationsgettoodetailedtodobyhand,butareveryeasy
withthecomputer. FortheshoesizedatainTable10.1wegetthe
distributionsshowninFigures10.2and 10.3fortheslopeandinter-
cept,respectively. Themostprobablevaluesthenleadtothebestfit,
showninFigure10.4.
TheStudent-t testclearlyshowsthattheslopeisnon-zero(well
over95%ofthedistributionliestotherightofzero),denotingasta-
tisticallysignificanteffectonshoesizefromheight. Themagnitudeof
theslope,slope = 0.42,canbeinterpretedthateveryinchofheight
leadstoa0.42increaseinshoesizeonaverage.
4
3
2
1
0
0.0 0.2 0.4 0.6 0.8
Slope
)epolS(P
Figure10.2:Posteriordistribution
fortheslopeforthelinearmodelon
50% theshoesizedatasubset.
25% 75%
10% 90%
5% 95%
1% 99%
0.22 0.35 0.50 0.62
0.11 0.27 0.42 0.57 0.73
Mean Squared Error
Anotherwayoflookingatthesameideaistointroducethenotion
ofMeanSquaredError(MSE).Thisisdefinedtobethenumberre-
sultingfromtakingthepredictedvaluesminustheobservedvalues,
squaringthem,andtakingtheirmean. Thesquaringensuresthat
deviationsfromthepredictionsbothtoohighandtoolowarecon-
sideredthesame. Thecloserthepredictionoverall,thesmallerthe
resultingMSE.Mathematicallythisiswrittenas
(cid:16) (cid:17)2
∑ y (mˆx +bˆ)
i i − i
MSE
≡ N


[TABLE]


50 | %

25 | % | 75 | %



5 | 10
% | % | 90 | % | 95 | %

1 | % | 99 | %

0. | 11 | 0. | 22
0. | 0.
27 | 35 | 0. | 0.
42 | 50
0. | 57 | 0. | 62
0. | 73




196 statistical inference for everyone
0.06
0.05
0.04
0.03
0.02
0.01
0.00
50 40 30 20 10 0 10
Intercept
)tpecretnI(P
Figure10.3:Posteriordistribution
fortheinterceptforthelinear
50% modelontheshoesizedatasubset.
25% 75%
10% 90%
5% 95%
1% 99%
-32.75 -24.38 -14.13 -5.77
-40.27 -29.39 -19.26 -9.12 1.76
14
12
10
8
6
4
60 62 64 66 68 70 72
Height [inches]
eziS
eohS
Figure10.4:Bestlinearfitforthe
shoesizedatasubset.
y=0.422x 19.256
−


[TABLE]


5 | 0%

25 | % | 75 | %





5 | 1
% | 0% | 9 | 0 | %
95 | %

1 | % | 99 | %



-40 | -32
.27 | .75
-2 | -24
9.39 | .38
-19 | -14
.26 | .13
-9 | . | -5.
12 | 77 | 1.7 | 6





[TABLE]


y=0.42 | 2x 19 | .256

−










multi-parameter models 197
Onecanintuitivelythinkofgettingthebestfitasadjustingtheslopes
andintercepts,calculatingtheMSEforeach,andstoppingwhenyou
reachaminimumvalue. AnexampleofthisisshowninFigure10.5.
16
14
12
10
8
6
4
60 62 64 66 68 70 72
Height [inches]
eziS
eohS
Figure10.5:MinimizingtheMean
SquaredError(MSE)resultsinthe
bestlinearfitfortheshoesizedata
MSE=0.9 subset.
MSE=1.4
MSE=4.2
MSE=9.9
An Educational Example
Thefollowingexampleisfromadatasetonschoolexpendituresand
2
SATscores. WeplotthetotalSATscoresasafunctionofexpendi- 2
tures,performalinearmodelfit,andpresentthebestvaluesand
theiruncertaintiesinFigure10.6. Themodelis
total = intercept+slope expenditure
·
Whatisimmediatelyoddisthatthisresultseemstosuggestthe
following:
1 ThelargertheexpenditureperpupilthelowertheSATscores.
2 Foreachthousanddollarsspentperpupil,thetotalSATscoregoes
down20points.
3 Ifyouspentzerodollarsperpupil,you’dreachamaximumof
SATscoreof1089.


[TABLE]


M
M | SE=0.9
SE=1.4

M
M | SE=4.2
SE=9.9












198 statistical inference for everyone
1150
1100
1050
1000
950
900
850
800
3 4 5 6 7 8 9 10
Expenditure [per pupil, thousands]
latoT
TAS
y= 20.892x+1089.294
−
0.06
0.05
0.04
0.03
0.02
0.01
0.00
40 30 20 10 0
Slope
)epolS(P
50%
0.010
0.008
0.006
5% 95% 0.004
1% 99% 0.002
0.000
-33.18 -8.60
-38.53 -20.89 -3.26
950 1000 1050 1100 1150 1200
Intercept
)tpecretnI(P
50%
5% 95%
1% 99%
1014.84 1163.75
982.47 1089.29 1196.12
Figure10.6:TotalSATscorevs
expenditure(top)andthedistribu-
tionsfortheslope(bottomleft)and
intercept(bottomright).


[TABLE]


y= 2 | 0.892x+108 | 9.294

−















[TABLE]


50 | %







5 | % | 95 | %

1 | % | 99 | %



-3 | 8 | -33
.53 | .18 | -20 | . | -
89 | 8. | 60
-3. | 26





[TABLE]


50 | %







1 | % | 5 | % | 95 | %
99 | %



982 | 1
.47 | 01 | 4.84 | 108 | 9. | 1
29 | 16 | 3.75
119 | 6.12




multi-parameter models 199
Thisseemscounterintuitivetosaytheleast. Whatisgoingon
here? Whatishappeningisthatthereareothervariablesthatare Thisisperhapsthemostimportant
relatedtotheexpenditurewhichthenleadtolowerSATscoreson lessonofregression.Whenyousee
aneffect,makesuretothinkofany
average. Suchaconfoundingvariableneedstobetakenintoaccountin
variablesthatmightalsobeaffected
whatiscalledcontrollingforavariable. thatmaygiverisetotheillusion
ofaneffect.Itiscriticalthatone
Forexample,ifwelookattherelationshipbetweenexpenditure
getinthishabit,oryouwillbeat
perpupilandthepercentofstudentstakingtheSATweseeapat- thewhimofeveryunscrupulous
tern,showninFigure10.7. Themorethatisspentperpupil,the statistician.
morestudents-bothbadandgood-taketheSAT.Thus,evenifex-
penditurehelpsstudents,thefactthatthepercentageofstudents
takingtheexamincreasescreatestheillusionoftheopposite. The
nextsectionstateshowyoucanovercomethisproblem.
10.2 Multiple regression
Inordertocontrolforavariablethatmaybeaffectingourresult,
wesimplyexpandourlinearmodel,includingslopes(alsocalled
coefficients)foreachofthedifferentvariables. Oncewedothis,visu-
alizationbecomeschallengingbecausewemoveintothreeormore
dimensions. Insteadof m fortheslope,themultipleslopesaretyp-
icallylabeledwiththegreekletter β andnumbered,suchas β ,β ,
1 2
etc... Theinterceptisthenlabeled β . Themodelstructure,however,
0
isthesame,andcanbewritten
y = β +β x +β x
0 1 1 2 2
···
wherethedifferent x , x ,etc... denotedifferentvariables. Forthe
1 2
exampleoftheSATscores,wemighthave
total = β +β expenditure+β percent_taking
0 1 2
· ·
wherepercent_takingisavariablerepresentingthepercentofstu-
dentstakingtheexam. Includingthisvariablegivestheposterior
distributionsshowninFigure10.8. Noticethattheeffectofexpendi-
tureisbothstatisticallysignificantandpositive. Wecaninterpretthe
valuesinthefollowingway.
• Foreach$1000morespentperpupilthetotalSATscoreincreases
onaverageby12.29.
• ForeachpercentincreaseinstudentstakingtheSAT,thetotalSAT
scoredecreasesonaverageby2.29.
Havewecontrolledforalloftheeffects? Perhapsnot! Thisis
wheretheingenuityandexpertiseofthepersonanalyzingtheprob-
lemcomesintoplay.

200 statistical inference for everyone
90
80
70
60
50
40
30
20
10
0
3 4 5 6 7 8 9 10
Expenditure [per pupil, thousands]
TAS
eht
gnikaT
stnedutS
fo
egatnecreP
y=11.638x 33.485
−
0.20
0.15
0.10
0.05
0.00
6 8 10 12 14 16 18
Slope
)epolS(P
0.035
50%
0.030
0.025
0.020
0.015
5% 95%
0.010
1% 99%
0.005
0.000
7.81 15.47
6.14 11.64 17.13
60 40 20 0
Intercept
)tpecretnI(P
50%
5% 95%
1% 99%
-56.68 -10.29
-66.77 -33.48 -0.20
Figure10.7:Percentofstudents
takingtheSATvsperpupilexpen-
diture(top)andthedistributions
fortheslope(bottomleft)and
intercept(bottomright).


[TABLE]


y=11. | 638x 33.48 | 5

−



















[TABLE]


50 | %





5 | % | 95 | %

1 | % | 99 | %

6. | 7.
14 | 81 | 11 | .6 | 4 | 15 | .4 | 7
17 | .13





[TABLE]




50 | %







5 | % | 95 | %

1 | % | 99 | %



-66 | -
.77 | 56 | .68 | -33 | .48 | -10 | .29
-0. | 20




multi-parameter models 201
0.10
0.08
0.06
0.04
0.02
0.00
0 5 10 15 20 25
βexpenditure
)erutidnepxeβ(P
50%
5% 95%
1% 99%
5.20 19.37
2.11 12.29 22.46
2.0
1.5
1.0
0.5
0.0
3.4 3.2 3.0 2.8 2.6 2.4 2.2
βpercenttaking
)gnikattnecrepβ(P
50%
5% 95%
1% 99%
-3.21 -2.49
-3.37 -2.85 -2.33
0.020
0.015
0.010
0.005
0.000
940 960 980 1000 1020 1040 1060
Intercept
)tpecretnI(P
Figure10.8:Theposteriordis-
tributionsforcoefficientsonthe
expenditureterm,thepercent
takingterm,andtheintercept.
50%
5% 95%
1% 99%
957.20 1030.47
941.25 993.83 1046.41


[TABLE]


50 | %





5 | % | 95 | %

1 | % | 99 | %



2. | 5.2
11 | 0 | 12 | .29 | 19 | .3 | 7
22 | .46





[TABLE]


50 | %





5 | % | 95 | %

1 | % | 99 | %

- | 3 | -3.
.37 | 21 | -2. | 85 | -2. | 49 | -2. | 33





[TABLE]


50 | %





5 | % | 95 | %

1 | % | 99 | %

94 | 957
1.25 | .20 | 993 | .83 | 103 | 0.47 | 104 | 6.41




202 statistical inference for everyone
10.3 Polynomial Regression
Asubsetmultipleregressionispolynomialregression,wherethevari-
ableyouarepredictingdependsonthe(usuallysingle)dependent
variablewithalargerexponentthanlinear,e.g. quadratic,cubic,etc...
10.4 Computer Examples
from sie import *
data=load_data( ’data/shoesize. xls ’)
data.head()
Index Gender Size Height
0 1 F 5.5 60
1 2 F 6.0 60
2 3 F 7.0 60
3 4 F 8.0 60
4 5 F 8.0 60
import random
random.seed(102)
rows = random.sample(data.index , 10)
newdata=data. ix[rows]
data=newdata
data
Index Gender Size Height
60 61 F 7.0 64
251 252 M 9.0 70
69 70 F 8.0 64
290 291 M 11.0 71
247 248 M 12.0 69
156 157 F 9.5 68
231 232 M 10.0 69
17 18 F 6.5 61
216 217 M 10.0 68
252 253 M 9.0 70
plot(data[ ’Height’] ,data[ ’Size ’] , ’o’)
gca(). set_xlim([60 ,72])
gca(). set_ylim([4 ,14])


[TABLE]




from sie import *







[TABLE]




data=load_data( ’data/shoesize. xls ’)







[TABLE]




data.head()







[TABLE]




import random







[TABLE]




random.seed(102)

rows = random.sample(data.index , 10)

newdata=data. ix[rows]

data=newdata

data







[TABLE]




plot(data[ ’Height’] ,data[ ’Size ’] , ’o’)

gca(). set_xlim([60 ,72])

gca(). set_ylim([4 ,14])




multi-parameter models 203
xlabel( ’Height [inches] ’)
ylabel( ’Shoe Size ’)
<matplotlib.text.Text at 0x10adae0d0>
result=regression( ’Size ~ Height’ ,data)
<matplotlib.figure.Figure at 0x10d200710>
<matplotlib.figure.Figure at 0x10d702610>


[TABLE]


xlabel( ’Height [inches] ’)

ylabel( ’Shoe Size ’)







[TABLE]




result=regression( ’Size ~ Height’ ,data)






204 statistical inference for everyone
plot(data[ ’Height’] ,data[ ’Size ’] , ’o’)
h=linspace(60,72,10)
plot(h, result[ ’_Predict ’](Height=h) , ’ ’)
−
gca(). set_xlim([60 ,72])
gca(). set_ylim([4 ,14])
xlabel( ’Height [inches] ’)
ylabel( ’Shoe Size ’)
b=result . Intercept .mean()
m=result .Height.mean()
if b>0:
text(62,12, ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)
else :
text(62,12, ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)


[TABLE]




plot(data[ ’Height’] ,data[ ’Size ’] , ’o’)



h=linspace(60,72,10)

plot(h, result[ ’_Predict ’](Height=h) , ’ ’)

−

gca(). set_xlim([60 ,72])

gca(). set_ylim([4 ,14])

xlabel( ’Height [inches] ’)

ylabel( ’Shoe Size ’)



b=result . Intercept .mean()

m=result .Height.mean()



if b>0:

text(62,12, ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)

else :

text(62,12, ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)






multi-parameter models 205
data=load_data( ’data/sat .csv ’)
result=regression( ’total ~ expenditure ’ ,data)
<matplotlib.figure.Figure at 0x1109156d0>
<matplotlib.figure.Figure at 0x110953110>


[TABLE]




data=load_data( ’data/sat .csv ’)







[TABLE]




result=regression( ’total ~ expenditure ’ ,data)






206 statistical inference for everyone
plot(data[ ’expenditure ’] ,data[ ’total ’] , ’o’)
xlabel( ’Expenditure [per pupil , thousands] ’)
ylabel( ’SAT Total ’)
h=linspace(3,10,10)
plot(h, result[ ’_Predict ’](expenditure=h) , ’ ’)
−
b=result . Intercept .mean()
m=result .expenditure.mean()
if b>0:
text(4.5,1125, ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)
else :
text(4.5,1125, ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)


[TABLE]




plot(data[ ’expenditure ’] ,data[ ’total ’] , ’o’)

xlabel( ’Expenditure [per pupil , thousands] ’)

ylabel( ’SAT Total ’)

h=linspace(3,10,10)

plot(h, result[ ’_Predict ’](expenditure=h) , ’ ’)

−

b=result . Intercept .mean()

m=result .expenditure.mean()



if b>0:

text(4.5,1125, ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)

else :

text(4.5,1125, ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)






multi-parameter models 207
result=regression( ’percent_taking ~ expenditure ’ ,data)
<matplotlib.figure.Figure at 0x111cfff10>
<matplotlib.figure.Figure at 0x111867750>


[TABLE]




result=regression( ’percent_taking ~ expenditure ’ ,data)






208 statistical inference for everyone
plot(data[ ’expenditure ’] ,data[ ’percent_taking ’] , ’o’)
xlabel( ’Expenditure [per pupil , thousands] ’)
ylabel( ’SAT Total ’)
h=linspace(3,10,10)
plot(h, result[ ’_Predict ’](expenditure=h) , ’ ’)
−
b=result . Intercept .mean()
m=result .expenditure.mean()
if b>0:
text (4.5 ,85 , ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)
else :
text (4.5 ,85 , ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)


[TABLE]




plot(data[ ’expenditure ’] ,data[ ’percent_taking ’] , ’o’)

xlabel( ’Expenditure [per pupil , thousands] ’)

ylabel( ’SAT Total ’)

h=linspace(3,10,10)

plot(h, result[ ’_Predict ’](expenditure=h) , ’ ’)

−

b=result . Intercept .mean()

m=result .expenditure.mean()



if b>0:

text (4.5 ,85 , ’$y=%.3f x + %.3f$ ’ % (m,b) ,fontsize=30)

else :

text (4.5 ,85 , ’$y=%.3f x %.3f$ ’ % (m,b) ,fontsize=30)






multi-parameter models 209
result=regression( ’total ~ expenditure + percent_taking ’ ,data)
<matplotlib.figure.Figure at 0x1107f5fd0>
<matplotlib.figure.Figure at 0x10d70a690>


[TABLE]




result=regression( ’total ~ expenditure + percent_taking ’ ,data)






210 statistical inference for everyone
<matplotlib.figure.Figure at 0x110fbcf90>


[TABLE]









11 Introduction to MCMC
Oncetheproblemsgettoasufficientcomplexity,theanalyticaltools
andapproximationswehaveemployedinpreviouschapterswillno
longerworkwell. Inthosecases,weturntosimulationtechniques,
oneofwhichisMarkovChainMonteCarlo(MCMC).Itiswellbe-
yondthisbooktotalkaboutthedetailsofthisprocess,butthebasic
processisthefollowing.
Westartwithamodelofthesystem,suchasthebentcoinmodel
inSection6.3. Inthatsystem,wetrytoestimatetheprobabilitythata
particulardoingwillflipheads,quantifiedbytheparameter θ which
cantakeonvaluesfrom θ = 0(i.e. acoinwhichonlyflipstails)
through θ = 0.5(i.e. a“fair”coinwhichflipstailsandheadsequally)
upto θ = 1(i.e. acoinwhichonlyflipsheads). Ourdataconsistsof
atotalnumberofflips, N,andhowmanyareheads, h. Althoughthis
problemcanbedoneanalytically,itisinstructivetowalkthrough
thesolvedproblemwiththenewmethodbeforelookingatmore
complexmodels.
MCMCproceeds,roughly,withthefollowingsteps
1 Manyrandom“walkers”areconstructed,eachwitharandom
valueoftheparameters(e.g. θ inthiscase).
2 Therandomvaluesarechosenfromthepriorprobabilityofthe
parameters. (e.g. uniforminthiscase, P(θ) =1)
3 The“walkers”movearoundrandomly,guidedbythelikelihood
function(e.g. theBinomialorBernoullidistribution,inthiscase)
4 Overhundredsorthousandsofsteps,thedistributionoftheval-
uesbeingexploredbythe“walkers”matchestheposteriordistri-
bution,soonecanlookathistogramsoftheresulting“walkers”to
getestimatesoftheparameters,andtheiruncertainty
11.1 One-Dimensional Models
Themodelwefirstlookatisthecoinflipmodel: given17heads
in25flips,whatistheprobabilitydistributionofthethemeasure

212 statistical inference for everyone
ofthecoin’sbent-ness, θ. Weknowthesolutionisoftheformofa
betadistribution,butweperformthesameanalysiswiththeMCMC
technique.
h,N=data=17,25
def P_data(data,theta):
h,N=data
distribution=Bernoulli(h,N)
return distribution(theta)
model=MCMCModel(data,P_data,
theta=Uniform(0,1))
Figure11.1:So-calledMCMC
“chains”forparameterθversus
time.Observethatthevaluesofθ
model.run_mcmc(500) startspreadevenlyfrom0to1at
model.plot_chains() thebeginningandthenthindown
toarangeofabout0.5-0.8withthe
middlearound0.7(17/25=0.68).
Reading the Output
Wecannowplotthedistributionsoftheparameters,just θ inthis
case,yieldingbest-fits,uncertainties,etc...
model.plot_distributions()
(seeFigure11.2)
Wecanfurtherperformsomesimplecalculationsontheprobabili-
tiesfortheparameters,suchas
model.P(’theta>0.5’)
0.96173333333333333

introduction to mcmc 213
Figure11.2:Distributionofθ,and
the95%credibleinterval.
model.P(’(0.2<theta) & (theta<.5)’)
0.038266666666666664
11.2 Multi-Dimensional Models
Itisstraightforwardthentoincludemorethanoneparameterandto
doregressionusingthistechnique. Forexample,hereisanexample
withsomeartificialdata,
def linear(x,a,b):
return a*x+b
model=MCMCModel_Regression(x,y,linear,
a=Uniform(-10,10),
b=Uniform(0,100),
)
model.run_mcmc(500)
model.plot_chains()
Figure11.3:Chainsforparameters
a,b,andthenoiseσ.

214 statistical inference for everyone
plot(x,y,’o’)
model.plot_predictions(xfit,color=’g’)
Figure11.4:Data(blue)andpre-
dictions(green)forthemodel-the
widthofthepredictionsdemon-
stratestheuncertainty.
model.plot_distributions()
Andwecanlookatbestestimates,quartiles,andprobabilitycom-
parisons,
model.percentiles([5,50,95])
{’_sigma’: array([ 0.97143798, 1.00744104, 1.0467333 ]),
’a’: array([ 0.07063144, 0.24939562, 0.42523751]),
’b’: array([ 39.88446461, 39.98633744, 40.09010139])}

introduction to mcmc 215
Figure11.5:Distributionsfor
parametersaandb(slopeand
intercept).
model.P(’a>0’)
0.98936000000000002
11.3 Hierarchical Model Example - Kruschke BEST Test
Acomparisonbetweenmeansisastandardstatisticaltechnique.
However,usingahierarchicalmodelcanbesuperiortothetypical
1
tests. 1
Inthisexample,weusetheKruschkeBEST Testtocomparethe
differencebetweenatreatmentandcontrol-wewanttoobtainthe
bestestimateofthedifferencebetweenthemeansofvariables. With
theMCMCtechnique,wecanachieveitwiththefollowing,
from sie import *

216 statistical inference for everyone
drug = (101,100,102,104,102,97,105,105,98,
101,100,123,105,103,100,95,102,106,
109,102,82,102,100,102,102,101,102,
102,103,103,97,97,103,101,97,104,
96,103,124,101,101,100,101,101,104,
100,101)
placebo = (99,101,100,101,102,100,97,101,
104,101,102,102,100,105,88,101,100,
104,100,100,100,101,102,103,97,101,
101,100,101,99,101,100,100,
101,100,99,101,100,102,99,100,99)
model=mcmc.BESTModel(drug,placebo)
model.run_mcmc()
Running MCMC...
Done.
5.80 s
model.names
[’mu1’, ’mu2’, ’sigma1’, ’sigma2’, ’nu’]
model.plot_chains(’mu1’)
model.plot_distribution(’mu1’)

introduction to mcmc 217
Figure11.6:Chainsforparameter
mu 1,themeanofthedruggroup.
Figure11.7:Distributionforpa-
rametermu 1,themeanofthedrug
group.

218 statistical inference for everyone
model.plot_distribution(’mu2’)
Figure11.8:png
model.plot_distribution(r’$\delta$=mu1-mu2’)
Figure11.9:Distributionforpa-
rameterδ,themeanofthedifference
betweenthedruggroupandthe
placebogroup.
Wecanclearlyseefromthedistributionof δ,aswellasthecred-
ibleranges,thatthereissignificantevidenceforanon-zeroeffect.
Wewouldwanttoextendthistoincludetheeffectsize,andexplore
thepriorprobabilityofthethedrugworking,inordertoreasonably
assesswhetherthisisaneffectworthpursuing.

12 Concluding Thoughts
12.1 Where have we come?
Wehavetriedinthisbooktopresentaparticularpictureofthe
world: everythingisprobability. Westartedwithbasicdefinitions
andapplications,andfollowedtheconsequencesoftherulesofprob-
abilitytoexaminemorecomplexproblems. Itisourhopethatthe
readerseesthatalloftheanalysisstemsfromasingleperspective. In
thisway,onecanapproachanyproblemofinferenceinaunifiedway,
applyingtherecipewe’veusedthroughout:
1 Proposeamodelforthedatayouobserve(whichcouldbeas
simpleas“thereisanunknowntruevaluefortheobservations”)
2 Specifyyourpriorknowledgeoftheparametersinthemodel,in
theformofapriorprobability(whichisoftenassimpleas“Idon’t
knowanythingabouttheparameters,soallpossiblevaluesare
equallylikely”)
3 Specifyhowlikelyyourdatawouldbeifyourmodelweretrue,
whichisthelikelihoodpartofBayes’rule
4 Applytherulesofprobability,namelyBayes’rule,todetermine
theposteriorprobabilityfortheparametersinthemodel
5 Usethepropertiesofprobabilityfunctionstocalculateanswers
tospecificquestions,forexample“isitlikelythatthisnumberis
greaterthanzero?” or“arethesetwomeasurementsdifferent?”
AlthoughIhaven’tcoveredallpossibleexamples,andthereare
additionsandclarificationsstillplanned,thisapproachcanbeused
forallnewproblemsonefaces. Theonlystepsthatcanbedaunting,
attimes,isthemathematicalconsequencesandeventherewehave
seenthatthejudicioususeofapproximationscangoalongway.

220 statistical inference for everyone
12.2 Where are we going?
TopicsI’dlovetoadd,andwillwhenIhavethechance,include(in
noparticularorder),
• MeasurementinScience
• LinearRegressionandCorrelation
• Two-sampleinferences
• Classification
• ModelBuildinginScience
• AnalysisofSocialScienceData
• InferenceforDeviationParameters
• ExperimentalDesign
• Computersimulations(e.g. MCMC)

Bibliography
Paultheoctopus,July2012. URLhttp://en.wikipedia.org/wiki/
Psychic_octopus.
AlanAgrestiandBrianCaffo. Simpleandeffectiveconfidence
intervalsforproportionsanddifferencesofproportionsresultfrom
addingtwosuccessesandtwofailures. TheAmericanStatistician,54
(4):280–288,2000.
K.BacheandM.Lichman. UCImachinelearningrepository,2013.
URLhttp://archive.ics.uci.edu/ml.
D.Berry. Statistics: ABayesianPerspective. Duxbury,1996.
A.Gelman,J.Hill,andEbooksCorporation. Dataanalysisusing
regressionandmultilevel/hierarchicalmodels,volume625. Cambridge
UniversityPressCambridge,UK:,2007.
DavidJHand,FergusDaly,KMcConway,DLunn,andEOs-
trowski. Ahandbookofsmalldatasets,volume1. CRCPress,2011.
LHeaps. Operationmorninglight. Paddington,S.l,1978. ISBN
0709203233.
E.T.Jaynes. ProbabilityTheory: TheLogicofScience. Cambridge
UniversityPress,Cambridge,2003. EditedbyG.LarryBretthorst.
LordJusticeKay. RvsSallyClark,April2003. URLhttp://www.
bailii.org/ew/cases/EWCA/Crim/2003/1020.html.
D.V.LindleyandL.D.Phillips. Inferenceforabernoulliprocess(a
bayesianview). TheAmericanStatistician,30(3):112–119,1976.
SharonMcGrayne. TheTheoryThatWouldNotDie: HowBayes’
RuleCrackedtheEnigmaCode,HuntedDownRussianSubmarines,
andEmergedTriumphantfromTwoCenturiesofControversy. YaleUni-
versityPress,2011. ISBN0300169698.
JamesOberg. U.S.satelliteshootdown: Theinsidestory. IEEE
Spectrum,2008.

222 statistical inference for everyone
J.Randi. Flim-flam!: psychics,ESP,unicorns,andotherdelusions,vol-
ume342. PrometheusBooksAmherst,NY,1982.
CarlSagan. Demon-HauntedWorld: ScienceasaCandleintheDark.
RandomHouseLLC,1996.
J.Sullivan. Peoplev.Collins,68cal.2d319,1968. URLhttp:
//scocal.stanford.edu/opinion/people-v-collins-22583.
A.TverskyandT.Gilovich. Thecoldfactsaboutthe"hothand"in
basketball. Anthologyofstatisticsinsports,16:169,2005.
A.TverskyandD.Kahneman. Judgmentunderuncertainty: Heuris-
ticsandbiases. Science,185(4157):1124,1974.
A.TverskyandD.Kahneman. Extensionalversusintuitivereason-
ing: Theconjunctionfallacyinprobabilityjudgment. Psychological
review,90(4):293,1983.

Appendix A
Computational Analysis
Thebookiswrittenwithanaccompanyingsoftwarepackage,writ-
teninPython. Asofthiswritingtherecommendeddistributionfor
installingpythonistheAnacondadistribution,availablehere:
https://store.continuum.io/cshop/anaconda/
Itis
• Free
• EasytoUse
• EasytoExtend
• VeryPowerful
Theaccompanyingsoftwareforthebookcanbeobtainedfromthe
bookwebsite,http://web.bryant.edu/ bblais/statistical-inference-
∼
for-everyone-sie.html



Appendix B
Notation and Standards
B.1 Useful Greek Letters
α Alpha slopeofaline
π Pi Representstheconstant
β Beta slopeofaline,intercept
3.1415 ,theratioofthecir-
γ Gamma ···
cumferencetothediameterofa
Γ Gamma
circle
δ Delta Asmallchangeinavariable
Π Pi Aproductofaseriesofnum-
∆ Delta Achangeinavariable
bers
(cid:101) Epsilon
ρ Rho
ζ Zeta
σ Sigma Thestandardwidthparameter
η Eta
ofthenormaldistribution
θ Theta Theparametersinabinomial/-
Σ Sigma Asumofaseriesofnumbers
betadistribution
τ Tau
Θ Theta
φ Phi
κ Kappa
Φ Phi
λ Lambda themeaninapoissondistribu-
χ Chi Adistributionrelatedtothe
tion
sumofnormallydistributed
Λ Lambda
variables
µ Mu themeaninanormaldistribu-
ψ Psi
tion(pronounced“mew”)
Ψ Psi
ν Nu (pronounced“new”)
ω Omega
ξ Xi
Ω Omega
Ξ Xi
B.2 Some Math Notation
Variables
Asetofvalues,labeledwithsubscripts...
x = 1
1
x = 5
2


[TABLE]


α Alpha slopeofaline
β Beta slopeofaline,intercept
γ Gamma
Γ Gamma
δ Delta Asmallchangeinavariable
∆ Delta Achangeinavariable
(cid:101) Epsilon
ζ Zeta
η Eta
θ Theta Theparametersinabinomial/-
betadistribution
Θ Theta
κ Kappa
λ Lambda themeaninapoissondistribu-
tion
Λ Lambda
µ Mu themeaninanormaldistribu-
tion(pronounced“mew”)
ν Nu (pronounced“new”)
ξ Xi
Ξ Xi | π Pi Representstheconstant
3.1415 ,theratioofthecir-
···
cumferencetothediameterofa
circle
Π Pi Aproductofaseriesofnum-
bers
ρ Rho
σ Sigma Thestandardwidthparameter
ofthenormaldistribution
Σ Sigma Asumofaseriesofnumbers
τ Tau
φ Phi
Φ Phi
χ Chi Adistributionrelatedtothe
sumofnormallydistributed
variables
ψ Psi
Ψ Psi
ω Omega
Ω Omega




226 statistical inference for everyone
x = 3
3
−
x = 2
4
x = 8
5
referredcollectivelyas x.
i
Sums
x +x +x +x +x =1+5+( 3)+2+8=13
1 2 3 4 5
−
isequivalentto
5
∑
x =1+5+( 3)+2+8=13
i
−
i=1
Products
x x x x x =1 5 ( 3) 2 8= 240
1 2 3 4 5
· · · · · · − · · −
isequivalentto
5
∏
x =1 5 ( 3) 2 8= 240
i
· · − · · −
i=1
Sample Mean
Thesamplemeanofasetofnumbersisdefinedas...
x +x + x
x¯ 1 2 ··· N
≡ N
Intheexampleabove
x +x +x +x +x 3
x¯ 1 2 3 4 5 =2
≡ 5 5
Itcanalsobewritten
∑N x
x¯ i=1 i
≡ N
or
∑ x
x¯ i i
≡ N

notation and standards 227
Sample Standard Deviation
s2 1 ∑ N (x x¯)2
≡ N 1 −
− i=1
Althoughthejustificationforthe
(cid:118) N 1partisbeyondthisbook,
(cid:117) (cid:117) 1 ∑ N on − eeasywaytorememberitis
s (cid:116) (x x¯)2 thatthesampledistributionofa
≡ N 1 −
− i=1 setofnumbersisanestimatefor
theσparameterofthenormal
distribution,representingthespread
Estimates
ofthedata.Youcanthinkofthe
N 1partasachecktokeepyou
−
Anyspecificestimateofaparameter,suchas θ,isdenotedwithahat, fromdoingthecrazythingof
suchas θˆ. estimatingaspreadwithonly1
datapoint!
Factorials
Factorialsaredefinedas
N! =1 2 3 (N 1) N
· · ··· − ·
forexample
5! =1 2 3 4 5=120
· · · ·
TheN-choose-knotationisashorthandforthefactorialsthatarise
inbinomialandBetadistributions.
(cid:32) (cid:33)
N N!
k ≡ k!(N k)!
−
B.3 Qualitative labels to probability values
Roughguidefortheconversionofqualitativelabelstoprobability
valuesusedthroughoutthebook.
term probability
virtuallyimpossible 1/1,000,000
extremelyunlikely 0.01(i.e. 1/100)
veryunlikely 0.05(i.e. 1/20)
unlikely 0.2(i.e. 1/5)
slightlyunlikely 0.4(i.e. 2/5)
evenodds 0.5(i.e. 50-50)
slightlylikely 0.6(i.e. 3/5)
likely 0.8(i.e. 4/5)
verylikely 0.95(i.e. 19/20)
extremelylikely 0.99(i.e. 99/100)
virtuallycertain 999,999/1,000,000


[TABLE]


term probability

virtuallyimpossible 1/1,000,000
extremelyunlikely 0.01(i.e. 1/100)
veryunlikely 0.05(i.e. 1/20)
unlikely 0.2(i.e. 1/5)
slightlyunlikely 0.4(i.e. 2/5)
evenodds 0.5(i.e. 50-50)
slightlylikely 0.6(i.e. 3/5)
likely 0.8(i.e. 4/5)
verylikely 0.95(i.e. 19/20)
extremelylikely 0.99(i.e. 99/100)
virtuallycertain 999,999/1,000,000






Appendix C
Common Distributions and Their Properties
Thischapterisareferenceforthestandarddistributionsencountered
instatisticalinference. Althoughyouareencouragedtoreadthis
chapterthrough,itcanalsobereadout-of-ordertolookataspecific
distribution.
C.1 Discrete and Continuous
Somedistributionsapplytoadiscrete(i.e. countable)numberof
possibilitieswhileothersapplytocontinuousvalues. Inthecase
ofdiscretevariables,theprobabilityisgivenbytheactualvalueof
thedistribution,soitmakessensetospeakoftheprobabilityofan
individuallabel, P(coin1). Inthecaseofcontinuousvariables,the
probabilityisgivenbytheareaunderthedistribution,soitmakes
senseonlytospeakoftheprobabilityifarangeoflabels, P(0.2< θ <
0.3).
C.2 Uniform
Discrete
DiscreteuniformdistributionThediscreteuniformdistributionis DiscreteuniformdistributionThe
definedtobeaconstantvalueforallpossibilities. Mathematicallythis discreteuniformdistributionis
definedtobeaconstantvalueforall
iswritten
possibilities.Mathematicallythisis
1
p(x ) = written
i N p(xi )=
N
1
where N isthetotalnumberofpossibilities,labeled x 1 to x N . The whereNisthetotalnumberof
pictureofthedistributionisshowninFigureC.1 possibilities,labeledx 1toxN.
Continuous
ContinuousuniformdistributionThecontinuousuniformdistri- Continuousuniformdistribution
butionisdefinedtobeaconstantbetweenaminimumandmaximum Thecontinuousuniformdistri-
butionisdefinedtobeaconstant
betweenaminimumandmaximum
value,andzeroeverywhereelse.
Mathematicallythisiswritten
1
p(x)= formin<x<max
max min
−
.

230 statistical inference for everyone
1.2
1.0
0.8
0.6
0.4
0.2
0.0
0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2
x
)x(P
FigureC.1:Discreteuniformdistri-
butionforvalues1to6.Thevalue
Min=0, Max=1
foreachisp(xi )=1/6.
5% 25% 50% 75% 95%
0.25 0.75
0.05 0.50 0.95
value,andzeroeverywhereelse. Mathematicallythisiswritten
1
p(x) = formin< x <max
max min
−
. ThepictureofthedistributionisshowninFigureC.2.
ExampleC.1 Youcallaplumber,andtheysaythattheycancomeanytime
inthenext4hours. Theprobabilityofthemarrivingatanyparticulartime
canberepresentedwithauniformdistribution. Whatistheprobabilitythat
theyarriveinthefirst20minutesofthesecondhour?
Inordertoaskquestionsabouttotalprobabilityfromacontinuous
distributionyoutaketheareaunderthecurvebetweentherelevant
values. Inthiscaseit’dbetheareaunderthecurvefromthetime t = Thereasonfortheparticularcon-
2hrand t = 2hr+20minutes = 2.333hr,asshowninFigureC.3. The stantvaluefortheuniformdistri-
bution,1/(max min),issimply
areaunderthecurveisjusttheareaoftheshadedregionbetween −
thattheareaoftheentirerectan-
times t = 2hrand t = 2.333hr,orjusttheareaofarectangle- A = glemustbe1,whichmeansthat
thereisa100%chanceofthevalues
base height. Thebaseoftherectangleisthelengthoftime,or
× fallingbetweentheminimumand
maximumvalues.
base=0.333hr
Theheightoftherectangleisgivenbytheconstantvalueoftheuni-
formdistribution,or
1 1 1
height= = =0.25
max min 4hr 0hr hr
− −


[TABLE]




5 | % | 25 | % | 50 | % | 75 | % | 95 | %











0. | 05 | 0. | 25 | 0. | 50 | 0. | 75 | 0. | 95




common distributions and their properties 231
1.2
1.0
0.8
0.6
0.4
0.2
0.0
0.2 0.0 0.2 0.4 0.6 0.8 1.0 1.2
x
)x(P
FigureC.2:Continuousuniform
distributionbetweenvalues0and1
Min=0, Max=1
5% 25% 50% 75% 95%
0.25 0.75
0.05 0.50 0.95
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0 1 2 3 4
time
)emit(P
FigureC.3:Continuousuniform
distributionfortheplumberexam-
Min=0, Max=4
ple(ExampleC.1).
5% 25% 50% 75% 95%
20 minutes
1.00 3.00
0.20 2.00 3.80


[TABLE]




5 | % | 25 | % | 50 | % | 75 | % | 95 | %











0. | 05 | 0. | 25 | 0. | 50 | 0. | 75 | 0. | 95





[TABLE]




5 | % 25 | % 50 | % 75 | % 95 | %







20 min | utes



0. | 1.
20 | 00
2. | 3.
00 | 00
3. | 80




232 statistical inference for everyone
Sothetotalprobabilityoftheplumbercominginthefirst20minutes
ofthesecondhouris
(cid:18) (cid:19)
1
P(2< t <2.25) = (0.333hr) 0.25 =0.0833
× hr
C.3 Binomial
BinomialdistributionThediscretebinomialdistributionisde- BinomialdistributionThediscrete
finedtobetheprobabilityofachieving h successesinagiven N binomialdistributionisdefinedto
betheprobabilityofachievingh
eventswhereeacheventhasagiven θ probabilityofsuccess.
successesinagivenNeventswhere
eacheventhasagivenθprobability
ofsuccess.
(cid:32) (cid:33)
h
P(h | N,θ) = N θh(1 − θ)N − h P(h
|
N,θ)= (cid:18)
N
h (cid:19) θh(1
−
θ)N
−
h
0.25
0.20
0.15
0.10
0.05
0.00
0 5 10 15 20 25 30
Number of heads
)03=N,h(P
FigureC.4:Probabilityofgetting
hheadsin30flipsgivenapossible
unfaircoin.Onecoinhasp =0.1,
p=0.1 wherethemaximumisfor3heads
p=0.5 (or1/10ofthe30flips),but2
p=0.8 headsisnearlyaslikely.Another
hasp = 0.5,andisthefaircoin
consideredearlierwithamaximum
at15heads(or1/2ofthe30flips).
Finally,anothercoinshownas
p=0.8where24heads(or8/10of
the30flips)ismaximum.
AlthoughitmaylooklikeaBeta,thebinomialdistributionisused
tofindthebestestimateforthenumberofsuccesses, h,giventhe
numberofevents, N,andtheprobabilityofthesuccessofasingle
event, θ.
C.4 Beta
BetadistributionThecontinuousBetadistributionistheposterior BetadistributionThecontinuous
probabilitydistributionfortheparameter θ,whereonehasobserved Betadistributionistheposterior
probabilitydistributionforthepa-
rameterθ,whereonehasobserved
hsuccessesinagivenNevents,and
eacheventisassumedtohaveaθ
probabilityofsuccess.
(cid:18) (cid:19)
N
P(θ
|
h,N)=(N+1)
· h
θh(1
−
θ)N
−
h


[TABLE]


p=0.1
p=0.5
p=0.8

p=0.1
p=0.5
p=0.8












common distributions and their properties 233
h successesinagiven N events,andeacheventisassumedtohavea
θ probabilityofsuccess.
(cid:32) (cid:33)
N
P(θ h,N) = (N+1) θh(1 θ)N
−
h
| · h −
Althoughitmaylooklikeabinomial,theBetadistributionisused
tofindthebestestimatefortheparameter θ wherethenumberof
successesandevents, h and N aregiven.
4
3
2
1
0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
θ
)θ(P
FigureC.5:Posteriorprobability
3 heads and 9 tails distributionfortheθvaluesof
thebentcoin-theprobability
50% thatthecoinwilllandheads.The
25% distributionisshownfordata3
headsand9tails.Thevarious
quartilesareshownintheplot.
75%
5%
95%
1%
99%
0.11 0.28 0.49
0.07 0.20 0.36 0.59
C.5 Normal (Gaussian)
NormaldistributionTheNormaldistributionisthemostcom- NormaldistributionTheNormal
mondistributionfoundinallofstatisticalinference. Itisthebest distributionisthemostcommon
distributionfoundinallofstatis-
priordistributiontouse,whenallyouknowisthatyourdatahas
ticalinference.Itisthebestprior
aconstanttruevalueandsomeconstantvariationaroundthattrue distributiontouse,whenallyou
knowisthatyourdatahasacon-
value. Itistheposteriorprobabilitydistributionfortheunknown
stanttruevalueandsomeconstant
truevaluegiven N samplesandtheknowndeviation, σ. Itisalsothe variationaroundthattruevalue.It
approximateformfornearlyeverydistributionwhenyouhavemany istheposteriorprobabilitydistri-
butionfortheunknowntruevalue
samples. Themathematicalformforthenormal,orGaussian,is
givenNsamplesandtheknownde-
viation,σ.Itisalsotheapproximate
formfornearlyeverydistribution
Normal(µ,σ) = √2 1 πσ2 e− (x − µ)2/2σ2 w m h at e h n e y m o a u ti h ca a l v f e o m rm an f y or sa th m e p n le o s r . m T a h l, e
orGaussian,is
Normal(µ,σ)= √2 1 πσ2 e− (x − µ)2/2σ2


[TABLE]




25 | 50
% | %

5 | % | 75 | %

1 | % | 95 | %

99 | %

0. | 0.
0 | 11
7 0. | 0.
20 | 2 | 8
0. | 36 | 0. | 49
0. | 59




234 statistical inference for everyone
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
x
)1,0(lamroN=)x(p
FigureC.6:Thenormaldistribution.
Threeusefulpropertiesof σ forthenormaldistributionarethe
following:
1 thenormaldistributionvalueatthemaximum(i.e. at x = µ)
isaround2.7timeslargerthanthevalueone-σ awayfromthe
maximum(at x = µ σ and x = µ+σ)
−
2 thetotalprobabilitybetweenthesetwopointsis65%.
3 95%ofthedistributionliesbetween µ 2σ and µ+2σ (seeFig-
−
ure7.3)


[TABLE]

















Appendix D
Tables
D.1 Credible Intervals for Standard Normal Distribution
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
68% CI at µ 1σ
±
CredibleInterval z Approximately
±
50.0% 0.6745σ
68.0% 0.9945σ 1σ
90.0% 1.6449σ
95.0% 1.9600σ 2σ
99.0% 2.5758σ
99.8% 3.0902σ 3σ
99.995% 4.0556σ 4σ
ExampleD.1 UsageoftheCredibleIntervalTablefortheNormalDistri-
bution
Givenasetof10sampleswithsamplemean x¯ = 5.2andknown
deviation σ = 0.3,thebestestimateforthemeanparameter µ,repre-
sentingthetruevalueofthedata,isthesamplemean, µˆ = 5.2with


[TABLE]


68% | CI | at µ | 1σ

±













[TABLE]


50.0% | ±
0.6745σ

68.0% | 0.9945σ | 1σ

90.0% | 1.6449σ

95.0% | 1.9600σ | 2σ

99.0% | 2.5758σ

99.8% | 3.0902σ | 3σ

99.995% | 4.0556σ | 4σ




236 statistical inference for everyone
uncertainty σ/√N or0.3/√10=0.095. Someofthecredibleintervals
forthisestimatethenarethefollowing
• 68%- [5.2 0.9945 0.095,5.2+0.9945 0.095] = [5.11,5.29]
− · ·
• 95%- [5.2 1.9600 0.095,5.2+1.9600 0.095] = [5.01,5.39]
− · ·
• 99.8%- [5.2 3.0902 0.095,5.2+3.0902 0.095] = [4.91,5.49]
− · ·
orapproximately
• 68%- [5.2 1 0.095,5.2+1 0.095] = [5.11,5.29]
− · ·
• 95%- [5.2 2 0.095,5.2+2 0.095] = [5.01,5.39]
− · ·
• 99.8%- [5.2 3 0.095,5.2+3 0.095] = [4.91,5.49]
− · ·
D.2 Credible Intervals for Student’s t Distribution
DegreesofFreedom
Credible 1 2 3 4 5 6 7 8
Interval
50.0% 1.000σ 0.816σ 0.765σ 0.741σ 0.727σ 0.718σ 0.711σ 0.706σ
68.0% 1.819σ 1.312σ 1.189σ 1.134σ 1.104σ 1.084σ 1.070σ 1.060σ
90.0% 6.314σ 2.920σ 2.353σ 2.132σ 2.015σ 1.943σ 1.895σ 1.860σ
95.0% 12.706σ 4.303σ 3.182σ 2.776σ 2.571σ 2.447σ 2.365σ 2.306σ
99.0% 63.657σ 9.925σ 5.841σ 4.604σ 4.032σ 3.707σ 3.499σ 3.355σ
99.8% 318.309σ 22.327σ 10.215σ 7.173σ 5.893σ 5.208σ 4.785σ 4.501σ
99.995% 12732.395σ 141.416σ 35.298σ 18.522σ 12.893σ 10.261σ 8.783σ 7.851σ
DegreesofFreedom
Credible 9 10 11 12 13 14 15 16
Interval
50.0% 0.703σ 0.700σ 0.697σ 0.695σ 0.694σ 0.692σ 0.691σ 0.690σ
68.0% 1.053σ 1.046σ 1.041σ 1.037σ 1.034σ 1.031σ 1.029σ 1.026σ
90.0% 1.833σ 1.812σ 1.796σ 1.782σ 1.771σ 1.761σ 1.753σ 1.746σ
95.0% 2.262σ 2.228σ 2.201σ 2.179σ 2.160σ 2.145σ 2.131σ 2.120σ
99.0% 3.250σ 3.169σ 3.106σ 3.055σ 3.012σ 2.977σ 2.947σ 2.921σ
99.8% 4.297σ 4.144σ 4.025σ 3.930σ 3.852σ 3.787σ 3.733σ 3.686σ
99.995% 7.215σ 6.757σ 6.412σ 6.143σ 5.928σ 5.753σ 5.607σ 5.484σ


[TABLE]


Credible
Interval | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8

50.0% | 1.000σ | 0.816σ | 0.765σ | 0.741σ | 0.727σ | 0.718σ | 0.711σ | 0.706σ

68.0% | 1.819σ | 1.312σ | 1.189σ | 1.134σ | 1.104σ | 1.084σ | 1.070σ | 1.060σ

90.0% | 6.314σ | 2.920σ | 2.353σ | 2.132σ | 2.015σ | 1.943σ | 1.895σ | 1.860σ

95.0% | 12.706σ | 4.303σ | 3.182σ | 2.776σ | 2.571σ | 2.447σ | 2.365σ | 2.306σ

99.0% | 63.657σ | 9.925σ | 5.841σ | 4.604σ | 4.032σ | 3.707σ | 3.499σ | 3.355σ

99.8% | 318.309σ | 22.327σ | 10.215σ | 7.173σ | 5.893σ | 5.208σ | 4.785σ | 4.501σ

99.995% | 12732.395σ | 141.416σ | 35.298σ | 18.522σ | 12.893σ | 10.261σ | 8.783σ | 7.851σ





[TABLE]


Credible
Interval | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16

50.0% | 0.703σ | 0.700σ | 0.697σ | 0.695σ | 0.694σ | 0.692σ | 0.691σ | 0.690σ

68.0% | 1.053σ | 1.046σ | 1.041σ | 1.037σ | 1.034σ | 1.031σ | 1.029σ | 1.026σ

90.0% | 1.833σ | 1.812σ | 1.796σ | 1.782σ | 1.771σ | 1.761σ | 1.753σ | 1.746σ

95.0% | 2.262σ | 2.228σ | 2.201σ | 2.179σ | 2.160σ | 2.145σ | 2.131σ | 2.120σ

99.0% | 3.250σ | 3.169σ | 3.106σ | 3.055σ | 3.012σ | 2.977σ | 2.947σ | 2.921σ

99.8% | 4.297σ | 4.144σ | 4.025σ | 3.930σ | 3.852σ | 3.787σ | 3.733σ | 3.686σ

99.995% | 7.215σ | 6.757σ | 6.412σ | 6.143σ | 5.928σ | 5.753σ | 5.607σ | 5.484σ




tables 237
DegreesofFreedom
Credible 17 18 19 20 21 22 23 24
Interval
50.0% 0.689σ 0.688σ 0.688σ 0.687σ 0.686σ 0.686σ 0.685σ 0.685σ
68.0% 1.024σ 1.023σ 1.021σ 1.020σ 1.019σ 1.017σ 1.016σ 1.015σ
90.0% 1.740σ 1.734σ 1.729σ 1.725σ 1.721σ 1.717σ 1.714σ 1.711σ
95.0% 2.110σ 2.101σ 2.093σ 2.086σ 2.080σ 2.074σ 2.069σ 2.064σ
99.0% 2.898σ 2.878σ 2.861σ 2.845σ 2.831σ 2.819σ 2.807σ 2.797σ
99.8% 3.646σ 3.610σ 3.579σ 3.552σ 3.527σ 3.505σ 3.485σ 3.467σ
99.995% 5.379σ 5.288σ 5.209σ 5.139σ 5.077σ 5.022σ 4.972σ 4.927σ
DegreesofFreedom
Credible 25 26 27 28 29 30 31 32
Interval
50.0% 0.684σ 0.684σ 0.684σ 0.683σ 0.683σ 0.683σ 0.682σ 0.682σ
68.0% 1.015σ 1.014σ 1.013σ 1.012σ 1.012σ 1.011σ 1.011σ 1.010σ
90.0% 1.708σ 1.706σ 1.703σ 1.701σ 1.699σ 1.697σ 1.696σ 1.694σ
95.0% 2.060σ 2.056σ 2.052σ 2.048σ 2.045σ 2.042σ 2.040σ 2.037σ
99.0% 2.787σ 2.779σ 2.771σ 2.763σ 2.756σ 2.750σ 2.744σ 2.738σ
99.8% 3.450σ 3.435σ 3.421σ 3.408σ 3.396σ 3.385σ 3.375σ 3.365σ
99.995% 4.887σ 4.849σ 4.816σ 4.784σ 4.756σ 4.729σ 4.705σ 4.682σ
DegreesofFreedom
Credible 33 34 35 36 37 38 39 40
Interval
50.0% 0.682σ 0.682σ 0.682σ 0.681σ 0.681σ 0.681σ 0.681σ 0.681σ
68.0% 1.010σ 1.009σ 1.009σ 1.008σ 1.008σ 1.008σ 1.007σ 1.007σ
90.0% 1.692σ 1.691σ 1.690σ 1.688σ 1.687σ 1.686σ 1.685σ 1.684σ
95.0% 2.035σ 2.032σ 2.030σ 2.028σ 2.026σ 2.024σ 2.023σ 2.021σ
99.0% 2.733σ 2.728σ 2.724σ 2.719σ 2.715σ 2.712σ 2.708σ 2.704σ
99.8% 3.356σ 3.348σ 3.340σ 3.333σ 3.326σ 3.319σ 3.313σ 3.307σ
99.995% 4.660σ 4.640σ 4.622σ 4.604σ 4.588σ 4.572σ 4.558σ 4.544σ
ExampleD.2 UsageoftheCredibleIntervalTablefortheStudent’st
Distribution
Givenasetof10samples(9degreesoffreedom)withsample
mean x¯ = 5.2andsampledeviation s = 0.3,thebestestimatefor
themeanparameter µ,representingthetruevalueofthedata,isthe
samplemean, µˆ = 5.2withuncertainty s/√N or0.3/√10 = 0.095.
Someofthecredibleintervalsforthisestimatethenarethefollowing
• 68%- [5.2 1.053 0.095,5.2+1.053 0.095] = [5.09,5.3]
− · ·
• 95%- [5.2 2.262 0.095,5.2+2.262 0.095] = [4.99,5.41]
− · ·
• 99.8%- [5.2 4.297 0.095,5.2+4.297 0.095] = [4.79,5.61]
− · ·


[TABLE]


Credible
Interval | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24

50.0% | 0.689σ | 0.688σ | 0.688σ | 0.687σ | 0.686σ | 0.686σ | 0.685σ | 0.685σ

68.0% | 1.024σ | 1.023σ | 1.021σ | 1.020σ | 1.019σ | 1.017σ | 1.016σ | 1.015σ

90.0% | 1.740σ | 1.734σ | 1.729σ | 1.725σ | 1.721σ | 1.717σ | 1.714σ | 1.711σ

95.0% | 2.110σ | 2.101σ | 2.093σ | 2.086σ | 2.080σ | 2.074σ | 2.069σ | 2.064σ

99.0% | 2.898σ | 2.878σ | 2.861σ | 2.845σ | 2.831σ | 2.819σ | 2.807σ | 2.797σ

99.8% | 3.646σ | 3.610σ | 3.579σ | 3.552σ | 3.527σ | 3.505σ | 3.485σ | 3.467σ

99.995% | 5.379σ | 5.288σ | 5.209σ | 5.139σ | 5.077σ | 5.022σ | 4.972σ | 4.927σ





[TABLE]


Credible
Interval | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32

50.0% | 0.684σ | 0.684σ | 0.684σ | 0.683σ | 0.683σ | 0.683σ | 0.682σ | 0.682σ

68.0% | 1.015σ | 1.014σ | 1.013σ | 1.012σ | 1.012σ | 1.011σ | 1.011σ | 1.010σ

90.0% | 1.708σ | 1.706σ | 1.703σ | 1.701σ | 1.699σ | 1.697σ | 1.696σ | 1.694σ

95.0% | 2.060σ | 2.056σ | 2.052σ | 2.048σ | 2.045σ | 2.042σ | 2.040σ | 2.037σ

99.0% | 2.787σ | 2.779σ | 2.771σ | 2.763σ | 2.756σ | 2.750σ | 2.744σ | 2.738σ

99.8% | 3.450σ | 3.435σ | 3.421σ | 3.408σ | 3.396σ | 3.385σ | 3.375σ | 3.365σ

99.995% | 4.887σ | 4.849σ | 4.816σ | 4.784σ | 4.756σ | 4.729σ | 4.705σ | 4.682σ





[TABLE]


Credible
Interval | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40

50.0% | 0.682σ | 0.682σ | 0.682σ | 0.681σ | 0.681σ | 0.681σ | 0.681σ | 0.681σ

68.0% | 1.010σ | 1.009σ | 1.009σ | 1.008σ | 1.008σ | 1.008σ | 1.007σ | 1.007σ

90.0% | 1.692σ | 1.691σ | 1.690σ | 1.688σ | 1.687σ | 1.686σ | 1.685σ | 1.684σ

95.0% | 2.035σ | 2.032σ | 2.030σ | 2.028σ | 2.026σ | 2.024σ | 2.023σ | 2.021σ

99.0% | 2.733σ | 2.728σ | 2.724σ | 2.719σ | 2.715σ | 2.712σ | 2.708σ | 2.704σ

99.8% | 3.356σ | 3.348σ | 3.340σ | 3.333σ | 3.326σ | 3.319σ | 3.313σ | 3.307σ

99.995% | 4.660σ | 4.640σ | 4.622σ | 4.604σ | 4.588σ | 4.572σ | 4.558σ | 4.544σ




238 statistical inference for everyone
D.3 Cumulative Standard Normal Distribution
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
area
z Area z Area z Area z Area z Area
onLeft onLeft onLeft onLeft onLeft
-3.70 0.0001 -3.40 0.0003 -3.10 0.0010 -2.80 0.0026 -2.50 0.0062
-3.69 0.0001 -3.39 0.0003 -3.09 0.0010 -2.79 0.0026 -2.49 0.0064
-3.68 0.0001 -3.38 0.0004 -3.08 0.0010 -2.78 0.0027 -2.48 0.0066
-3.67 0.0001 -3.37 0.0004 -3.07 0.0011 -2.77 0.0028 -2.47 0.0068
-3.66 0.0001 -3.36 0.0004 -3.06 0.0011 -2.76 0.0029 -2.46 0.0069
-3.65 0.0001 -3.35 0.0004 -3.05 0.0011 -2.75 0.0030 -2.45 0.0071
-3.64 0.0001 -3.34 0.0004 -3.04 0.0012 -2.74 0.0031 -2.44 0.0073
-3.63 0.0001 -3.33 0.0004 -3.03 0.0012 -2.73 0.0032 -2.43 0.0075
-3.62 0.0001 -3.32 0.0005 -3.02 0.0013 -2.72 0.0033 -2.42 0.0078
-3.61 0.0002 -3.31 0.0005 -3.01 0.0013 -2.71 0.0034 -2.41 0.0080
-3.60 0.0002 -3.30 0.0005 -3.00 0.0013 -2.70 0.0035 -2.40 0.0082
-3.59 0.0002 -3.29 0.0005 -2.99 0.0014 -2.69 0.0036 -2.39 0.0084
-3.58 0.0002 -3.28 0.0005 -2.98 0.0014 -2.68 0.0037 -2.38 0.0087
-3.57 0.0002 -3.27 0.0005 -2.97 0.0015 -2.67 0.0038 -2.37 0.0089
-3.56 0.0002 -3.26 0.0006 -2.96 0.0015 -2.66 0.0039 -2.36 0.0091
-3.55 0.0002 -3.25 0.0006 -2.95 0.0016 -2.65 0.0040 -2.35 0.0094
-3.54 0.0002 -3.24 0.0006 -2.94 0.0016 -2.64 0.0041 -2.34 0.0096
-3.53 0.0002 -3.23 0.0006 -2.93 0.0017 -2.63 0.0043 -2.33 0.0099
-3.52 0.0002 -3.22 0.0006 -2.92 0.0018 -2.62 0.0044 -2.32 0.0102
-3.51 0.0002 -3.21 0.0007 -2.91 0.0018 -2.61 0.0045 -2.31 0.0104
-3.50 0.0002 -3.20 0.0007 -2.90 0.0019 -2.60 0.0047 -2.30 0.0107
-3.49 0.0002 -3.19 0.0007 -2.89 0.0019 -2.59 0.0048 -2.29 0.0110
-3.48 0.0003 -3.18 0.0007 -2.88 0.0020 -2.58 0.0049 -2.28 0.0113
-3.47 0.0003 -3.17 0.0008 -2.87 0.0021 -2.57 0.0051 -2.27 0.0116
-3.46 0.0003 -3.16 0.0008 -2.86 0.0021 -2.56 0.0052 -2.26 0.0119
-3.45 0.0003 -3.15 0.0008 -2.85 0.0022 -2.55 0.0054 -2.25 0.0122
-3.44 0.0003 -3.14 0.0008 -2.84 0.0023 -2.54 0.0055 -2.24 0.0125
-3.43 0.0003 -3.13 0.0009 -2.83 0.0023 -2.53 0.0057 -2.23 0.0129
-3.42 0.0003 -3.12 0.0009 -2.82 0.0024 -2.52 0.0059 -2.22 0.0132
-3.41 0.0003 -3.11 0.0009 -2.81 0.0025 -2.51 0.0060 -2.21 0.0136
-3.40 0.0003 -3.10 0.0010 -2.80 0.0026 -2.50 0.0062 -2.20 0.0139


[TABLE]








ar | ea









[TABLE]


-3.70 | 0.0001

-3.69 | 0.0001

-3.68 | 0.0001

-3.67 | 0.0001

-3.66 | 0.0001

-3.65 | 0.0001

-3.64 | 0.0001

-3.63 | 0.0001

-3.62 | 0.0001

-3.61 | 0.0002

-3.60 | 0.0002

-3.59 | 0.0002

-3.58 | 0.0002

-3.57 | 0.0002

-3.56 | 0.0002

-3.55 | 0.0002

-3.54 | 0.0002

-3.53 | 0.0002

-3.52 | 0.0002

-3.51 | 0.0002

-3.50 | 0.0002

-3.49 | 0.0002

-3.48 | 0.0003

-3.47 | 0.0003

-3.46 | 0.0003

-3.45 | 0.0003

-3.44 | 0.0003

-3.43 | 0.0003

-3.42 | 0.0003

-3.41 | 0.0003

-3.40 | 0.0003





[TABLE]


-3.40 | 0.0003

-3.39 | 0.0003

-3.38 | 0.0004

-3.37 | 0.0004

-3.36 | 0.0004

-3.35 | 0.0004

-3.34 | 0.0004

-3.33 | 0.0004

-3.32 | 0.0005

-3.31 | 0.0005

-3.30 | 0.0005

-3.29 | 0.0005

-3.28 | 0.0005

-3.27 | 0.0005

-3.26 | 0.0006

-3.25 | 0.0006

-3.24 | 0.0006

-3.23 | 0.0006

-3.22 | 0.0006

-3.21 | 0.0007

-3.20 | 0.0007

-3.19 | 0.0007

-3.18 | 0.0007

-3.17 | 0.0008

-3.16 | 0.0008

-3.15 | 0.0008

-3.14 | 0.0008

-3.13 | 0.0009

-3.12 | 0.0009

-3.11 | 0.0009

-3.10 | 0.0010





[TABLE]


-3.10 | 0.0010

-3.09 | 0.0010

-3.08 | 0.0010

-3.07 | 0.0011

-3.06 | 0.0011

-3.05 | 0.0011

-3.04 | 0.0012

-3.03 | 0.0012

-3.02 | 0.0013

-3.01 | 0.0013

-3.00 | 0.0013

-2.99 | 0.0014

-2.98 | 0.0014

-2.97 | 0.0015

-2.96 | 0.0015

-2.95 | 0.0016

-2.94 | 0.0016

-2.93 | 0.0017

-2.92 | 0.0018

-2.91 | 0.0018

-2.90 | 0.0019

-2.89 | 0.0019

-2.88 | 0.0020

-2.87 | 0.0021

-2.86 | 0.0021

-2.85 | 0.0022

-2.84 | 0.0023

-2.83 | 0.0023

-2.82 | 0.0024

-2.81 | 0.0025

-2.80 | 0.0026





[TABLE]


-2.80 | 0.0026

-2.79 | 0.0026

-2.78 | 0.0027

-2.77 | 0.0028

-2.76 | 0.0029

-2.75 | 0.0030

-2.74 | 0.0031

-2.73 | 0.0032

-2.72 | 0.0033

-2.71 | 0.0034

-2.70 | 0.0035

-2.69 | 0.0036

-2.68 | 0.0037

-2.67 | 0.0038

-2.66 | 0.0039

-2.65 | 0.0040

-2.64 | 0.0041

-2.63 | 0.0043

-2.62 | 0.0044

-2.61 | 0.0045

-2.60 | 0.0047

-2.59 | 0.0048

-2.58 | 0.0049

-2.57 | 0.0051

-2.56 | 0.0052

-2.55 | 0.0054

-2.54 | 0.0055

-2.53 | 0.0057

-2.52 | 0.0059

-2.51 | 0.0060

-2.50 | 0.0062





[TABLE]


-2.50 | 0.0062

-2.49 | 0.0064

-2.48 | 0.0066

-2.47 | 0.0068

-2.46 | 0.0069

-2.45 | 0.0071

-2.44 | 0.0073

-2.43 | 0.0075

-2.42 | 0.0078

-2.41 | 0.0080

-2.40 | 0.0082

-2.39 | 0.0084

-2.38 | 0.0087

-2.37 | 0.0089

-2.36 | 0.0091

-2.35 | 0.0094

-2.34 | 0.0096

-2.33 | 0.0099

-2.32 | 0.0102

-2.31 | 0.0104

-2.30 | 0.0107

-2.29 | 0.0110

-2.28 | 0.0113

-2.27 | 0.0116

-2.26 | 0.0119

-2.25 | 0.0122

-2.24 | 0.0125

-2.23 | 0.0129

-2.22 | 0.0132

-2.21 | 0.0136

-2.20 | 0.0139




tables 239
Cumulative Normal Distribution (cont.)
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
area
z Area z Area z Area z Area z Area
onLeft onLeft onLeft onLeft onLeft
-2.20 0.0139 -1.90 0.0287 -1.60 0.0548 -1.30 0.0968 -1.00 0.1587
-2.19 0.0143 -1.89 0.0294 -1.59 0.0559 -1.29 0.0985 -0.99 0.1611
-2.18 0.0146 -1.88 0.0301 -1.58 0.0571 -1.28 0.1003 -0.98 0.1635
-2.17 0.0150 -1.87 0.0307 -1.57 0.0582 -1.27 0.1020 -0.97 0.1660
-2.16 0.0154 -1.86 0.0314 -1.56 0.0594 -1.26 0.1038 -0.96 0.1685
-2.15 0.0158 -1.85 0.0322 -1.55 0.0606 -1.25 0.1056 -0.95 0.1711
-2.14 0.0162 -1.84 0.0329 -1.54 0.0618 -1.24 0.1075 -0.94 0.1736
-2.13 0.0166 -1.83 0.0336 -1.53 0.0630 -1.23 0.1093 -0.93 0.1762
-2.12 0.0170 -1.82 0.0344 -1.52 0.0643 -1.22 0.1112 -0.92 0.1788
-2.11 0.0174 -1.81 0.0351 -1.51 0.0655 -1.21 0.1131 -0.91 0.1814
-2.10 0.0179 -1.80 0.0359 -1.50 0.0668 -1.20 0.1151 -0.90 0.1841
-2.09 0.0183 -1.79 0.0367 -1.49 0.0681 -1.19 0.1170 -0.89 0.1867
-2.08 0.0188 -1.78 0.0375 -1.48 0.0694 -1.18 0.1190 -0.88 0.1894
-2.07 0.0192 -1.77 0.0384 -1.47 0.0708 -1.17 0.1210 -0.87 0.1922
-2.06 0.0197 -1.76 0.0392 -1.46 0.0721 -1.16 0.1230 -0.86 0.1949
-2.05 0.0202 -1.75 0.0401 -1.45 0.0735 -1.15 0.1251 -0.85 0.1977
-2.04 0.0207 -1.74 0.0409 -1.44 0.0749 -1.14 0.1271 -0.84 0.2005
-2.03 0.0212 -1.73 0.0418 -1.43 0.0764 -1.13 0.1292 -0.83 0.2033
-2.02 0.0217 -1.72 0.0427 -1.42 0.0778 -1.12 0.1314 -0.82 0.2061
-2.01 0.0222 -1.71 0.0436 -1.41 0.0793 -1.11 0.1335 -0.81 0.2090
-2.00 0.0228 -1.70 0.0446 -1.40 0.0808 -1.10 0.1357 -0.80 0.2119
-1.99 0.0233 -1.69 0.0455 -1.39 0.0823 -1.09 0.1379 -0.79 0.2148
-1.98 0.0239 -1.68 0.0465 -1.38 0.0838 -1.08 0.1401 -0.78 0.2177
-1.97 0.0244 -1.67 0.0475 -1.37 0.0853 -1.07 0.1423 -0.77 0.2206
-1.96 0.0250 -1.66 0.0485 -1.36 0.0869 -1.06 0.1446 -0.76 0.2236
-1.95 0.0256 -1.65 0.0495 -1.35 0.0885 -1.05 0.1469 -0.75 0.2266
-1.94 0.0262 -1.64 0.0505 -1.34 0.0901 -1.04 0.1492 -0.74 0.2296
-1.93 0.0268 -1.63 0.0516 -1.33 0.0918 -1.03 0.1515 -0.73 0.2327
-1.92 0.0274 -1.62 0.0526 -1.32 0.0934 -1.02 0.1539 -0.72 0.2358
-1.91 0.0281 -1.61 0.0537 -1.31 0.0951 -1.01 0.1562 -0.71 0.2389
-1.90 0.0287 -1.60 0.0548 -1.30 0.0968 -1.00 0.1587 -0.70 0.2420


[TABLE]








ar | ea









[TABLE]


-2.20 | 0.0139

-2.19 | 0.0143

-2.18 | 0.0146

-2.17 | 0.0150

-2.16 | 0.0154

-2.15 | 0.0158

-2.14 | 0.0162

-2.13 | 0.0166

-2.12 | 0.0170

-2.11 | 0.0174

-2.10 | 0.0179

-2.09 | 0.0183

-2.08 | 0.0188

-2.07 | 0.0192

-2.06 | 0.0197

-2.05 | 0.0202

-2.04 | 0.0207

-2.03 | 0.0212

-2.02 | 0.0217

-2.01 | 0.0222

-2.00 | 0.0228

-1.99 | 0.0233

-1.98 | 0.0239

-1.97 | 0.0244

-1.96 | 0.0250

-1.95 | 0.0256

-1.94 | 0.0262

-1.93 | 0.0268

-1.92 | 0.0274

-1.91 | 0.0281

-1.90 | 0.0287





[TABLE]


-1.90 | 0.0287

-1.89 | 0.0294

-1.88 | 0.0301

-1.87 | 0.0307

-1.86 | 0.0314

-1.85 | 0.0322

-1.84 | 0.0329

-1.83 | 0.0336

-1.82 | 0.0344

-1.81 | 0.0351

-1.80 | 0.0359

-1.79 | 0.0367

-1.78 | 0.0375

-1.77 | 0.0384

-1.76 | 0.0392

-1.75 | 0.0401

-1.74 | 0.0409

-1.73 | 0.0418

-1.72 | 0.0427

-1.71 | 0.0436

-1.70 | 0.0446

-1.69 | 0.0455

-1.68 | 0.0465

-1.67 | 0.0475

-1.66 | 0.0485

-1.65 | 0.0495

-1.64 | 0.0505

-1.63 | 0.0516

-1.62 | 0.0526

-1.61 | 0.0537

-1.60 | 0.0548





[TABLE]


-1.60 | 0.0548

-1.59 | 0.0559

-1.58 | 0.0571

-1.57 | 0.0582

-1.56 | 0.0594

-1.55 | 0.0606

-1.54 | 0.0618

-1.53 | 0.0630

-1.52 | 0.0643

-1.51 | 0.0655

-1.50 | 0.0668

-1.49 | 0.0681

-1.48 | 0.0694

-1.47 | 0.0708

-1.46 | 0.0721

-1.45 | 0.0735

-1.44 | 0.0749

-1.43 | 0.0764

-1.42 | 0.0778

-1.41 | 0.0793

-1.40 | 0.0808

-1.39 | 0.0823

-1.38 | 0.0838

-1.37 | 0.0853

-1.36 | 0.0869

-1.35 | 0.0885

-1.34 | 0.0901

-1.33 | 0.0918

-1.32 | 0.0934

-1.31 | 0.0951

-1.30 | 0.0968





[TABLE]


-1.30 | 0.0968

-1.29 | 0.0985

-1.28 | 0.1003

-1.27 | 0.1020

-1.26 | 0.1038

-1.25 | 0.1056

-1.24 | 0.1075

-1.23 | 0.1093

-1.22 | 0.1112

-1.21 | 0.1131

-1.20 | 0.1151

-1.19 | 0.1170

-1.18 | 0.1190

-1.17 | 0.1210

-1.16 | 0.1230

-1.15 | 0.1251

-1.14 | 0.1271

-1.13 | 0.1292

-1.12 | 0.1314

-1.11 | 0.1335

-1.10 | 0.1357

-1.09 | 0.1379

-1.08 | 0.1401

-1.07 | 0.1423

-1.06 | 0.1446

-1.05 | 0.1469

-1.04 | 0.1492

-1.03 | 0.1515

-1.02 | 0.1539

-1.01 | 0.1562

-1.00 | 0.1587





[TABLE]


-1.00 | 0.1587

-0.99 | 0.1611

-0.98 | 0.1635

-0.97 | 0.1660

-0.96 | 0.1685

-0.95 | 0.1711

-0.94 | 0.1736

-0.93 | 0.1762

-0.92 | 0.1788

-0.91 | 0.1814

-0.90 | 0.1841

-0.89 | 0.1867

-0.88 | 0.1894

-0.87 | 0.1922

-0.86 | 0.1949

-0.85 | 0.1977

-0.84 | 0.2005

-0.83 | 0.2033

-0.82 | 0.2061

-0.81 | 0.2090

-0.80 | 0.2119

-0.79 | 0.2148

-0.78 | 0.2177

-0.77 | 0.2206

-0.76 | 0.2236

-0.75 | 0.2266

-0.74 | 0.2296

-0.73 | 0.2327

-0.72 | 0.2358

-0.71 | 0.2389

-0.70 | 0.2420




240 statistical inference for everyone
Cumulative Normal Distribution (cont.)
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
area
z Area z Area z Area z Area z Area
onLeft onLeft onLeft onLeft onLeft
-0.70 0.2420 -0.40 0.3446 -0.10 0.4602 0.20 0.5793 0.50 0.6915
-0.69 0.2451 -0.39 0.3483 -0.09 0.4641 0.21 0.5832 0.51 0.6950
-0.68 0.2483 -0.38 0.3520 -0.08 0.4681 0.22 0.5871 0.52 0.6985
-0.67 0.2514 -0.37 0.3557 -0.07 0.4721 0.23 0.5910 0.53 0.7019
-0.66 0.2546 -0.36 0.3594 -0.06 0.4761 0.24 0.5948 0.54 0.7054
-0.65 0.2578 -0.35 0.3632 -0.05 0.4801 0.25 0.5987 0.55 0.7088
-0.64 0.2611 -0.34 0.3669 -0.04 0.4840 0.26 0.6026 0.56 0.7123
-0.63 0.2643 -0.33 0.3707 -0.03 0.4880 0.27 0.6064 0.57 0.7157
-0.62 0.2676 -0.32 0.3745 -0.02 0.4920 0.28 0.6103 0.58 0.7190
-0.61 0.2709 -0.31 0.3783 -0.01 0.4960 0.29 0.6141 0.59 0.7224
-0.60 0.2743 -0.30 0.3821 0.00 0.5000 0.30 0.6179 0.60 0.7257
-0.59 0.2776 -0.29 0.3859 0.01 0.5040 0.31 0.6217 0.61 0.7291
-0.58 0.2810 -0.28 0.3897 0.02 0.5080 0.32 0.6255 0.62 0.7324
-0.57 0.2843 -0.27 0.3936 0.03 0.5120 0.33 0.6293 0.63 0.7357
-0.56 0.2877 -0.26 0.3974 0.04 0.5160 0.34 0.6331 0.64 0.7389
-0.55 0.2912 -0.25 0.4013 0.05 0.5199 0.35 0.6368 0.65 0.7422
-0.54 0.2946 -0.24 0.4052 0.06 0.5239 0.36 0.6406 0.66 0.7454
-0.53 0.2981 -0.23 0.4090 0.07 0.5279 0.37 0.6443 0.67 0.7486
-0.52 0.3015 -0.22 0.4129 0.08 0.5319 0.38 0.6480 0.68 0.7517
-0.51 0.3050 -0.21 0.4168 0.09 0.5359 0.39 0.6517 0.69 0.7549
-0.50 0.3085 -0.20 0.4207 0.10 0.5398 0.40 0.6554 0.70 0.7580
-0.49 0.3121 -0.19 0.4247 0.11 0.5438 0.41 0.6591 0.71 0.7611
-0.48 0.3156 -0.18 0.4286 0.12 0.5478 0.42 0.6628 0.72 0.7642
-0.47 0.3192 -0.17 0.4325 0.13 0.5517 0.43 0.6664 0.73 0.7673
-0.46 0.3228 -0.16 0.4364 0.14 0.5557 0.44 0.6700 0.74 0.7704
-0.45 0.3264 -0.15 0.4404 0.15 0.5596 0.45 0.6736 0.75 0.7734
-0.44 0.3300 -0.14 0.4443 0.16 0.5636 0.46 0.6772 0.76 0.7764
-0.43 0.3336 -0.13 0.4483 0.17 0.5675 0.47 0.6808 0.77 0.7794
-0.42 0.3372 -0.12 0.4522 0.18 0.5714 0.48 0.6844 0.78 0.7823
-0.41 0.3409 -0.11 0.4562 0.19 0.5753 0.49 0.6879 0.79 0.7852
-0.40 0.3446 -0.10 0.4602 0.20 0.5793 0.50 0.6915 0.80 0.7881


[TABLE]








ar | ea









[TABLE]


-0.70 | 0.2420

-0.69 | 0.2451

-0.68 | 0.2483

-0.67 | 0.2514

-0.66 | 0.2546

-0.65 | 0.2578

-0.64 | 0.2611

-0.63 | 0.2643

-0.62 | 0.2676

-0.61 | 0.2709

-0.60 | 0.2743

-0.59 | 0.2776

-0.58 | 0.2810

-0.57 | 0.2843

-0.56 | 0.2877

-0.55 | 0.2912

-0.54 | 0.2946

-0.53 | 0.2981

-0.52 | 0.3015

-0.51 | 0.3050

-0.50 | 0.3085

-0.49 | 0.3121

-0.48 | 0.3156

-0.47 | 0.3192

-0.46 | 0.3228

-0.45 | 0.3264

-0.44 | 0.3300

-0.43 | 0.3336

-0.42 | 0.3372

-0.41 | 0.3409

-0.40 | 0.3446





[TABLE]


-0.40 | 0.3446

-0.39 | 0.3483

-0.38 | 0.3520

-0.37 | 0.3557

-0.36 | 0.3594

-0.35 | 0.3632

-0.34 | 0.3669

-0.33 | 0.3707

-0.32 | 0.3745

-0.31 | 0.3783

-0.30 | 0.3821

-0.29 | 0.3859

-0.28 | 0.3897

-0.27 | 0.3936

-0.26 | 0.3974

-0.25 | 0.4013

-0.24 | 0.4052

-0.23 | 0.4090

-0.22 | 0.4129

-0.21 | 0.4168

-0.20 | 0.4207

-0.19 | 0.4247

-0.18 | 0.4286

-0.17 | 0.4325

-0.16 | 0.4364

-0.15 | 0.4404

-0.14 | 0.4443

-0.13 | 0.4483

-0.12 | 0.4522

-0.11 | 0.4562

-0.10 | 0.4602





[TABLE]


-0.10 | 0.4602

-0.09 | 0.4641

-0.08 | 0.4681

-0.07 | 0.4721

-0.06 | 0.4761

-0.05 | 0.4801

-0.04 | 0.4840

-0.03 | 0.4880

-0.02 | 0.4920

-0.01 | 0.4960

0.00 | 0.5000

0.01 | 0.5040

0.02 | 0.5080

0.03 | 0.5120

0.04 | 0.5160

0.05 | 0.5199

0.06 | 0.5239

0.07 | 0.5279

0.08 | 0.5319

0.09 | 0.5359

0.10 | 0.5398

0.11 | 0.5438

0.12 | 0.5478

0.13 | 0.5517

0.14 | 0.5557

0.15 | 0.5596

0.16 | 0.5636

0.17 | 0.5675

0.18 | 0.5714

0.19 | 0.5753

0.20 | 0.5793





[TABLE]


0.20 | 0.5793

0.21 | 0.5832

0.22 | 0.5871

0.23 | 0.5910

0.24 | 0.5948

0.25 | 0.5987

0.26 | 0.6026

0.27 | 0.6064

0.28 | 0.6103

0.29 | 0.6141

0.30 | 0.6179

0.31 | 0.6217

0.32 | 0.6255

0.33 | 0.6293

0.34 | 0.6331

0.35 | 0.6368

0.36 | 0.6406

0.37 | 0.6443

0.38 | 0.6480

0.39 | 0.6517

0.40 | 0.6554

0.41 | 0.6591

0.42 | 0.6628

0.43 | 0.6664

0.44 | 0.6700

0.45 | 0.6736

0.46 | 0.6772

0.47 | 0.6808

0.48 | 0.6844

0.49 | 0.6879

0.50 | 0.6915





[TABLE]


0.50 | 0.6915

0.51 | 0.6950

0.52 | 0.6985

0.53 | 0.7019

0.54 | 0.7054

0.55 | 0.7088

0.56 | 0.7123

0.57 | 0.7157

0.58 | 0.7190

0.59 | 0.7224

0.60 | 0.7257

0.61 | 0.7291

0.62 | 0.7324

0.63 | 0.7357

0.64 | 0.7389

0.65 | 0.7422

0.66 | 0.7454

0.67 | 0.7486

0.68 | 0.7517

0.69 | 0.7549

0.70 | 0.7580

0.71 | 0.7611

0.72 | 0.7642

0.73 | 0.7673

0.74 | 0.7704

0.75 | 0.7734

0.76 | 0.7764

0.77 | 0.7794

0.78 | 0.7823

0.79 | 0.7852

0.80 | 0.7881




tables 241
Cumulative Normal Distribution (cont.)
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
area
z Area z Area z Area z Area z Area
onLeft onLeft onLeft onLeft onLeft
0.80 0.7881 1.10 0.8643 1.40 0.9192 1.70 0.9554 2.00 0.9772
0.81 0.7910 1.11 0.8665 1.41 0.9207 1.71 0.9564 2.01 0.9778
0.82 0.7939 1.12 0.8686 1.42 0.9222 1.72 0.9573 2.02 0.9783
0.83 0.7967 1.13 0.8708 1.43 0.9236 1.73 0.9582 2.03 0.9788
0.84 0.7995 1.14 0.8729 1.44 0.9251 1.74 0.9591 2.04 0.9793
0.85 0.8023 1.15 0.8749 1.45 0.9265 1.75 0.9599 2.05 0.9798
0.86 0.8051 1.16 0.8770 1.46 0.9279 1.76 0.9608 2.06 0.9803
0.87 0.8078 1.17 0.8790 1.47 0.9292 1.77 0.9616 2.07 0.9808
0.88 0.8106 1.18 0.8810 1.48 0.9306 1.78 0.9625 2.08 0.9812
0.89 0.8133 1.19 0.8830 1.49 0.9319 1.79 0.9633 2.09 0.9817
0.90 0.8159 1.20 0.8849 1.50 0.9332 1.80 0.9641 2.10 0.9821
0.91 0.8186 1.21 0.8869 1.51 0.9345 1.81 0.9649 2.11 0.9826
0.92 0.8212 1.22 0.8888 1.52 0.9357 1.82 0.9656 2.12 0.9830
0.93 0.8238 1.23 0.8907 1.53 0.9370 1.83 0.9664 2.13 0.9834
0.94 0.8264 1.24 0.8925 1.54 0.9382 1.84 0.9671 2.14 0.9838
0.95 0.8289 1.25 0.8944 1.55 0.9394 1.85 0.9678 2.15 0.9842
0.96 0.8315 1.26 0.8962 1.56 0.9406 1.86 0.9686 2.16 0.9846
0.97 0.8340 1.27 0.8980 1.57 0.9418 1.87 0.9693 2.17 0.9850
0.98 0.8365 1.28 0.8997 1.58 0.9429 1.88 0.9699 2.18 0.9854
0.99 0.8389 1.29 0.9015 1.59 0.9441 1.89 0.9706 2.19 0.9857
1.00 0.8413 1.30 0.9032 1.60 0.9452 1.90 0.9713 2.20 0.9861
1.01 0.8438 1.31 0.9049 1.61 0.9463 1.91 0.9719 2.21 0.9864
1.02 0.8461 1.32 0.9066 1.62 0.9474 1.92 0.9726 2.22 0.9868
1.03 0.8485 1.33 0.9082 1.63 0.9484 1.93 0.9732 2.23 0.9871
1.04 0.8508 1.34 0.9099 1.64 0.9495 1.94 0.9738 2.24 0.9875
1.05 0.8531 1.35 0.9115 1.65 0.9505 1.95 0.9744 2.25 0.9878
1.06 0.8554 1.36 0.9131 1.66 0.9515 1.96 0.9750 2.26 0.9881
1.07 0.8577 1.37 0.9147 1.67 0.9525 1.97 0.9756 2.27 0.9884
1.08 0.8599 1.38 0.9162 1.68 0.9535 1.98 0.9761 2.28 0.9887
1.09 0.8621 1.39 0.9177 1.69 0.9545 1.99 0.9767 2.29 0.9890
1.10 0.8643 1.40 0.9192 1.70 0.9554 2.00 0.9772 2.30 0.9893


[TABLE]








ar | ea









[TABLE]


0.80 | 0.7881

0.81 | 0.7910

0.82 | 0.7939

0.83 | 0.7967

0.84 | 0.7995

0.85 | 0.8023

0.86 | 0.8051

0.87 | 0.8078

0.88 | 0.8106

0.89 | 0.8133

0.90 | 0.8159

0.91 | 0.8186

0.92 | 0.8212

0.93 | 0.8238

0.94 | 0.8264

0.95 | 0.8289

0.96 | 0.8315

0.97 | 0.8340

0.98 | 0.8365

0.99 | 0.8389

1.00 | 0.8413

1.01 | 0.8438

1.02 | 0.8461

1.03 | 0.8485

1.04 | 0.8508

1.05 | 0.8531

1.06 | 0.8554

1.07 | 0.8577

1.08 | 0.8599

1.09 | 0.8621

1.10 | 0.8643





[TABLE]


1.10 | 0.8643

1.11 | 0.8665

1.12 | 0.8686

1.13 | 0.8708

1.14 | 0.8729

1.15 | 0.8749

1.16 | 0.8770

1.17 | 0.8790

1.18 | 0.8810

1.19 | 0.8830

1.20 | 0.8849

1.21 | 0.8869

1.22 | 0.8888

1.23 | 0.8907

1.24 | 0.8925

1.25 | 0.8944

1.26 | 0.8962

1.27 | 0.8980

1.28 | 0.8997

1.29 | 0.9015

1.30 | 0.9032

1.31 | 0.9049

1.32 | 0.9066

1.33 | 0.9082

1.34 | 0.9099

1.35 | 0.9115

1.36 | 0.9131

1.37 | 0.9147

1.38 | 0.9162

1.39 | 0.9177

1.40 | 0.9192





[TABLE]


1.40 | 0.9192

1.41 | 0.9207

1.42 | 0.9222

1.43 | 0.9236

1.44 | 0.9251

1.45 | 0.9265

1.46 | 0.9279

1.47 | 0.9292

1.48 | 0.9306

1.49 | 0.9319

1.50 | 0.9332

1.51 | 0.9345

1.52 | 0.9357

1.53 | 0.9370

1.54 | 0.9382

1.55 | 0.9394

1.56 | 0.9406

1.57 | 0.9418

1.58 | 0.9429

1.59 | 0.9441

1.60 | 0.9452

1.61 | 0.9463

1.62 | 0.9474

1.63 | 0.9484

1.64 | 0.9495

1.65 | 0.9505

1.66 | 0.9515

1.67 | 0.9525

1.68 | 0.9535

1.69 | 0.9545

1.70 | 0.9554





[TABLE]


1.70 | 0.9554

1.71 | 0.9564

1.72 | 0.9573

1.73 | 0.9582

1.74 | 0.9591

1.75 | 0.9599

1.76 | 0.9608

1.77 | 0.9616

1.78 | 0.9625

1.79 | 0.9633

1.80 | 0.9641

1.81 | 0.9649

1.82 | 0.9656

1.83 | 0.9664

1.84 | 0.9671

1.85 | 0.9678

1.86 | 0.9686

1.87 | 0.9693

1.88 | 0.9699

1.89 | 0.9706

1.90 | 0.9713

1.91 | 0.9719

1.92 | 0.9726

1.93 | 0.9732

1.94 | 0.9738

1.95 | 0.9744

1.96 | 0.9750

1.97 | 0.9756

1.98 | 0.9761

1.99 | 0.9767

2.00 | 0.9772





[TABLE]


2.00 | 0.9772

2.01 | 0.9778

2.02 | 0.9783

2.03 | 0.9788

2.04 | 0.9793

2.05 | 0.9798

2.06 | 0.9803

2.07 | 0.9808

2.08 | 0.9812

2.09 | 0.9817

2.10 | 0.9821

2.11 | 0.9826

2.12 | 0.9830

2.13 | 0.9834

2.14 | 0.9838

2.15 | 0.9842

2.16 | 0.9846

2.17 | 0.9850

2.18 | 0.9854

2.19 | 0.9857

2.20 | 0.9861

2.21 | 0.9864

2.22 | 0.9868

2.23 | 0.9871

2.24 | 0.9875

2.25 | 0.9878

2.26 | 0.9881

2.27 | 0.9884

2.28 | 0.9887

2.29 | 0.9890

2.30 | 0.9893




242 statistical inference for everyone
Cumulative Normal Distribution (cont.)
0.4
0.3
0.2
0.1
0.0
4 3 2 1 0 1 2 3 4
z
)z(P
area
z Area z Area z Area z Area z Area
onLeft onLeft onLeft onLeft onLeft
2.30 0.9893 2.60 0.9953 2.90 0.9981 3.20 0.9993 3.50 0.9998
2.31 0.9896 2.61 0.9955 2.91 0.9982 3.21 0.9993 3.51 0.9998
2.32 0.9898 2.62 0.9956 2.92 0.9982 3.22 0.9994 3.52 0.9998
2.33 0.9901 2.63 0.9957 2.93 0.9983 3.23 0.9994 3.53 0.9998
2.34 0.9904 2.64 0.9959 2.94 0.9984 3.24 0.9994 3.54 0.9998
2.35 0.9906 2.65 0.9960 2.95 0.9984 3.25 0.9994 3.55 0.9998
2.36 0.9909 2.66 0.9961 2.96 0.9985 3.26 0.9994 3.56 0.9998
2.37 0.9911 2.67 0.9962 2.97 0.9985 3.27 0.9995 3.57 0.9998
2.38 0.9913 2.68 0.9963 2.98 0.9986 3.28 0.9995 3.58 0.9998
2.39 0.9916 2.69 0.9964 2.99 0.9986 3.29 0.9995 3.59 0.9998
2.40 0.9918 2.70 0.9965 3.00 0.9987 3.30 0.9995 3.60 0.9998
2.41 0.9920 2.71 0.9966 3.01 0.9987 3.31 0.9995 3.61 0.9998
2.42 0.9922 2.72 0.9967 3.02 0.9987 3.32 0.9995 3.62 0.9999
2.43 0.9925 2.73 0.9968 3.03 0.9988 3.33 0.9996 3.63 0.9999
2.44 0.9927 2.74 0.9969 3.04 0.9988 3.34 0.9996 3.64 0.9999
2.45 0.9929 2.75 0.9970 3.05 0.9989 3.35 0.9996 3.65 0.9999
2.46 0.9931 2.76 0.9971 3.06 0.9989 3.36 0.9996 3.66 0.9999
2.47 0.9932 2.77 0.9972 3.07 0.9989 3.37 0.9996 3.67 0.9999
2.48 0.9934 2.78 0.9973 3.08 0.9990 3.38 0.9996 3.68 0.9999
2.49 0.9936 2.79 0.9974 3.09 0.9990 3.39 0.9997 3.69 0.9999
2.50 0.9938 2.80 0.9974 3.10 0.9990 3.40 0.9997 3.70 0.9999
2.51 0.9940 2.81 0.9975 3.11 0.9991 3.41 0.9997 3.71 0.9999
2.52 0.9941 2.82 0.9976 3.12 0.9991 3.42 0.9997 3.72 0.9999
2.53 0.9943 2.83 0.9977 3.13 0.9991 3.43 0.9997 3.73 0.9999
2.54 0.9945 2.84 0.9977 3.14 0.9992 3.44 0.9997 3.74 0.9999
2.55 0.9946 2.85 0.9978 3.15 0.9992 3.45 0.9997 3.75 0.9999
2.56 0.9948 2.86 0.9979 3.16 0.9992 3.46 0.9997 3.76 0.9999
2.57 0.9949 2.87 0.9979 3.17 0.9992 3.47 0.9997 3.77 0.9999
2.58 0.9951 2.88 0.9980 3.18 0.9993 3.48 0.9997 3.78 0.9999
2.59 0.9952 2.89 0.9981 3.19 0.9993 3.49 0.9998 3.79 0.9999
2.60 0.9953 2.90 0.9981 3.20 0.9993 3.50 0.9998 3.80 0.9999


[TABLE]








ar | ea









[TABLE]


2.30 | 0.9893

2.31 | 0.9896

2.32 | 0.9898

2.33 | 0.9901

2.34 | 0.9904

2.35 | 0.9906

2.36 | 0.9909

2.37 | 0.9911

2.38 | 0.9913

2.39 | 0.9916

2.40 | 0.9918

2.41 | 0.9920

2.42 | 0.9922

2.43 | 0.9925

2.44 | 0.9927

2.45 | 0.9929

2.46 | 0.9931

2.47 | 0.9932

2.48 | 0.9934

2.49 | 0.9936

2.50 | 0.9938

2.51 | 0.9940

2.52 | 0.9941

2.53 | 0.9943

2.54 | 0.9945

2.55 | 0.9946

2.56 | 0.9948

2.57 | 0.9949

2.58 | 0.9951

2.59 | 0.9952

2.60 | 0.9953





[TABLE]


2.60 | 0.9953

2.61 | 0.9955

2.62 | 0.9956

2.63 | 0.9957

2.64 | 0.9959

2.65 | 0.9960

2.66 | 0.9961

2.67 | 0.9962

2.68 | 0.9963

2.69 | 0.9964

2.70 | 0.9965

2.71 | 0.9966

2.72 | 0.9967

2.73 | 0.9968

2.74 | 0.9969

2.75 | 0.9970

2.76 | 0.9971

2.77 | 0.9972

2.78 | 0.9973

2.79 | 0.9974

2.80 | 0.9974

2.81 | 0.9975

2.82 | 0.9976

2.83 | 0.9977

2.84 | 0.9977

2.85 | 0.9978

2.86 | 0.9979

2.87 | 0.9979

2.88 | 0.9980

2.89 | 0.9981

2.90 | 0.9981





[TABLE]


2.90 | 0.9981

2.91 | 0.9982

2.92 | 0.9982

2.93 | 0.9983

2.94 | 0.9984

2.95 | 0.9984

2.96 | 0.9985

2.97 | 0.9985

2.98 | 0.9986

2.99 | 0.9986

3.00 | 0.9987

3.01 | 0.9987

3.02 | 0.9987

3.03 | 0.9988

3.04 | 0.9988

3.05 | 0.9989

3.06 | 0.9989

3.07 | 0.9989

3.08 | 0.9990

3.09 | 0.9990

3.10 | 0.9990

3.11 | 0.9991

3.12 | 0.9991

3.13 | 0.9991

3.14 | 0.9992

3.15 | 0.9992

3.16 | 0.9992

3.17 | 0.9992

3.18 | 0.9993

3.19 | 0.9993

3.20 | 0.9993





[TABLE]


3.20 | 0.9993

3.21 | 0.9993

3.22 | 0.9994

3.23 | 0.9994

3.24 | 0.9994

3.25 | 0.9994

3.26 | 0.9994

3.27 | 0.9995

3.28 | 0.9995

3.29 | 0.9995

3.30 | 0.9995

3.31 | 0.9995

3.32 | 0.9995

3.33 | 0.9996

3.34 | 0.9996

3.35 | 0.9996

3.36 | 0.9996

3.37 | 0.9996

3.38 | 0.9996

3.39 | 0.9997

3.40 | 0.9997

3.41 | 0.9997

3.42 | 0.9997

3.43 | 0.9997

3.44 | 0.9997

3.45 | 0.9997

3.46 | 0.9997

3.47 | 0.9997

3.48 | 0.9997

3.49 | 0.9998

3.50 | 0.9998





[TABLE]


3.50 | 0.9998

3.51 | 0.9998

3.52 | 0.9998

3.53 | 0.9998

3.54 | 0.9998

3.55 | 0.9998

3.56 | 0.9998

3.57 | 0.9998

3.58 | 0.9998

3.59 | 0.9998

3.60 | 0.9998

3.61 | 0.9998

3.62 | 0.9999

3.63 | 0.9999

3.64 | 0.9999

3.65 | 0.9999

3.66 | 0.9999

3.67 | 0.9999

3.68 | 0.9999

3.69 | 0.9999

3.70 | 0.9999

3.71 | 0.9999

3.72 | 0.9999

3.73 | 0.9999

3.74 | 0.9999

3.75 | 0.9999

3.76 | 0.9999

3.77 | 0.9999

3.78 | 0.9999

3.79 | 0.9999

3.80 | 0.9999


