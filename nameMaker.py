# -*- coding: utf-8 -*-
'''
Created on Sep 20, 2013

@author: bertalan@princeton.edu
'''
from optparse import OptionParser
import pprint as pp; pp = pp.pprint
import random
from matplotlib.pyparsing_py2 import dictOf


# import numpy as np
# import kevrekidis as kv
# import tomSims as ts

# russian = '''Tverdislav
# Afansi Aleksei Anton Boris Daniil Dmitri Efim Feodor Gavril Igor Kapsirko
# Leonid Maksim Nikifor Oleg Pafnuty Pozvizd Radko Sadko Stanislav Tverdislav
# Varlam Vsevolod Yakim Yuri Zakhary  
# '''.strip().split()

vowels = list('aeiou') + ['ei', 'ii']
consonants = list(set('abcdefghijklmnopqrstuvwxyz'.lower()) - set(vowels)) \
         + ['kh', 'vs', 'bj', 'sh', 'ch', 'zh', 'th', 'mw', 'dr', 'cz', 'br',
            'sl', 'tr', 'ph', 'wh']
dictOfNames = {
'russian': u''' Abram Adam Adrian Afanasiy Afanasy Agafya Agata Aglaya Agnessa Agrafena Akilina Akim
 Aksinya Akulina Albert Aleksandr Aleksandra Aleksandrina Aleksei Aleksey Alexei Alexey
 Alisa Alla Allochka Alyona Alyosha Anastas Anastasia Anastasiy Anastasiya Anatoli
 Anatoliy Anatoly Andrei Andrey Anfisa Angela Angelina Ania Anisim Anna Annushka Anton
 Antonina Anushka Anya Anzhela Anzhelina Apollinariya Ariadna Arina Arisha Aristarkh
 Arkadi Arkadiy Arkady Arkhip Arseni Arseniy Artur Artyom Asya Avdotya Avgust Benedikt
 Bogdan Bogdana Boleslav Boleslava Boris Borislav Borislava Borya Bronislav Bronislava
 Daniil Darya David Demyan Denis Desya Diana Dima Dimitri Dmitri Dmitrii Dmitriy Dmitry
 Dominika Dorofei Dorofey Dunya Dunyasha Eduard Ekaterina Elena Elizaveta Ermolai
 Esfir Eva Evdokiya Evgeni Evgeniy Evgeniya Evgeny Evpraksiya Faddei Faddey Faina
 Fedor Fedora Fedot Fedya Feliks Feodor Feodora Feodosiy Feofan Feofil Feofilakt Ferapont
 Filat Filipp Filippa Fima Foka Foma Fyodor Gala Galina Galya Gavriil Gavriila Gena
 Gennadi Gennadiy Gennadiya Gennady Genya Georgiy Georgy Gerasim German Germogen Gleb
 Grigori Grigoriy Grigory Grisha Grusha Igor Ilari Ilia Illarion Ilya Inga Inna Innokenti
 Innokentiy Ioann Iona Iosif Ipati Ipatiy Ippolit Ira Irina Irinei Iriney Irinushka
 Isaak Isay Isidor Isidora Ivan Ivanna Jekaterina Karina Karp Katenka Katerina Katia
 Katya Kazimir Kenya Khariton Kir Kira Kirill Klara Klava Klavdiya Kliment Kolya Konstantin
 Kostya Kristina Kseniya Kuzma Lana Lara Larisa Lavrenti Lavrentiy Lavrenty Lazar
 Lena Leonid Leonti Leontiy Leonty Lev Lidiya Lidochka Lilia Liliya Lilya Liouba Liza
 Lizaveta Luba Ludmilla Luka Lyosha Lyov Lyuba Lyubochka Lyubov Lyudmila Makar Makari
 Makariy Maks Maksim Maksimilian Manya Marfa Margarita Marina Mariya Mark Marlen Martin
 Marya Maryana Masha Matfey Matrona Matryona Matvei Matvey Maxim Mefodiy Melor Mikhail
 Milan Milena Miloslav Miloslava Miron Miroslav Miroslava Misha Mitrofan Mitya Modest
 Modya Moisey Motya Mstislav Nadejda Nadezhda Nadya Nastasia Nastasya Nastya Nata
 Nataliya Natalya Natasha Naum Nazar Nazariy Nestor Nika Nikifor Nikita Nikodim Nikolai
 Nikolay Nikon Nina Nina Ninel Nonna Oksana Oleg Olga Olya'''.strip().split(),
'norweigian': u''' Aage Adam Adolf Adrian Agathe Åge Agnes Agnetha Ågot Aina Aksel Albert Albin Aleksander
 Alexander Alexandra Alf Alf Alfhild Alfred Alv Alva Amanda Amund Anders Andor Andrea
 Andreas Anita Anja Anna Annbjørg Anne Annelie Anniken Ansgar Anton Antonia Arnbjørg
 Arne Aron Arthur Artur Arvid Asbjørn Åse Asgeir Aslaug Åsmund Asta Astrid Audhild
 August Axel Bård Beata Benedikte Bergliot Bergljot Berit Bernhard Bernt Bertil Birger
 Birgit Birgitta Bjarne Bjarte Bjoern Bjørg Bjørn Bodil Borghild Brit Brita Britt
 Britta Brynhild Brynjar Cai Caj Camilla Carina Carl Caroline Casper Cathrine Cecilie
 Charlotte Christen Christian Christin Christina Christine Christoffer Dag Dagfinn
 Dagmar Dagny Dagrun Daniel David Dorothea Ea Ebba Ebbe Edith Edvard Edvin Egil Eilert
 Einar Eindride Eira Eirik Eleonora Eli Elias Elin Elisabet Elisabeth Elise Ella Ellinor
 Else Emanuel Embla Emil Emilia Emilie Emma Endre Enok Erik Erika Erle Erlend Erling
 Esben Espen Ester Eva Felix Filip Finn Folke Frans Fredrik Frida Fridtjof Fritjof
 Frode Frøya Gabriel Geir Georg Gerd Gerda Gina Gjurd Godtfred Gøran Gregers Grete
 Grethe Gro Gry Gudbrand Gudmund Gudrun Gulbrand Gull Gunda Gunhild Gunnar Gunne Gunnhild
 Gunnvor Gunvor Gustav Haakon Håkon Haldor Halldor Halle Hallvard Halstein Halvard
 Halvdan Halvor Hanna Hanna Hanne Hanne Hans Harald Håvard Hedda Hedvig Hege Heidi
 Helena Helene Helga Helge Hella Hemming Henning Henriette Henrik Henrike Herleif
 Herman Hilda Hildegard Hildegarde Hildur Hjalmar Hjørdis Holger Hugo Hulda Ida Ina
 Inga Inge Ingebjørg Ingeborg Ingegerd Inger Ingolf Ingrid Ingvar Ingvild Irene Iris
 Isabella Ivar Jacob Jacobine Jakob Jan Janne Jannicke Jannike Jarl Jarle Jens Jessica
 Joakim Johan Johanna Johanne Johannes Jon Jonas Jonatan Jonathan Jørg Jørgen Jørn
 Jorun Jorunn Josef Judit Julia Kai Kaia Kaj Kaja Kamilla Kåre Karen Kari Karin Karina
 Karine Karl Karla Karolina Karoline Kasper Katarina Katharina Kathrine Katja Katrine
 Kay Kennet Kenneth Kevin Kim Kirsten Kjell Kjellfrid Kjersti Kjerstin Kjetil Klara
 Klaus'''.strip().split(),
'greek': u'''Agape Agapios Agathe Aglaia Aikaterine Akakios Alexandra Alexandros
Alexis Anargyros Anastasia Anastasios Andreas Angeliki Angelos Aniketos Anna
Apostolis Apostolos Argyris Athanasia Athanasios Chara Charalampos Chrysanthe
Chrysanthos Chryssa Demetrios Demi Despina Despoina Diamantina Diamanto
Dimitrios Dimitris Dimosthenis Dionysios Dora Dorotheos Efimia Efrosyni
Efstathios Efthalia Efthymia Eftychia Eleftheria Eleftherios Elene Eleni
Elias Elisavet Elpida Emmanouil Evangelos Evdokia Evgenia Filippa Filippos
Fotini Fotios Fotis Gavriil Georgia Georgios Gerasimos Glykeria Gregorios
Gus Iason Ioanna Ioannes Ioannis Iosif Iro Katerina Katina Kiki Konstantina
Konstantinos Koralia Korina Kyriake Kyriaki Kyriakos Kyveli Lavrentios
Lefteris Leonidas Louiza Maria Marianna Marika Marina Marinos Marios Martha
Matthias Melina Michail Michalis Mihail Mihalis Nana Natasa Neofytos Nicolaos
Nikodemos Nikolaos Nikolas Nikoleta Nomiki Olympia Panagiota Panagiotakis
Panagiotis Panayiotis Panos Paraskevas Paraskeve Paraskevi Pavlos Pelagia
Petra Petros Photios Sara Selene Serafeim Sibylla Silas Sofia Sophia Sotiria
Sotirios Sotiris Spiridon Spiro Spiros Spyridon Spyridoula Spyro Spyros
Stamatia Stamatios Stamatis Stathis Stavros Stefanos Stelios Stephanos
Stylianos Takis Tasia Tasoula Thanasis Thanos Thekla Theodora Theodoros
Theodosia Theophania Theophylaktos Thomas Timothea Tryphon Vangelis Varvara
Vasiliki Vasilios Vasilis Vassilis Vlasis Vlassis Xene Xenia Yanni Yannis
Yianni Yiannis Yiorgos Yorgos Zenovia Zinon Zinovia Zoe
'''.strip().split(),
'sweedish': u''' Acke Adam Adolf Adrian Agata Agda Agnes Agneta Agnetha Aina Åke Albert Albin Alexander
 Alexandra Alf Alf Alfhild Alfred Alva Alvar Amanda Anders Andrea Andreas Anita Anja
 Anna Anne Annelie Annika Ansgar Anton Antonia Arnborg Arne Aron Arthur Artur Arvid
 Åsa Asbjörn Åse Aslög Asta Astrid August Axel Barbro Beata Beatrice Bengt Bengta
 Berit Bernhard Bernt Bertil Birger Birgit Birgitta Bjarne Bjoern Björn Björne Bo
 Bodil Borghild Börje Bosse Brita Britt Britta Cai Caj Cajsa Camilla Carin Carina
 Carita Carl Carola Carolina Caroline Casper Catharina Cathrine Catrine Cecilia Charlotta
 Charlotte Christer Christian Christin Christina Christine Christoffer Cilla Claes
 Dag Dagmar Dagny Daniel David Dorotea Ea Ebba Ebbe Edit Edith Edvard Edvin Egil Eilert
 Einar Eira Eleonora Elias Elin Elina Elis Elisabet Elisabeth Elise Ella Ellinor Elof
 Elov Elsa Elva Emanuel Embla Emelie Emil Emilia Emilie Emma Enok Eric Erica Erik
 Erika Erland Erling Esbjörn Ester Eva Evelina Felicia Felix Filip Filippa Finn Folke
 Frans Fredrik Fredrika Frej Freja Frida Fridtjof Fritjof Gabriel Gabriella Georg
 Gerd Gerda Gerhard Gina Gittan Gjord Göran Gösta Göstav Gottfrid Greger Greta Gry
 Gudmund Gudrun Gull Gunborg Gunda Gunhild Gunilla Gunnar Gunne Gunvor Gustaf Gustav
 Håkan Halsten Halvar Hampus Hanna Hanna Hanne Hans Harald Hasse Hedda Hedvig Heidi
 Helena Helene Helga Helge Hella Helmi Hemming Henning Henrik Henrika Henrike Herman
 Hilda Hildegard Hildegarde Hildur Hillevi Hjalmar Hjördis Holger Hugo Hulda Ida Ina
 Inga Inge Ingeborg Ingegärd Ingegerd Ingemar Inger Ingmar Ingolf Ingrid Ingvar Irene
 Iris Isabella Isak Ivar Jacob Jakob Jan Janina Janna Janne Jannicke Jannike Jarl
 Jarle Jens Jerk Jerker Jessica Joakim Joel Johan Johanna Johannes Jon Jonas Jonatan
 Jonathan Jonna Jöran Jörgen Josef Josefina Judit Julia Kai Kai Kaj Kaj Kaja Kajsa
 Kalle Kamilla Kåre Karin Karina Karita Karl Karla Karolina Kasper Katarina Katharina
 Katja Katrin Katrina Kay Kennet Kenneth Kerstin Kettil Kevin Kia'''.strip().split(),
'vietnamese': u''' An Bảo Bích Bình Cam Châu Chi Chí Cúc Dinh Đức Dũng Dương Hoa Hồng Huệ Hùng Hường
 Kim Lan Lành Liên Linh Mai Minh Ngải Ngọc Nguyên Nguyệt Nhung Phương Phượng Quân
 Quang Quý Quyền Thanh Thi Thu Thuần Thùy Tién Trai Trúc Tú Tuân Tuyến Tuyết Vân Văn
 Viên Vinh Xuân Yên'''.strip().split(),
'turkish': u''' Abdullah Adalet Adem Adnan Ahmed Ahmet Ali Alp Altan Arda Arzu Asil Aslan Asli Asuman
 Ata Atilla Attila Ayberk Aydan Aydin Aygül Aygün Ayla Aylin Ayşe Aysel Aysu Aysun
 Aytaç Aziz Bahadir Bahar Banu Bariş Başak Bayram Behiye Behram Belgin Berk Berkant
 Berker Berna Berrak Beste Beyza Bihter Bilge Bora Buğra Bülent Bulut Bünyamin Burak
 Burçin Burcu Çağatay Çağla Çağri Can Canan Cem Cemal Cemil Cengiz Cenk Ceren Çetin
 Cihan Cihangir Coşkun Cumhur Damla Demir Deniz Derya Devrim Didem Dilan Dilara Dilay
 Dilek Direnç Doruk Duygu Ebru Ece Eda Ediz Egemen Ekin Ekrem Elif Elmas Elvan Emel
 Emin Emine Emir Emre Ender Engin Enis Enver Erdem Eren Erol Esen Eser Esin Esra Evren
 Fahri Fatih Fatma Fatoş Feray Feridun Feriha Ferit Fidan Fikri Fikriye Filiz Firat
 Fuat Funda Fusun Galip Gamze Gaye Gizem Göker Gonca Gözde Gül Gülay Gülbahar Gülden
 Gülistan Gülizar Gülten Günay Gürsel Hakan Halil Halim Haluk Handan Hande Harun Hasan
 Hatice Havva Hayati Haydar Hayri Hazan Hikmet Hülya Hüseyin Hüsnü İbrahim İhsan İlhami
 İlhan İlkay İlker İlkin İlknur İpek Irmak İsa İskender İsmail İsmet İzzet Kaan Kader
 Kadir Kadri Kadriye Kağan Kelebek Kemal Kerem Kerim Kiraz Kivanç Koray Kudret Kuzey
 Lale Latife Levent Leyla Mahzun Makbule Mazhar Mehmed Mehmet Mehtap Melek Meltem
 Mert Meryem Mesud Mesut Metin Mücahit Müge Muhammet Mümtaz Murat Musa Mustafa Nadiye
 Naz Nazli Nergis Nermin Nesrin Nilüfer Nimet Nur Nuray Nurgül Nurten Ömer Onur Orhan
 Osman Ozan Özge Özgür Özlem Pembe Pinar Recep Reyhan Ridvan Riza Rizvan Sabah Sabri
 Sabriye Safiye Şahin Şahnaz Sanem Savaş Şebnem Seda Sedef Şehrazad Şehrazat Şehzade
 Selâhattin Selahattin Selim Semih Semiha Şenay Serhan Serhat Serkan Şermin Serpil
 Sevda Sevgi Sevil Sevinç Sidika Sila Simge Şirin Soner Su Şukri Şukriye Şule Süleyman
 Tahir Taner Tarik Taylan Tayyip Temel Timur Tolga Toygar Tuba Tuğba Tülay Tunç Tuncay
 Turgay Tutku Ufuk'''.strip().split(),
'lovecraftianish': u''' Aomamosab Azstt Boarna Bothig Chuauan-cla Ctho-otha D'guakrudake D'lephothot D'naulam
 Ggn-dh Ibonddh Krnygyguraa L'boaugabol Lalomigu N'ilogo Nthazha Oghurlzos Phalleibhog
 Phararnehot Ra-ph Stuatlot Thol-tloia Thu-kiboma Tlzat-saubota Ygosthl Bbhothaqugg
 Bor-phulel Bosig-rnaiglo Bost Ct'othoshog Dao-ac E'holo Egothigur Gll-haqura Igokilaqu
 Inegnaar Keghasth Kehac-zon Kel-ph Na'mmote Nyotanakr Rhogosharli Rtt'chab Salagug
 Ugggggubolo Ugothacach Ygoth-zsiguat Zhugota Zhul-eny Zotarushaca Aotaqul-oga Chinthan
 Chol-cth Clekr-yot Gogud-mepho Hull-nalosa Hurath Igort Kehosau Ki-tha Krshach-uate
 Krstsachi Maudhoth Mmenatho Momith Ndhugogl Ngubbo Pha-krs Pha-sote Sathola Tephot-thora
 Thagote Ya-mat Yggurlo Zhaugoliq A'rudho Auth-hotl Azo-yaqulllho Closotho Dham-chat
 Ell-chu Elo-phorsho Hangnoth Huaaglh Hugthog-matla Ictelarh Iquboleit Lh'cth Maqugystlla
 Mathaate Nacathol Ogothabbotam Ogursthotu Rachalot Shathai Thaliquau U'sthaubol Ugois
 Ygothugake Zorulla'''.strip().split(),
'egyptianmythology': u'''Amen Ammon Amon Amon-ra Amun Anapa Anoubis Anubis Asar Atem Aten Aton Atum Bast Bastet
 Djehuti Hathor Heru Het-heru Horos Horus Iah Iset Isis Neith Nephthys Nit Osiris
 Ptah Ra Re Set Seth Sutekh Thoth Yamanu'''.strip().split(),
'norsemythology': u''' Alf Alfr Alvis Ask Askr Balder Baldr Borghild Borghildr Brynhildr Eir Embla Frea
 Frey Freya Freyja Freyr Frigg Gandalf Gerd Grid Grímhildr Gróa Gudrun Gunnar Gunnarr
 Guðrún Heidrun Hel Hildr Huld Hulda Idun Iðunn Jarl Loke Loki Nanna Njáll Njord Njörðr
 Oden Odin Ǫrvar Orvar Óðinn Saga Sif Signý Sigrún Sigurd Sigurðr Sindri Siv Skaði
 Skuld Svanhild Svanhildr Thor Þórr Týr Tyr Urd Verdandi Vidar Víðarr Völund Völundr
 Yngvi'''.strip().split(),
'mongolian': u''' Altantsetseg Batbayar Bat-erdene Bolormaa Chingis Enkhjargal Enkhtuya Erdenechimeg
 Ganbaatar Ganzorig Munkhtsetseg Naranbaatar Narantsetseg Nergüi Odtsetseg Otgonbayar
 Oyunchimeg Sarangerel Tömörbaatar'''.strip().split(),
'swahili': u''' Asha Chausiku Eshe Faraji Furaha Imamu Imani Jelani Jengo Jumaane Kamaria Khamisi
 Kibwe Marjani Mchumba Mosi Mwanajuma Mwenye Nia Nuru Nyah Sanaa Sauda Sefu Simba
 Subira Tendaji Zuberi Zuri'''.strip().split(),
'czech': u''' Adam Adéla Adolf Adriana Agáta Albína Alena Aleš Alexandr Alexandra Alexej Alois
 Alžběta Amálie Anastázie Anastazie Anděl Anděla Andrea Andrej Aneta Angelika Anna
 Antonie Antonín Apolena Artur Augustín Augustin Aurel Bára Barbora Bartoloměj Beáta
 Bedřich Běla Benedikt Benedikta Benjamín Berta Blanka Blažej Bohdan Bohumil Bohumila
 Bohumír Bohuslav Bohuslava Boleslav Boleslava Bonifác Bořivoj Božena Božidar Branislav
 Branislava Bronislav Bronislava Cecílie Cecilie Cenek Ctibor Ctirad Cyril Dalibor
 Dalimil Dan Dana Danica Daniel Daniela Darina Darja David Denis Denisa Dobromil Dobroslav
 Dominik Dominika Dorota Doubravka Drahomír Drahomíra Drahoslav Drahoslava Dušan Dušana
 Edita Eduard Edvard Eliška Ema Emil Emílie Erik Erika Ester Eugen Eva Evžen Ferdinand
 Filip František Františka Gabriel Gabriela Hana Havel Hedvika Helena Honza Hynek
 Ignác Ilona Irena Irenka Iva Ivan Ivana Ivanka Iveta Ivona Izabela Jáchym Jakub Jan
 Jana Janek Janička Jarek Jarka Jarmil Jarmila Jaromil Jaromír Jaroslav Jaroslava
 Jindřich Jiří Jiřina Jitka Johan Johana Jolana Jonáš Josef Josefa Judita Justina
 Justýna Kája Kajetán Kamil Kamila Karel Karolína Kateřina Katka Kazimír Klára Klaudie
 Klement Koloman Konrád Kornel Kristina Kristýna Kryštof Kveta Ladislav Ladislava
 Lenka Leoš Libena Libor Libuše Lída Linda Livie Lubomír Luboš Lucie Luděk Ludmila
 Ludvík Lukáš Lýdie Madlenka Magda Magdaléna Magdalena Mahulena Maja Malena Marcel
 Marcela Marek Marián Marian Mariana Marie Marika Markéta Marta Martin Martina Máša
 Matěj Matouš Matylda Maxmilián Melánie Metoděj Michael Michaela Michal Michala Mikoláš
 Mikula Mikuláš Mila Milada Milan Milana Milena Miloš Miloslav Miloslava Mirek Miroslav
 Miroslava Monika Mstislav Naďa Naděžda Natálie Nicol Nicola Nicole Nikol Nikola Nikola
 Nina Noemi Oldřich Olga Oliver Olivie Ondřej Otakar Otmar Otokar Patricie Patrik
 Pavel Pavla Pavlina Petr Petra Přemysl Radana Radek Radim Radka Radko Radmila Radomil
 Radomila Radomír Radomíra Radoš Radoslav Radoslava Radovan Radúz Řehoř Renáta Renata
 René Richard Robert Roman Romana Rostislav Rudolf Růžena Sabina Samuel Sára Šárka
 Silvestr Silvie Šimon Šimona Simona Slavěna Slavomír Sofie Soňa'''.strip().split(),
'chinese': u''' Ah Ai An Bai Bao Bo Chang Chao Chen Cheng Chin Chun Da Dong Fen Fu Gang Guo Hai He
 Heng Hong Hua Huan Huang Hui Jia Jian Jiang Jin Jing Ju Jun Kun Lan Li Lim Lin Ling
 Mei Min Ming Mu Ning Nuan Nuo Ping Qiang Qing Qiu Rong Ru Shi Shu Shui Shun Su Tai
 Tu Wei Wen Wu Xiang Xiu Xue Xun Ya Yi Yin Yong Yu Yun Zan Zhen Zheng Zhi Zhong Zhou'''.strip().split(),
'japanese': u''' Ai Aiko Aimi Aina Airi Akane Akemi Aki Akiko Akio Akira Ami Aoi Arata Asuka Atsuko
 Aya Ayaka Ayako Ayame Ayane Ayano Ayumu Chika Chikako Chinatsu Chiyo Chiyoko Cho
 Chou Chouko Daichi Daiki Daisuke Emi Etsuko Goro Gorou Hachiro Hachirou Hana Hanako
 Haru Haruka Haruki Haruko Haruna Haruto Hayate Hayato Hibiki Hideaki Hideki Hideyoshi
 Hikari Hikaru Hina Hinata Hiraku Hiroko Hiroshi Hiroto Hitomi Honoka Hoshi Hoshiko
 Hotaka Hotaru Ichiro Ichirou Isamu Itsuki Izumi Jiro Jirou Junko Juro Jurou Kaede
 Kaito Kanon Kaori Kaoru Kasumi Katashi Katsu Katsuo Katsuro Katsurou Kazue Kazuki
 Kazuko Kazuo Keiko Ken Ken'ichi Kenji Kenshin Kenta Kichiro Kichirou Kiku Kimiko
 Kiyoko Kiyoshi Kohaku Kokoro Kotone Kouki Kouta Kumiko Kuro Kurou Kyo Kyou Mai Makoto
 Mami Manami Mao Mariko Masami Masaru Masuyo Mayu Megumi Mei Michi Michiko Midori
 Mika Miki Miku Minako Minoru Mio Misaki Mitsuko Miu Miyako Miyu Mizuki Moe Momoka
 Momoko Moriko Nana Nanami Naoki Naoko Naomi Natsuki Natsuko Natsumi Noa Noboru Nobu
 Noburu Nobuyuki Nori Noriko Osamu Ran Rei Ren Riko Riku Rikuto Rin Rina Rio Rokuro
 Rokurou Ryo Ryoichi Ryota Ryou Ryouichi Ryouta Ryuu Ryuunosuke Saburo Saburou Sachiko
 Saki Sakura Sakurako Satomi Sayuri Setsuko Shichiro Shichirou Shin Shinju Shinobu
 Shiori Shiro Shirou Shizuka Sho Shou Shouta Shun Sora Souta Sumiko Susumu Suzu Suzume
 Taichi Taiki Takahiro Takako Takara Takashi Takehiko Takeshi Takuma Takumi Tamiko
 Taro Tarou Tomiko Tomoko Tomomi Tsubaki Tsubame Tsubasa Tsukiko Ume Umeko Wakana
 Yamato Yasu Yoko Yori Yoshi Yoshiko Yoshiro Yoshirou Youko Youta Yua Yui Yuina Yuki
 Yukiko Yuko Yumi Yumiko Yuri Yuu Yuudai Yuuka Yuuki Yuuko Yuuma Yuuna Yuuta Yuuto
 Yuzuki'''.strip().split(),
'hungarian': u''' Ábel Ada Ádám Adél Adelaida Adorján Adrienn Ági Ágnes Ágoston Ágota Ákos Alajos Albert
 Alberta Alexander Alexandra Alfréd Alida Aliz Álmos Amália Ambrus Anasztáz Anasztázia
 Andor András Andrea Andris Angyalka Anikó Anna Annuska Antal Antónia Aranka Arisztid
 Áron Árpád Artúr Attila Aurél Aurélia Balázs Bálint Bandi Barbara Barna Barnabás
 Bartal Beáta Béla Bence Benedek Benjámin Bernadett Bernát Berta Bertalan Bertók Bianka
 Blanka Boldizsár Bonifác Borbála Bözsi Brigitta Cecília Cili Csaba Csenge Csilla
 Dani Dániel Dávid Délia Demeter Dénes Dezső Diána Dominik Domonkos Dömötör Donát
 Dóra Dorika Dorina Dorottya Duci Edina Edit Eduárd Edvárd Edvin Elek Éliás Emánuel
 Emese Emil Endre Enikő Erik Erika Ernő Ervin Erzsébet Erzsi Eszter Eszti Etel Etele
 Etelka Eufrozina Eulália Éva Évike Fábián Fabó Fanni Felícia Felicia Felicitás Ferdinánd
 Ferenc Feri Ferkó Filip Flóra Franci Franciska Frigyes Fruzsina Fülöp Gabi Gábor
 Gábriel Gabriella Gáspár Gazsi Gellért Gergely Gergő Gertrúd Géza Gizella Gizi Gréta
 Gusztáv Gyöngyi György Györgyi Györgyike Győző Gyula Gyuri Hajna Hajnal Hajnalka
 Heléna Henrik Ibolya Ida Ignác Ildi Ildikó Ildó Ili Ilka Illés Ilona Ilonka Imre
 Imrus Irén Irma Irmuska István Izabella Izidóra Izsák Jakab Jákob Jancsi Jani Janika
 János Jázmin Jenci Jenő Johanna Jola Jolán Jolánka Jóska Jozefa József Józsi Józsua
 Judit Juli Júlia Julianna Juliska Kajetán Kálmán Kamilla Karcsi Karola Karolina Károly
 Kata Katalin Katalinka Katarina Kati Kató Kazimír Kázmér Kelemen Kinga Kitti Klára
 Klotild Konrád Konstantin Kornél Kornélia Kristóf Krisztián Krisztina Laci Lajos
 Lara László Laura Lázár Liliána Linda Liza Loránd Lóránt Lőrinc Luca Lujza Lukács
 Magdaléna Magdolna Mara Marcell Margaréta Margit Margita Mari Mária Marián Marianna
 Marica Marika Mariska Márk Márta Martin Márton Mártuska Máté Matild Mátyás Melánia
 Mihály Miklós Miksa Miléna Misi Miska Mónika Móric Mózes Nándor Natália Nikola Nikolett
 Norbert Ödi Ödön Olga Olimpia Olivér Olívia Orbán Orsolya Oszkár Ottó Pál Panni Patrik
 Paula Péter Peti Petra Piri'''.strip().split(),
'arabic': u''' Aali Aaliyah Aamina Aaminah 'abbas Abbas Abd-al-aziz Abd-al-hamid Abd-al-kader Abd-al-karim
 Abd-allah Abd-al-latif Abd-al-malik Abd-al-qadir Abd-al-rahman Abd-al-rashid Abdul
 Abdul-aziz Abdul-hamid Abdullah Abdul-rahman Abdur-rashid 'abla Abu Abu Abu Adam
 Adel Adil Adnan Afaf Afif Afra Afzal Ahmad Ahmed Aida 'aisha Akeem Akilah Akram Ala
 Ala Ali Alia Alim Alina Aliya Aliyah Aliyya Aliyyah Almas Alya Amal Amani Amin Amina
 Aminah Aminah Amir Amira Amirah Amjad 'ammar Amna Anas Anass Anisa Anwar Anwer Aqil
 Aqila Arij Arwa As'ad Asad Ashfaq Asif Asim Asma Asmaa Asra Ata Atallah Ataullah
 Atifa Atiya Atuf Ayda Ayesha Ayishah Ayman Azhar 'aziz Badr Baha Bahadur Bahiga Bahij
 Bahija Bahiyya Baki Bakr Baqi Baqir Barack Barak Barakat Basil Basim Basima Basir
 Basira Basit Basma Bassam Bassem Batul Bilal Binyamin Botros Boulos Boutros Budur
 Bulus Butrus Dalal Daniyah Daud Dawood Dawud Dema Dima Diya Djamila Dua Duha Ebrahim
 Esmail Essa Fadi Fadia Fadil Fadila Fadl Fahd Fahim Fahima Fairuz Faiz Faiza Faizel
 Fakhri Fakhriyya Farag Farah Faraj Fareed Farid Farida Fariha Faris Farooq Farouk
 Farrah Faruq Fathi Fathiyya Fatima Fatimah Fatin Fatma Fawzi Fawziya Fawziyya Fayiz
 Fayruz Faysal Fayza Fazl Fidda Fihr Fikri Fikriyya Firdaus Firdos Firuz Fizza Fouad
 Fuad Gabir Gabr Gafar Galal Galila Gamal Gamil Gamila Gathbiyya Gauhar Gawahir Gawdat
 Gazbiyya Ghada Ghadir Ghalib Ghaliya Ghassan Ghayth Ghufran Guda Gulzar Habib Habiba
 Hadi Hadia Hadil Hadiya Hadiyya Hadjara Hadya Hafeez Hafiz Hafsa Hafsah Hafza Hagir
 Haidar Haider Haifa Hajar Hakeem Hakim Hala Hameed Hamid Hamza Hana Hanaa Hanan Hani
 Hania Hanif Hanifa Haniyah Haniyya Harith Haroun Harun Hasan Hashim Hasib Hasim Hassan
 Hatim Hawa Hayder Hayfa Haytham Hesham Hiba Hikmat Hind Hisein Hisham Hooda Hosni
 Houda Houssam Huda Husain Husam Husayn Husni Hussain Hussein Hyder Ibraheem Ibrahim
 Ibtihaj Ibtisam Ihab Ihsan Ikraam Ikram Ilham Ilyas Imad Imam Iman Imen Imram Imran
 Imtiyaz In'am Inas Iqbal Irfan Isa 'isam'''.strip().split(),
'spanish': u''' Aarón Abel Abene Abigaíl Abilio Adalberto Adán Adela Adelaida Adelia Adelina Adelita
 Adolfito Adolfo Adora Adoración Adrià Adrián Adriana Afonso África Agapito Agata
 Agnès Águeda Agurne Agurtzane Agustí Agustín Agustina Aina Aingeru Ainhoa Aintza
 Aintzane Aitor Alaia Alazne Alba Alberte Alberto Ale Aleix Aleixo Alejandra Alejandro
 Alejo Alesander Àlex Alexandra Alexandre Alfonso Alfredo Alícia Alicia Alita Alma
 Almudena Alondra Alonso Álvaro Amada Amado Amaia Amalia Amancio Amanda Amando Amaranta
 Amarilis Amaya Ámbar Ambrosio Amelia América Américo Amets Amílcar Amparo Ana Anabel
 Anacleto Anaïs Anastasia Anastasio Ander Andoni Andrés Andreu Ángel Àngel Ángela
 Angélica Angelina Angelino Angelita Aníbal Anita Anna Anne Anselma Anselmo Antía
 Antón Antoni Antonia Antonio Antton Anunciación Anxo Apolinar Araceli Aracelis Aracely
 Arantxa Arantzazu Arcelia Argi Argider Argiñe Ariadna Aristides Arkaitz Armando Armida
 Arnau Arrats Arsenio Artur Arturo Ascensión Asdrubal Asier Assumpció Asun Asunción
 Atilio August Augusto Aureliano Aurelio Aurora Azeneth Azucena Bakar Bakarne Balbina
 Baldomero Balduino Balendin Baltasar Bartolomé Bartolomeu Bartomeu Basajaun Basilio
 Baudelio Bautista Beatriu Beatriz Belén Beñat Benigna Benigno Benita Benito Benjamín
 Berezi Bernardino Bernardita Bernardo Bernat Berta Bethania Bibiana Bidane Bieito
 Bienvenida Bihotz Bikendi Bittor Blanca Blas Bolívar Bonifacio Brais Branca Breixo
 Brigida Brunilda Bruno Buenaventura Calista Calisto Calixta Calixto Camila Camilo
 Cande Candela Candelaria Candelario Candelas Cándida Caridad Carla Carles Carlito
 Carlitos Carlos Carlota Carme Carmela Carmelita Carmelo Carmen Carmina Carolina Casimiro
 Catalina Catarina Caterina Cayetano Cebrián Cecilia Cecilio Ceferino Celestina Celestino
 Celia Celino Celio Celso César Charo Che Chelo Chimo Chita Chucho Chus Chuy Cibrán
 Cipriano Ciríaco Ciriaco Cirino Ciro Clara Clarisa Claudia Claudio Clemente Clementina
 Cleto Clímaco Cloe Concepción Concha Conchita Conrado Constanza Consuela Consuelo
 Cornelio Crescencia Cristián Cristina Cristóbal Cruz Cruzita Curro Custodia Custodio
 Dalia Danel Dani Dania Daniel Daniela Danilo Darío David Débora Delfina Delia Demetrio
 Desi Desideria Desiderio Diana Dídac Diego Dimas Dionisio Dolores Dolors Dominga
 Domingo Domitila'''.strip().split(),
'hindusanskritpunjabi': u''' Abha Abhay Abhilasha Aditi Aditya Agni Aishwarya Ajeet Ajit Ajith Akanksha Akash
 Akhil Amala Amar Amit Amita Amrit Amrita Anand Ananda Anandi Ananta Ananth Anantha
 Anil Anila Anima Aniruddha Anish Anjali Ankita Ankur Anuj Anuja Anupam Anupama Aparajita
 Aradhana Aravind Aravinda Archana Arjun Arjuna Arun Aruna Arundhati Arya Aseem Asha
 Ashok Ashoka Asim Avani Avanti Avinash Bala Baladeva Baldev Basant Basu Bharat Bharata
 Bhaskar Bhaskara Bijay Bijoy Bipin Bishen Brahma Brijesh Brijesha Buddha Chanda Chandan
 Chandana Chander Chandra Chandrakant Chandrakanta Chetan Chetana Chiranjeevi Chiranjivi
 Damayanti Damodar Damodara Darshana Dayaram Debdan Deepak Deepali Deepti Deo Deodan
 Dev Devadas Devaraja Devdan Devdas Devi Devika Devraj Dhananjay Dhaval Dilip Dilipa
 Dinesh Dipak Dipaka Dipali Dipika Dipti Divya Draupadi Drishti Drupada Duleep Durai
 Durga Esha Ganesh Ganesha Gauri Gautam Gautama Geevarghese Girish Girisha Gita Gobind
 Gopal Gopala Gopinath Gopinatha Gotam Gotama Govind Govinda Gowri Harendra Hari Harinder
 Harish Harisha Harsha Harshad Harshal Ila Inderjit Inderpal Indira Indra Indrajit
 Indrani Indu Isha Jagannath Jagannatha Jagdish Jagjit Jai Jaidev Jaswinder Jay Jaya
 Jayant Jayanta Jayanti Jayashri Jayendra Jaywant Jeetendra Jitender Jitendra Jitinder
 Jyoti Jyotsana Jyotsna Kailash Kajal Kala Kali Kalidas Kalidasa Kalpana Kalyan Kalyana
 Kalyani Kama Kamal Kamala Kamini Kanchana Kanta Kanti Kapil Kapila Karan Karishma
 Karna Kashi Kasi Kaur Kausalya Kaveri Kavi Kavita Kiran Kirtida Kishan Kishen Kishor
 Kishore Kishori Kistna Krishna Kshitij Kshitija Kumar Kumara Kumari Kunal Kunala
 Kunti Lakshman Lakshmana Lakshmi Lal Lalit Lalita Lata Lavanya Laxman Laxmi Leela
 Lila Lilavati Lina Lochan Lochana Madhav Madhava Madhavi Madhu Madhukar Madhur Madhuri
 Mahavir Mahavira Mahendra Mahesh Mahesha Mahinder Mala Malati Malini Mandeep Mani
 Maninder Manish Manisha Manju Manjula Manjusha Manu Maya Mayur Meena Meera Mina Minali
 Mira Mitul Mohan Mohana Mohandas Mohinder Mohini Mridula Mukesh Mukesha Mukta Mukul
 Murali Nagendra Nala Nalini Nanda Nandita Narayan Narayana Narendra Narinder Naveen
 Navin Neela Neelam Neha Nikhil'''.strip().split(),
}
# dictOfNames = {'russian': russian, 'greek': greek, 'norweigian': norweigian,
#                'sweedish': sweedish, 'scandinavian': sweedish + norweigian,
#                'vietnamese': vietnamese, 'turkish': turkish,
#                'lovecraftianish': lovecraftianish, 'egyptianmythology': egyptianmythology,
#                'norsemythology': norsemythology, 'mongolian': mongolian,
#                'swahili': swahili, 'czech': czech}


