"""
author : ridowan
tanggal : 19 april 2017
"""
# import libraries
import urllib2  
from bs4 import BeautifulSoup

import csv  
from datetime import datetime

import datetime
i = datetime.datetime.now()
# specify the url
url = [
	#Prov Aceh
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banda%20Aceh&AreaID=501397&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bireun&AreaID=501398&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Blang%20Kejeren&AreaID=501399&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Blangpidie&AreaID=501400&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Calang&AreaID=501401&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Idi%20Rayeuk&AreaID=501402&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Karang%20Baru&AreaID=501403&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Jantho&AreaID=501404&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kutacane&AreaID=501405&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Langsa&AreaID=501406&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lhokseumawe&AreaID=501407&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lhoksukon&AreaID=501408&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Meulaboh&AreaID=501409&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Meureundu&AreaID=501605&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sabang&AreaID=501410&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sigli&AreaID=501411&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Simpang%20Tiga%20Redelong&AreaID=501412&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sinabang&AreaID=501413&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Singkil&AreaID=501414&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Subulussalam&AreaID=501606&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Suka%20Makmue&AreaID=501415&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Takengon&AreaID=501416&Prov=1',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tapaktuan&AreaID=501417&Prov=1',
	#Banten
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Anyer&AreaID=5002202&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bayah&AreaID=5002245&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Binuangen&AreaID=5002244&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bojonegara&AreaID=5002208&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Carita&AreaID=5002209&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cilegon&AreaID=501171&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ciruas&AreaID=501597&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gunung%20kencana&AreaID=5002205&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Labuhan&AreaID=5002203&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lebak&AreaID=5002207&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Malingping&AreaID=5002206&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Merak&AreaID=5002201&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pandeglang&AreaID=501172&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rangkas%20Bitung&AreaID=501173&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Serang&AreaID=501174&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tangerang&AreaID=501175&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tigaraksa&AreaID=501176&Prov=4',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ujung%20Kulon&AreaID=5002204&Prov=4',
	#DKI Jakarta
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bekasi&AreaID=501214&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bogor&AreaID=501215&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Depok&AreaID=501223&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jakarta%20Barat&AreaID=501192&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jakarta%20Pusat&AreaID=501195&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jakarta%20Selatan&AreaID=501193&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jakarta%20Timur&AreaID=501191&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jakarta%20Utara&AreaID=501196&Prov=7',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kepulauan%20Seribu&AreaID=501194&Prov=7',
	#Jawa Barat
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bandung&AreaID=501212&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banjar&AreaID=501213&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ciamis&AreaID=501216&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cianjur&AreaID=501217&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cibinong&AreaID=501218&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cikarang&AreaID=501219&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cimahi&AreaID=501220&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cirebon&AreaID=501221&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cisaat&AreaID=501222&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Garut&AreaID=501224&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Indramayu&AreaID=501225&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Karawang&AreaID=501226&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kuningan&AreaID=501227&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Majalengka&AreaID=501228&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ngamprah&AreaID=501599&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pelabuhan%20Ratu&AreaID=501229&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Purwakarta&AreaID=501230&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Singaparna&AreaID=501231&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Soreang&AreaID=501232&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Subang&AreaID=501233&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sumber&AreaID=501234&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sumedang&AreaID=501235&Prov=10',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tasikmalaya&AreaID=501236&Prov=10',
	#Kalimantan Barat
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bengkayang&AreaID=501310&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kapuas%20Hulu&AreaID=5002241&Prov=13', #Kapuas Hulu
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kayong%20Utara&AreaID=5002243&Prov=13', #Kayong Utara
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ketapang&AreaID=501311&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kubu%20Raya&AreaID=5002218&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Landak&AreaID=501312&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Melawi&AreaID=5002242&Prov=13', #Melawi
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mempawah&AreaID=501313&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pontianak&AreaID=501315&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sambas&AreaID=501317&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sanggau&AreaID=501318&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sekadau&AreaID=501319&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Singkawang&AreaID=501320&Prov=13',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sintang&AreaID=501321&Prov=13',
	#Kalimantan Timur
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Balikpapan&AreaID=501349&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bontang&AreaID=501350&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Penajam&AreaID=501353&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Samarinda&AreaID=501354&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sendawar&AreaID=501355&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sengata&AreaID=501356&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanah%20Grogot&AreaID=501357&Prov=16',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tenggarong&AreaID=501361&Prov=16',
	#Lampung
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bandar%20Lampung&AreaID=501373&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Blambangan%20Umpu&AreaID=501374&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gunung%20Sugih&AreaID=501375&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kalianda&AreaID=501376&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Agung&AreaID=501377&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kotabumi&AreaID=501378&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Liwa&AreaID=501379&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Menggala&AreaID=501380&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Metro&AreaID=501381&Prov=19',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sukadana&AreaID=5002234&Prov=19',
	#Nusa Tenggara Barat
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Bima&AreaID=501418&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Dompu&AreaID=501419&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gerung&AreaID=501420&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mataram&AreaID=501421&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Praya&AreaID=501422&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sape&AreaID=5002222&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Selong&AreaID=501423&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sumbawa%20Besar&AreaID=501424&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Taliwang&AreaID=501425&Prov=22',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung&AreaID=5002223&Prov=22',
	#Bali
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Amplapura&AreaID=501162&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bangli&AreaID=501163&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Denpasar&AreaID=501164&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gianyar&AreaID=501165&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mangupura&AreaID=501166&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Negara&AreaID=501167&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Semarapura&AreaID=501168&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Singaraja&AreaID=501169&Prov=2',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tabanan&AreaID=501170&Prov=2',
	#Bangka Belitung
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jebus&AreaID=5002247&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Koba&AreaID=501362&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Manggar&AreaID=501363&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mentok&AreaID=501364&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkal%20Pinang&AreaID=501365&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Selat%20Nasik&AreaID=5002249&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sungai%20Liat&AreaID=501366&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sungai%20Selan&AreaID=5002248&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Pandan&AreaID=501367&Prov=3',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Toboali&AreaID=501368&Prov=3',
	#Bengkulu
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bengkulu%20Utara&AreaID=501177&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bengkulu&AreaID=501178&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kaur&AreaID=501179&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rejang%20Lebong&AreaID=501180&Prov=5', 
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kepahiang&AreaID=501181&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bengkulu%20Selatan&AreaID=501182&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mukomuko&AreaID=501183&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Seluma&AreaID=501184&Prov=5',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lebong&AreaID=501185&Prov=5',
	#DI Yogyakarta
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bantul&AreaID=501186&Prov=6',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sleman&AreaID=501187&Prov=6',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wates&AreaID=501188&Prov=6',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wonosari&AreaID=501189&Prov=6',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Yogyakarta&AreaID=501190&Prov=6',
	#Gorontalo
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gorontalo&AreaID=501197&Prov=8',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kwandang&AreaID=501598&Prov=8',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Limboto&AreaID=501198&Prov=8',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Marisa&AreaID=501199&Prov=8',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Suwawa&AreaID=501200&Prov=8',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tilamuta&AreaID=501201&Prov=8',
	#Jambi
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bangko&AreaID=501202&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bulian&AreaID=501203&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bungo&AreaID=501204&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jambi&AreaID=501205&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kerinci&AreaID=5002260&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kuala%20Tungkal&AreaID=501207&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sabak&AreaID=501208&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sarolangun&AreaID=501209&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sengeti&AreaID=501210&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sungai%20Penuh&AreaID=501206&Prov=9',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tebo&AreaID=501211&Prov=9',
	#Jawa Tengah
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banjarnegara&AreaID=501237&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Batang&AreaID=501238&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Blora&AreaID=501239&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Boyolali&AreaID=501240&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Brebes&AreaID=501241&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Cilacap&AreaID=501242&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Demak&AreaID=501243&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jepara&AreaID=501244&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kajen&AreaID=501245&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Karanganyar&AreaID=501246&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kebumen&AreaID=501247&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kendal&AreaID=501248&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Klaten&AreaID=501249&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kudus&AreaID=501250&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Magelang&AreaID=501251&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mungkid&AreaID=501252&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pati&AreaID=501253&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pekalongan&AreaID=501254&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pemalang&AreaID=501255&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Purbalingga&AreaID=501256&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Purwodadi&AreaID=501257&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Purwokerto&AreaID=501258&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Purworejo&AreaID=501259&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rembang&AreaID=501260&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Salatiga&AreaID=501261&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Slawi&AreaID=501263&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sragen&AreaID=501264&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sukoharjo&AreaID=501265&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Surakarta&AreaID=501266&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tegal&AreaID=501267&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Temanggung&AreaID=501268&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ungaran&AreaID=501269&Prov=11',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wonosobo&AreaID=501271&Prov=11',
	#Jawa Timur
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bangkalan&AreaID=501272&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banyuwangi&AreaID=501273&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Batu&AreaID=501274&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bojonegoro&AreaID=501277&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gresik&AreaID=501279&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jember&AreaID=501280&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jombang&AreaID=501281&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Blitar&AreaID=5002271&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Kediri&AreaID=5002268&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Madiun&AreaID=501288&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Malang&AreaID=501284&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Mojokerto&AreaID=5002269&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Pasuruan&AreaID=5002272&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabupaten%20Probolinggo&AreaID=5002270&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Blitar&AreaID=501275&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Kediri&AreaID=501282&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Madiun&AreaID=501287&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Malang&AreaID=501290&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Mojokerto&AreaID=501291&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Pasuruan&AreaID=501297&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Probolinggo&AreaID=501300&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lamongan&AreaID=501285&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lumajang&AreaID=501286&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Magetan&AreaID=501289&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Nganjuk&AreaID=501293&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ngawi&AreaID=501294&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pacitan&AreaID=501295&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pamekasan&AreaID=501296&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ponorogo&AreaID=501299&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sampang&AreaID=501302&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sidoarjo&AreaID=501303&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Situbondo&AreaID=501304&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sumenep&AreaID=501305&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Surabaya&AreaID=501306&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Trenggalek&AreaID=501307&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tuban&AreaID=501308&Prov=12',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tulungagung&AreaID=501309&Prov=12',
	#Kalimantan Selatan
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Amuntai&AreaID=501323&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banjarbaru&AreaID=501324&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Banjarmasin&AreaID=501325&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Batulicin&AreaID=501326&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Berabai&AreaID=501327&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kandangan&AreaID=501328&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kotabaru&AreaID=501329&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Marabahan&AreaID=501330&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Martapura&AreaID=501563&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Paringin&AreaID=501332&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pelaihari&AreaID=501333&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rantau&AreaID=501334&Prov=14',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung&AreaID=501426&Prov=14',
	#Kalimantan Tengah
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Buntok&AreaID=501335&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kasongan&AreaID=501336&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kuala%20Kapuas&AreaID=501337&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kuala%20Kurun&AreaID=501338&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kuala%20Pembuang&AreaID=501339&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Muarateweh&AreaID=501340&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Nanga%20Bulik&AreaID=501341&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palangkaraya&AreaID=501342&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkalan%20Bun&AreaID=501343&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkalan%20Bun&AreaID=501343&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pulangpisau&AreaID=501344&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Puruk%20Cahu&AreaID=501345&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sampit&AreaID=501346&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sukamara&AreaID=501347&Prov=15',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tamiang%20Layang&AreaID=501348&Prov=15',
	#Kalimantan Utara
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Malinau&AreaID=501351&Prov=17',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Nunukan&AreaID=501352&Prov=17',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Redeb&AreaID=501358&Prov=17',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Selor&AreaID=501359&Prov=17',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tarakan&AreaID=501360&Prov=17',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tana%20Tidung&AreaID=501600&Prov=17',
	#Kep Riau
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Batam&AreaID=501601&Prov=18',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Daik%20Lingga&AreaID=501369&Prov=18',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ranai&AreaID=501370&Prov=18',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Balai%20Karimun&AreaID=501603&Prov=18',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Pinang&AreaID=501371&Prov=18',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tarempa&AreaID=501372&Prov=18',
	#Riau
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bagan%20Siapiapi&AreaID=501472&Prov=26', #Kab Rokan Hilir
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bangkinang&AreaID=501473&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bengkalis&AreaID=501474&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Dumai&AreaID=501475&Prov=26', #Kota Dumai
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkalan%20Kerinci&AreaID=501476&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pasir%20Pengarairan&AreaID=501477&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pekanbaru&AreaID=501478&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rengat&AreaID=501479&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Selat%20panjang&AreaID=5002217&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Siak%20Sri%20Indrapura&AreaID=501480&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Teluk%20Kuantan&AreaID=501481&Prov=26',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tembilahan&AreaID=501482&Prov=26',
	#Sumatera Utara
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Aek%20Kanopan&AreaID=5002212&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Balige&AreaID=501573&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Binjai%20Kota&AreaID=501574&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Dolok%20Sanggul&AreaID=501575&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gunung%20Sitoli&AreaID=501576&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Gunung%20Tua&AreaID=5002214&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kabanjahe&AreaID=501577&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kisaran&AreaID=501578&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Pinang&AreaID=5002211&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lahomi&AreaID=5002216&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lima%20Puluh&AreaID=5002210&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lotu&AreaID=5002215&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lubuk%20Pakam&AreaID=501579&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Medan&AreaID=501580&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Padang%20Sidempuan&AreaID=501581&Prov=34', #Kota Padang Sidempuan
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangururan&AreaID=501583&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Panyabungan&AreaID=501584&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pematang%20Raya&AreaID=501585&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pematang%20Siantar&AreaID=501586&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rantau%20Prapat&AreaID=501587&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Salak&AreaID=501588&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sei%20Rampah&AreaID=501589&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sibolga&AreaID=501590&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sibuhuan&AreaID=5002213&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sidikalang&AreaID=501591&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sipirok&AreaID=501592&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Stabat&AreaID=501593&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanjung%20Balai&AreaID=501594&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tarutung&AreaID=501595&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tebing%20Tinggi&AreaID=501572&Prov=34',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Teluk%20Dalam&AreaID=501596&Prov=34',
	#Sumatera Selatan
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Baturaja&AreaID=501558&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Indralaya&AreaID=501559&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kayu%20Agung&AreaID=5002230&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lahat&AreaID=501561&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lubuk%20Linggau&AreaID=501562&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Martapura&AreaID=5002231&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Muara%20Enim&AreaID=501564&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Muaradua&AreaID=501565&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Musirawas&AreaID=501566&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pagar%20Alam&AreaID=501567&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palembang&AreaID=501568&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkalan%20Balai&AreaID=501569&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Prabumulih&AreaID=501570&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sekayu&AreaID=501571&Prov=33',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tebing%20Tinggi&AreaID=501618&Prov=33',
	#Sumatera Barat
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Arosuka&AreaID=501539&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Batusangkar&AreaID=501540&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bukittinggi&AreaID=501541&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lubuk%20Basung&AreaID=501542&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lubuk%20Sikaping&AreaID=501543&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Muaro%20Sijunjung&AreaID=501544&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Padang&AreaID=501545&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Padang%20Aro&AreaID=501546&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Padangpanjang&AreaID=501547&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Painan&AreaID=501548&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pariaman&AreaID=501549&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Parit%20Malintang&AreaID=501550&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Payakumbuh&AreaID=501551&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pulau%20Punjung&AreaID=501552&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sarilamak&AreaID=501553&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sawahlunto&AreaID=501554&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Simpang%20Empat&AreaID=501555&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Solok&AreaID=501556&Prov=32',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tuapejat&AreaID=501557&Prov=32',
	#Sulawesi Utara
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Air%20Madidi&AreaID=501530&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Amurang&AreaID=501531&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bitung&AreaID=501532&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Boroko&AreaID=1200110&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kotamobagu&AreaID=501615&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lolak&AreaID=501533&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Manado&AreaID=501534&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Melongguane&AreaID=501535&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ondong%20Siau&AreaID=501616&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ratahan&AreaID=501617&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tahuna&AreaID=501536&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tomohon&AreaID=1200111&Prov=31',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tondano&AreaID=501538&Prov=31',
	#Sulawesi Selatan
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bantaeng&AreaID=501488&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Barru&AreaID=501489&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Benteng&AreaID=501490&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bulukumba&AreaID=501491&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Enrekang&AreaID=501492&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jeneponto&AreaID=501493&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Makale&AreaID=501494&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Makassar&AreaID=501495&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Malili&AreaID=501496&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Maros&AreaID=501497&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Masamba&AreaID=501498&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palopo&AreaID=501499&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pangkajane&AreaID=501500&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pare%20Pare&AreaID=501501&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pinrang&AreaID=501502&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rantepao&AreaID=501503&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sengkang&AreaID=501504&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sidenreng&AreaID=501505&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sinjai&AreaID=501506&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sungguminasa&AreaID=501507&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Takalar&AreaID=501508&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Watampone&AreaID=501509&Prov=28',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Watan%20Soppeng&AreaID=501510&Prov=28',
	#Sulawesi Tengah
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ampana&AreaID=501520&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bungku&AreaID=501521&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Buol&AreaID=501522&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Donggala&AreaID=501523&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Luwuk&AreaID=501524&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Palu&AreaID=1200106&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Parigi&AreaID=501526&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Poso&AreaID=501527&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Salakan&AreaID=501528&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sigi%20Biromaru&AreaID=5002257&Prov=29',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Toli%20Toli&AreaID=501529&Prov=29',
	#Sulawesi Tenggara
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Andoolo&AreaID=501511&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bau%20Bau&AreaID=501512&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Buranga&AreaID=501612&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kendari&AreaID=501513&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kolaka&AreaID=501514&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lasusua&AreaID=501515&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pasar%20Wajo&AreaID=501516&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Raha&AreaID=501517&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Rumbia&AreaID=501518&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Unaaha&AreaID=501613&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wanggudu&AreaID=501614&Prov=30',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wangi%20Wangi&AreaID=501519&Prov=30',
	#Sulawesi Barat
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Majene&AreaID=501483&Prov=27',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mamasa&AreaID=501484&Prov=27',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mamuju&AreaID=501485&Prov=27',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Pasangkayu&AreaID=501486&Prov=27',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Polewali&AreaID=501487&Prov=27',
	'http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Topoyo&AreaID=1200113&Prov=27',
	#Maluku
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ambon&AreaID=501382&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bula&AreaID=501383&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Dobo&AreaID=501384&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kisar&AreaID=1200097&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Leksula&AreaID=1200094&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Masohi&AreaID=501385&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Namlea&AreaID=501386&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Piru&AreaID=501387&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Saumlaki&AreaID=501388&Prov=20',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tual&AreaID=501389&Prov=20',

	#Maluku Utara
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jailolo&AreaID=501390&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Labuha&AreaID=501391&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Maba&AreaID=501392&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Morotai&AreaID=5002255&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sanana&AreaID=501393&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sofifi&AreaID=5002253&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Taliabu&AreaID=5002254&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ternate&AreaID=501394&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tidore&AreaID=501604&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tobelo&AreaID=501395&Prov=21',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Weda&AreaID=501396&Prov=21',
	#Papua Barat
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Aimas&AreaID=501463&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bintuni&AreaID=501464&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Fak%20Fak&AreaID=501465&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kaimana&AreaID=501466&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kumurkek&AreaID=1200099&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Manokwari&AreaID=501467&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ransiki&AreaID=1200101&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Teminabuan&AreaID=501469&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Waisai&AreaID=501470&Prov=25',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wasior&AreaID=501471&Prov=25',
	#Papua
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Agats&AreaID=501443&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Biak&AreaID=501444&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Botawa&AreaID=501445&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Burmeso&AreaID=501611&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Enarotali&AreaID=501446&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Genyem&AreaID=5002259&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Jayapura&AreaID=501447&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Karubaga&AreaID=501448&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kepi&AreaID=501449&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Merauke&AreaID=501450&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mulia&AreaID=501451&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Nabire&AreaID=501452&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Oksibil&AreaID=501453&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sarmi&AreaID=501454&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sentani&AreaID=501455&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Serui&AreaID=501456&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sorendiweri&AreaID=501457&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sumohai&AreaID=501458&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Tanah%20Merah&AreaID=501459&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Timika&AreaID=501460&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Wamena&AreaID=501461&Prov=24',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Waris&AreaID=501462&Prov=24',
	#Nusa Tenggara Timur
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Atambua&AreaID=501427&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ba%20a&AreaID=501428&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Bajawa&AreaID=501429&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Betun&AreaID=5002265&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Borong&AreaID=501607&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ende&AreaID=501430&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kalabahi&AreaID=501431&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kefamenanu&AreaID=501432&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kefamenanu&AreaID=501432&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kupang&AreaID=501434&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Labuan%20Bajo&AreaID=501435&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Larantuka&AreaID=501436&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Lewoleba&AreaID=501437&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Maumere&AreaID=501438&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Mbay&AreaID=501608&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Oelamasi&AreaID=5002266&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Ruteng&AreaID=501439&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Sabu&AreaID=5002256&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Soe&AreaID=501440&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Waibakul&AreaID=501609&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Waikabubak&AreaID=501441&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Waingapu&AreaID=501442&Prov=23',
	'http://bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Weetabula&AreaID=501610&Prov=23'
	
]
# query the website and return the html to the variable 'page'
data = []

