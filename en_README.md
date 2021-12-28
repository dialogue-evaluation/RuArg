# RuArg-2022

# Argument mining evaluation

## Description
Argument mining (or argumentation mining) is a field of computational linguistics that explores methods for extracting from texts and classifying arguments and relationships between them, as well as constructing an argumentative structure. An argument must include a claim containing a stance towards some topic or object, and at least one premise (“favor” or “against”) of this stance. Often a “premise” is called an “argument” when it is clear from the context which claim is being referred to.  
There is a large number of works devoted to argument mining [1–4]. There are also evaluations [5-7], but mainly for the English language. In the RuArg-2022 evaluation, for the first time, it is proposed to test the argument mining systems on the Russian language texts.

There are many tasks of argument mining. We have selected two of them: stance detection and premise classification.
In the first task, it is required to determine the point of view (stance) of the text’s author in relation to the given claim. In the second task, you need to recognize whether the text contains premises “for” or “against” to a given claim.

We have formulated three claims regarding the COVID-19 pandemic (and anti-epidemic measures in general):
1. “Vaccination is beneficial for society.”
1. “The introduction and observance of quarantine is beneficial for society.”
1. “Wearing masks is beneficial for society.”

A collection of sentences was gathered from social networks – comments on posts from social media. These sentences can contain both statements defining the author's stance towards the given claims, and statements with premises “for” / “against” these claims.

Each sentence was annotated by stance and premise for all three claims. Thus, each sentence has six labels.
The following classes (labels) were used:
-	“for” (2);
-	“against” (0);
-	“other” (1) (for stance, this class merges classes “neutral”, “unclear” or “for and against”) / “no argument” (for a premise);
-	"irrelevant" (-1) (for this claim).

The annotated sentences were divided into three corpora: training, validation, and test.
After the announcement of the evaluation, the training and validation corpora are provided. Later, the test corpus will be published (without annotation).

Problem statement: participants are required to automatically annotate each test sentence by stance and premises for each claim (vaccination, quarantine, masks) separately – in total, six labels must be assigned to the sentence. Labels belong to a set of four classes (see above).

The main performance metric in each of the two tasks is the macro F1-score (macro F1<sub>rel</sub>-score), which is averaged first over three relevance classes (the class “irrelevant” is excluded), and then over topics. More precisely, the following procedure is used:
-	for each of the three claims, F1-score is calculated for each class (label) separately;
-	F1-scores are averaged over three out of four classes (the “irrelevant” class is excluded) – macro F1<sub>rel</sub>-score is obtained for a given claim;
-	macro F1<sub>rel</sub>-scores for all three claims are averaged – we get macro F1<sub>rel</sub>-score relative to the task (stance detection or premise classification).

As a result, two main macro F1<sub>rel</sub>-scores will be calculated – one for each task. Participants’ systems will be ranked by these metrics (two separate lists). The F1<sub>rel</sub>-score for claims and F1-score for individual classes (labels) will be considered auxiliary.

Participants who presented their solution at the evaluation can submit a paper for publication, which undergoes double-blind peer review on an equal basis with other participants of the Dialogue conference (for more details see [this link](https://www.dialog-21.ru/evaluation/2022/publish)).

## Timetable
-	December 21, 2021 – publication of the training and validation corpora.
-	February 7, 2022 – publication of the unlabeled test corpus.
-	February 11, 2022 – the end of the submissions of the participants' systems results.
-	February 18, 2022 – the end of the evaluation of the participants' systems results.
-	March 15, 2022 – submission of papers by participants.

## Organizers
-	Natalia Loukachevitch (Moscow State University)
-	Boris Dobrov (Moscow State University)
-	Alexander Panchenko (Skolkovo Institute of Science and Technology)
-	Irina Nikishina (Skolkovo Institute of Science and Technology)
-	Evgeny Kotelnikov (Vyatka State University)

## Links
-	[CodaLab](https://codalab.lisn.upsaclay.fr/competitions/786)
-	[Telegram](https://t.me/+ybQevjgmlFRkMzRi)

## References
1. Lawrence J., Reed C. Argument Mining: A Survey. Computational Linguistics. 2020. Vol. 45(4). P. 765–818.
1. Schaefer R., Stede M. Annotation and detection of arguments in tweets. Proceedings of the 7th Workshop on Argument Mining. 2020. P. 53–58.
1. Trautmann D., Daxenberger J., Stab C., Schütze H., Gurevych I. Fine-Grained Argument Unit Recognition and Classification. 34th AAAI Conference on Artificial Intelligence (AAAI-20). P. 9048–9056.
1. Vecchi E.M., Falk N., Jundi I., Lapesa G. Towards Argument Mining for Social Good: A Survey. Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics. P. 1338–1352.
1. Bondarenko A., Hagen M., Potthast M., Wachsmuth H., Beloucif M., Biemann C., Panchenko A., Stein B. Touché: First Shared Task on Argument Retrieval. Proceedings of the 42nd European Conference on Information Retrieval (ECIR 2020), 2020. P. 517–523.
1. Habernal I., Wachsmuth H., Gurevych I., Stein B. The Argument Reasoning Comprehension Task: Identification and Reconstruction of Implicit Warrants. Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 2018. P. 1930–1940.
1. Pontiki M., Galanis D., Papageorgiou H., Androutsopoulos I., Manandhar S., AL-Smadi M., Al-Ayyoub M., Zhao Y., Qin B., De Clercq O., Hoste V., Apidianaki M., Tannier X., Loukachevitch N., Kotelnikov E., Bel N., Jiménez-Zafra S.M., Eryiğit G. SemEval-2016 Task 5: Aspect Based Sentiment Analysis. Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016). 2016. P. 19–30.
