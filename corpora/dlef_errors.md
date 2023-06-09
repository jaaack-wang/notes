## Ignorance of sources

The authors ignore the sources when annotating sentence-level event fauctuality. 



#### English, Document id: ED1103

**Source**: ASU 's president Michael Crow

```
<sentence id="ES1103.15">`` We are trying to use these joint programs to attract highly qualified Chinese students to the campus and set up platforms for joint research , '' says ASU 's president Michael Crow .</sentence>

<sentence id="ES1103.16">-EOP- .</sentence>

==> <sentence id="ES1103.17">`` Our next plan is to <event id="EE1103.2" sentence_level_value="PS+">find</event> ways to be engaged with our digital_education activity .</sentence>

==> <sentence id="ES1103.18">We are working to <event id="EE1103.3" sentence_level_value="CT+">link</event> up with many new universities and expanded universities to use technology and work together . ''</sentence>

....

<sentence id="ES1103.40">-EOP- .</sentence>

==> <sentence id="ES1103.41">`` The university has <event id="EE1103.4" sentence_level_value="CT+">created</event> huge opportunities for new learning ways and many unique pathways for Chinese students , who are involved in different programs , '' Crow says .</sentence>

<sentence id="ES1103.42">-EOP- .</sentence>

==> <sentence id="ES1103.43">Many Chinese universities <event id="EE1103.5" sentence_level_value="CT+">seek</event> connections with only the most elite US universities , but those are the schools that exclude the largest number of students , Crow says .</sentence>

<sentence id="ES1103.44">-EOP- .</sentence>

<sentence id="ES1103.45">`` But we have a broader model .</sentence>

==> <sentence id="ES1103.46">And what we are <event id="EE1103.6" sentence_level_value="CT+">looking</event> for are Chinese universities to work with that have the objective of having the most impact on the whole of society .</sentence>

<sentence id="ES1103.47">And that 's the whole external US_China education bond . ''</sentence>
```



**Source**: the text author(s)

```
<sentence id="ES1103.2">China Daily USA -EOP- .</sentence>

==> <sentence id="ES1103.3">US public universities are <event id="EE1103.0" sentence_level_value="CT+">seeking</event> opportunities to enhance cooperation with Chinese counterparts to advance technological development and build global centers for innovative interdisciplinary research .</sentence>

<sentence id="ES1103.4">-EOP- .</sentence>

==> <sentence id="ES1103.5">Arizona State University , a US public_research university established in 1885 in Tempe , near Phoenix , Arizona , started several China_related initiatives 15 years ago to <event id="EE1103.1" sentence_level_value="CT+">provide</event> more opportunities for students .</sentence>
```



## Multiple targets in an document

Questions:

- How to determine the document-level factuality? 
- How to determine these targets are all related to the same event (document-level)? 
- How does the annotated sentence-level factuality contribute to the document-level factuality?

#### English, Document id: ED1103

seeking, provide, find, link, created, seek, looking

```
<sentence id="ES1103.3">US public universities are <event id="EE1103.0" sentence_level_value="CT+">seeking</event> opportunities to enhance cooperation with Chinese counterparts to advance technological development and build global centers for innovative interdisciplinary research .</sentence>

<sentence id="ES1103.5">Arizona State University , a US public_research university established in 1885 in Tempe , near Phoenix , Arizona , started several China_related initiatives 15 years ago to <event id="EE1103.1" sentence_level_value="CT+">provide</event> more opportunities for students .</sentence>

<sentence id="ES1103.17">`` Our next plan is to <event id="EE1103.2" sentence_level_value="PS+">find</event> ways to be engaged with our digital_education activity .</sentence>

<sentence id="ES1103.18">We are working to <event id="EE1103.3" sentence_level_value="CT+">link</event> up with many new universities and expanded universities to use technology and work together . ''</sentence>

<sentence id="ES1103.41">`` The university has <event id="EE1103.4" sentence_level_value="CT+">created</event> huge opportunities for new learning ways and many unique pathways for Chinese students , who are involved in different programs , '' Crow says .</sentence>

<sentence id="ES1103.43">Many Chinese universities <event id="EE1103.5" sentence_level_value="CT+">seek</event> connections with only the most elite US universities , but those are the schools that exclude the largest number of students , Crow says .</sentence>

<sentence id="ES1103.46">And what we are <event id="EE1103.6" sentence_level_value="CT+">looking</event> for are Chinese universities to work with that have the objective of having the most impact on the whole of society .</sentence>
```