for pg in url:
	page = urllib2.urlopen(pg)
	# parse the html using beautiful soap and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')

	#get kode_prov
	start = pg.find('Prov=')+5
	kode_prov = pg[start:]

	def ACEH():
		global prov
		prov = 'Aceh'
	def BANTEN():
		global prov
		prov = 'Banten'
	def DKI():
		global prov
		prov = 'DKI Jakarta'
	def JABAR():
		global prov
		prov = 'Jawa Barat'
	def KALBAR():
		global prov
		prov = 'Kalimantan Barat'
	def KALTIM():
		global prov
		prov = 'Kalimantan Timur'
	def LAMPUNG():
		global prov
		prov = 'Lampung'
	def NTB():
		global prov
		prov = 'Nusa Tenggara Barat'
	def PABAR():
		global prov
		prov = 'Papua Barat'
	def SULSEL():
		global prov
		prov = 'Sulawesi Selatan'
	def SULTAR():
		global prov
		prov = 'Sulawesi Utara'
	def SUMUT():
		global prov
		prov = 'Sumatera Utara'
	def GORONTALO():
		global prov
		prov = "Gorontalo"
	def BALI():
		global prov
		prov = "Bali"
	def BENGKULU():
		global prov
		prov = 'Bengkulu'
	def JATENG():
		global prov
		prov = 'Jawa Tengah'
	def KALSEL():
		global prov
		prov = 'Kalimantan Selatan'
	def KALTUR():
		global prov
		prov = 'Kalimantan Utara'
	def MALUKU():
		global prov
		prov = 'Maluku'
	def NTT():
		global prov
		prov = 'Nusa Tenggara Timur'
	def RIAU():
		global prov
		prov = 'Riau'
	def SULTENG():
		global prov
		prov = 'Sulawesi Tengah'
	def SUMBAR():
		global prov
		prov = 'Sumatera Barat'
	def BABEL():
		global prov
		prov = 'Bangka Belitung'
	def DIY():
		global prov
		prov = 'DI Yogyakarta'
	def JAMBI():
		global prov
		prov = 'Jambi'
	def JATIM():
		global prov
		prov = 'Jawa Timur'
	def KALTENG():
		global prov
		prov = 'Kalimantan Tengah'
	def KEPRI():
		global prov
		prov = 'Kepulauan Riau'
	def MALKUR():
		global prov
		prov = 'Maluku Utara'
	def PAPUA():
		global prov
		prov = 'Papua'
	def SULBAR():
		global prov
		prov = 'Sulawesi Barat'
	def SULTAR():
		global prov
		prov = 'Sulawesi Tenggara'
	def SUMSEL():
		global prov
		prov = 'Sumatera Selatan'
	def errhandler ():
		print("Your input has not been recognised")

	get_kode = {
		"1": ACEH,
		"4": BANTEN,
		"7": DKI,
		"10": JABAR,
		"13": KALBAR,
		"16": KALTIM,
		"19": LAMPUNG,
		"22": NTB,
		"25": PABAR,
		"28": SULSEL,
		"31": SULTAR,
		"34": SUMUT,
		"8": GORONTALO,
		"2": BALI,
		"5": BENGKULU,
		"11": JATENG,
		"14": KALSEL,
		"17": KALTUR,
		"20": MALUKU,
		"23": NTT,
		"26": RIAU,
		"29": SULTENG,
		"32": SUMBAR,
		"3": BABEL,
		"6": DIY,
		"9": JAMBI,
		"12": JATIM,
		"15": KALTENG,
		"18": KEPRI,
		"21": MALKUR,
		"24": PAPUA,
		"27": SULBAR,
		"30": SULTENG,
		"33": SUMSEL
	}

	get_kode.get(kode_prov,errhandler)() #replace swicth

	

	# get kab_kota
	kab_kota = soup.find('h2', attrs={'class': 'blog-grid-title-lg'})
	kab_kotas = kab_kota.text.strip() # strip() is used to remove starting and trailing

	check = kab_kotas.find(' ')+1
	str_check = kab_kotas[check:]

	if str_check == '()':
		str_kab_kota = kab_kotas
	else:
		find_kab = kab_kotas.find('(')+1
		str_findKab = kab_kotas[find_kab:]
		str_replace = str_findKab.replace(')', '')
		#replace multiple string
		mapping = {'Kab. ':'','Kota ':'','Kodya ':'','Kep. ':'KEPULAUAN','Pahuwato':'PAHUWATO','Pangkajene Kep.':'PANGKAJENE DAN KEPULAUAN'}
		for k,v in mapping.iteritems():
			if k in str_replace: 
				change_str = str_replace.replace(k,v)
		#   #
		str_kab_kota = change_str

		#finding string Kab. or Kota
		if 'Kab.' in str_replace:
			ket = "Kab"
		elif 'Kota' in str_replace:
			ket = 'Kota'
		else:
			ket = '-'
	
	#get cuaca
	tab2 = soup.find('div', {'id':'TabPaneCuaca2'})
	get_cuaca = tab2.find_all("div",{"class":"kiri"})
	pagi = get_cuaca[0].text.strip()
	siang = get_cuaca[1].text.strip()
	malam = get_cuaca[2].text.strip()
	DiniHari = get_cuaca[3].text.strip()

	#check jenis hujan
	if pagi == 'Hujan Petir' or pagi == 'Hujan Lebat' or pagi == 'Hujan Sedang':
		cuacaPagi = 'Hujan'
	else:
		cuacaPagi = '-'

	if siang == 'Hujan Petir' or siang == 'Hujan Lebat' or siang == 'Hujan Sedang':
		cuacaSiang = 'Hujan'
	else:
		cuacaSiang = '-'

	if malam == 'Hujan Petir' or malam == 'Hujan Lebat' or malam == 'Hujan Sedang':
		cuacaMalam = 'Hujan'
	else:
		cuacaMalam = '-'

	if DiniHari == 'Hujan Petir' or DiniHari == 'Hujan Lebat' or DiniHari == 'Hujan Sedang':
		cuacaDiniHari = 'Hujan'
	else:
		cuacaDiniHari = '-'

	#genarate name file csv using date
	days = str(i.day+1)
	month = str(i.month)
	year = str(i.year)
	tanggal=days+"-"+month+"-"+year

	data.append((prov,str_kab_kota, cuacaPagi,cuacaSiang,cuacaMalam,cuacaDiniHari,ket)) #append data
#create file csv
with open("bmkg-"+tanggal+".csv", "a") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['Provinsi','kab_kota', 'pagi','siang','malam','DiniHari','Keterangan'])
	# The for loop
	#writer.writerow('kab_kota, pagi,siang,malam,DiniHari)
	for prov,str_kab_kota, cuacaPagi,cuacaSiang,cuacaMalam,cuacaDiniHari,ket in data:
		writer.writerow([prov,str_kab_kota, cuacaPagi,cuacaSiang,cuacaMalam,cuacaDiniHari,ket])
#   #