def splitConsonants(part):
    if part not in vowels and len(part) > 1:
        print part


def getSyllables(name):
    modified = unicode(name.lower())
    for vowel in vowels:
        modified = modified.replace(vowel, '#'+vowel+'#')
    parts = [s for s in modified.split('#') if s is not '']
    syls = []
    syl = ''
    for i in range(len(parts)):
        part = parts[i]
        if part not in vowels:
            syl += part
            if i == len(parts)-1:
                syls.append(part)
        else:
            syl += part
            syls.append(syl)
            syl = ''
    def fixSyls(syls):
        for i in range(1, len(syls)):
            this = syls[i]
            prev = syls[i-1]
            if len(this) > 1:
                if this[:2] not in consonants:
                    prev += this[0]
                    this = this[1:]
            elif this in consonants:
                prev += this[0]
                this = this[1:]
            syls[i] = this
            syls[i-1] = prev
        return syls
    syls = fixSyls(syls)
    return [s for s in syls if s is not '']
#         splitConsonants(part)


def allSyls(names):
    toSum = [set(getSyllables(name)) for name in names]
    rsyls = set()
    for syls in toSum:
        rsyls = rsyls.union(syls)
    return [l for l in list(rsyls) if len(l) > 0]


def name(names, numSyls=None):
    sylList = allSyls(names)
    if numSyls is None:
        numSyls = random.randint(1, 5)
    random.shuffle(sylList)
    return ''.join(sylList[:numSyls]).capitalize()

        