### Uncertain/underspecified events being wrongly annotated 

```
<sentence id="ES365.0">China hopes Haitian government finds proper <event id="EE365.0" sentence_level_value="CT+">development</event> path -EOP- .</sentence>
```

```
<sentence id="ES687.3">Hong Kong wants its companies to <event id="EE687.1" sentence_level_value="CT+">partner</event> with British counterparts so they can take on projects together , both in China and other economies in the area covered by the Belt and Road Initiative , attendees of a conference in London heard on Thursday .</sentence>
```

```
<sentence id="ES1210.17">Dong said a fundamental way to prevent financial <event id="EE1210.7" sentence_level_value="CT+">risks</event> is to meet the financing demand of the real economy sectors .</sentence>
```

```
<sentence id="ES1210.18">`` Only when the real economy gets healthy can we fundamentally prevent systemic financial <event id="EE1210.8" sentence_level_value="CT+">risks</event> , '' he said -EOP- .</sentence>
```

```
<sentence id="CS0.0">

美国务卿称从未考虑 US Secretary of State claims that he never thinks of 

<event id="CE0.0" sentence_level_value="CT-">辞职 resignation </event>

未否认曾称特朗普是白痴。but he does not deny calling Trump an idiot.

</sentence>
```

```
<sentence id="CS0.10">
4日早晨，美国全国广播公司（NBC）报道，由于和白宫意见不合，整个夏天蒂勒森都处于
<event id="CE0.3" sentence_level_value="PS+">辞职</event>
的边缘，他还曾在7月20日一次五角大楼的会议后称总统特朗普是“白痴”，(副总统彭斯曾力劝蒂勒森不要) Vice president Pence asked Tillerson not to 
<event id="CE0.4" sentence_level_value="CT-">辞职 resign</event>
。
</sentence>
```



## Nonsensical annotations

```
<sentence id="ES1341.48">`` I want to thank the Confucius <event id="EE1341.4" sentence_level_value="CT+">Institute</event> for sharing the wonderful language and culture of China to the world , '' she said .</sentence>
```

```
 <sentence id="ES617.0">Chimes of Big Ben to be quieter , slightly <event id="EE617.0" sentence_level_value="PS+">out</event> of time when coming back -EOP- .</sentence>
```

```
<sentence id="ES1417.9">Egalia is a taxpayer_funded school in the Sodermalm district of <event id="EE1417.2" sentence_level_value="CT+">Stockholm</event> , Sweden .</sentence>
```

```
<sentence id="ES1300.11">`` This strongly suggests that the <event id="EE1300.5" sentence_level_value="CT+">yeti</event> legend has a root in biological facts and that is has to do with bears that are living in the region today , '' said biologist Charlotte Lindqvist of the University at Buffalo in New York and Nanyang Technological University , Singapore , who led the study published in the scientific journal Proceedings of the Royal Society B. -EOP- .</sentence>
```

```
<sentence id="ES1427.27">This subsequently came to an end , which the German Space Agency official interpreted as a possible `` second landing '' on Comet <event id="EE1427.0" sentence_level_value="PS+">67P</event> .</sentence>
```

```
<sentence id="ES1410.18">However , bringing the criminals to justice will be a challenge because the <event id="EE1410.2" sentence_level_value="CT+">sheep</event> chomped their way through quite a lot of the evidence .</sentence>
```

```
<sentence id="ES1397.47">`` <event id="EE1397.2" sentence_level_value="Uu">If</event> properly understood , China 's internal imbalances would be seen not as a risk but as the unavoidable byproduct of a generally successful <event id="EE1397.3" sentence_level_value="CT+">growth</event> process that reflects rapid urbanization and regional specialization in production . ''</sentence>
```

```
<sentence id="ES1226.16">Brown said he expects the `` new <event id="EE1226.2" sentence_level_value="PS+">normal</event> '' caused by the changing climate would exacerbate other problems , including California 's long history of severe droughts .</sentence>
```