def lfill(string, length, filler=' '):
    if len(string) < length:
        filling = filler * (length - len(string))
        return filling + string
    else:
        return string[:length]


def demo(verbosity=0):
    fillLength = max([len(lang) for lang in dictOfNames.keys()]) + 17
    for language in sorted(dictOfNames.keys()):
        if verbosity > 0:
            print
            random.shuffle(dictOfNames[language])
            print lfill("Some "+language.capitalize()+" names:", fillLength),
            print dictOfNames[language][:5]
        if verbosity > 1:
            someSyls = allSyls(dictOfNames[language])
            random.shuffle(someSyls)
            someSyls = someSyls[:6]
            print lfill("Some "+language.capitalize() + " syllables:", fillLength),
            print someSyls
        print lfill(language.capitalize()+"-ish:", fillLength),
        print name(dictOfNames[language])


def main():
    usage = "usage: %prog [options] language"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--demo", dest="demo", action='store_true',
                      help='Show a demo.')
    parser.add_option("-t", '--trueName', dest='trueName', action='store_true',
                      help='Give a name from the actual corpus.')
    parser.add_option('-n', '--numSyls', dest='numSyls', default=None,
                      help='How many syllables to use in the generated name.')
    parser.add_option('-v', '--verbosity', default=0,
                      help='Level of extra information to show in the demo.')

    (options, args) = parser.parse_args()
    
    if options.demo:
        demo(int(options.verbosity))
    else:
        def err(msg):
            parser.print_help()
            print
            from sys import exit; exit("ERROR: " + msg)
        if len(args) == 0:
            err("Give positional argument 'language', one of: \n    "
                         + ' '.join(sorted(dictOfNames.keys())))
        key = args[0].lower()
        if key not in dictOfNames:
            err("'"+key.lower()+"'" + " not one of: \n    " +
                ' '.join(sorted(dictOfNames.keys())))
        if options.trueName:
            names = dictOfNames[key]
            print random.choice(names)
        else:
            numSyls = options.numSyls
            if numSyls is not None:
                numSyls = int(numSyls)
            print name(dictOfNames[key], numSyls=numSyls)


if __name__ == '__main__':
    main()
#     print allSyls(dictOfNames['spanish'])
