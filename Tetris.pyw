import sys , os , math , random
import pygame
from pygame. locals import *


#6._1 Susikuriam FPS kintamaji
FPS = 5

#17._1 Sukuriam ekrano parametrus
EKRANO_DYDIS = [400,600]

#20._1 Sukuriam pilka spalva
PILKA = (200,200,200)

#24._1 Sukuriam balta spalva
BALTA = (255,255,255)

# Zemelapio dydzio kintamieji
DYDIS_X = 12
DYDIS_Y = 20

# Bloko dydzio ilgis
BLOKO_ILGIS = 24

#34._1 Laukimo laiko kintamasis
LAUKIMO_LAIKAS = 0

# 48._1 susikuriam "tetra_pasirinkimo" kintamuosius
FIGURU_PASIRINKIMAI = (1,4)




# Kuriame specialia klase matomiems zaidimo objektams parodyti
class Blokas(pygame.sprite.Sprite):

    # Pradedame iprastai nuo '__init__' arba kitaip konstruktoriaus klases
    def __init__ (self, bloko_tipas, xy):

        # Kvieciame tevines klases (Sprite) konstruktoriu
        pygame.sprite.Sprite.__init__(self)

        # klases kintamuosius aprasysim su self, self.bloko_tipas bus paduotas bloko_tipas
        self.bloko_tipas = bloko_tipas
        

        # Musu visame zaidime vyraus 5 bloku tipai


        # Jeigu neaisku kodel naudojame "os.path.join"
        # http://www.pygame.org/docs/ref/image.html#pygame.image.load

        if bloko_tipas == 1: # uzkraunam blocku tipa
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_1.gif' ))
            
        elif bloko_tipas == 2:
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_2.gif' ))
            
        elif bloko_tipas == 3:    
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_3.gif' ))
            
        elif bloko_tipas == 4:
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_4.gif' ))
            
        elif bloko_tipas == 5:
            self.image = pygame.image.load( os.path.join( 'zaidimo_lauko_blokas.gif' ))

        # sukuriam nauja paveiksleli su tuo paciu pikseliu formatu kaip ir nuotrauka (tai darome kad isgautume greiciausia nuotraukos formata atvaizdavimui)
        self.image.convert()

        # '.get_rect' grazina keturkampi apimanti visa paduota pavirsiu, siuo atveju 'self.image'
        self.rect = self.image.get_rect() 

        # Tada musu keturkampio kaires ir virsaus koordinates bus paduoto tuple koordinates (xy - tai tuple)
        self.rect.left, self.rect.top = xy


    # Analogiskai padarysime kiekvieno zaidimo langelio tipo transformavimo funkcija
    def transformavimas(self, bloko_tipas):

        self.bloko_tipas = bloko_tipas

        if bloko_tipas == 1:            
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_1.gif' ))
        elif bloko_tipas  == 2:
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_2.gif' ))
        elif bloko_tipas == 3:    
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_3.gif' ))
        elif bloko_tipas == 4:
            self.image = pygame.image.load( os.path.join( 'figuros_blokas_4.gif' ))
        elif bloko_tipas == 5:
            self.image = pygame.image.load( os.path.join( 'zaidimo_lauko_blokas.gif' ))
           
        # sukuriam nauja paveiksleli su tuo paciu pikseliu formatu kaip ir nuotrauka (tai darome kad isgautume greiciausia nuotraukos formata atvaizdavimui) 
        self.image.convert()

        # Kadangi transformuojam tik zaidimo langelio tipa tai mums sitame metode daugiau nieko nebereikia

    
class Zaidimas(object):

    # Zaidimo klases __init__ 
    def __init__(self):
        
        # inicializuosim pygame modulius
        pygame.init()

        # incializuosim zaidimo langa (WINDOW), ekrano dydi susikursime virsuje klasiu
        self.langas = pygame.display.set_mode(EKRANO_DYDIS)

        # Treciame punkte arba 'leisti' metode reikia panaudoti 'self.laikrodis' (zaidimo laiko kintamaji) todel ji cia susikuriam
        self.laikrodis = pygame.time.Clock()


        # Musu fonas bus kurimas ekrano dydyje
        self.fonas = pygame.Surface(EKRANO_DYDIS)

        # Ir fona uzpildysim pilka spalva, kintamaji 'PILKA' susikursime virsuje klasiu
        self.fonas.fill(PILKA)

        ################################################################################################## -- SRIFTAI
        
        # kintamajam sriftai priskirsime lista, visu musu sistemoje galimu sriftu. Sriftu pavadinimai bus is mazuju raidziu su isimtais tarpais ir skyryba
        sriftai = pygame.font.get_fonts()

        # musu srfitas1 bus pasirinktas sriftas pagal kelia ['pygame.font.match_font' grazina pilna srifto kelia sistemoje] ir dydi
        self.sriftas1 = pygame.font.Font(pygame.font.match_font("Arial"), 18)

        #Musu rezultatas kintamaji (pradine reiksme 0)
        self.rezultatas = 0

        #Musu tekstas1 sudarytas is zodzio 'Rezultatas' ir kintamojo rezultatas
        self.tekstas1 = self.sriftas1.render('Rezultatas: %s'%self.rezultatas, True, BALTA)

        #Pasidarysime rect1 kintamaji ir turima tekstas1 kintamaji su rezultatu grazinsime kaip nauja keturkampi
        self.rect1 = self.tekstas1.get_rect()

        #Musu naujai sudaryto keturkampio centrines x ir y koordinates
        self.rect1.centerx = 200
        self.rect1.centery = 20

        # piesiame fone ,teksta keturkampio dydzio
        self.fonas.blit(self.tekstas1, self.rect1)
    
        # Piesiame fona, kairiajam virsutiniame kampe    
        self.langas.blit(self.fonas, (0,0))

        # Atnaujiname musu viso lango turini(visa langa)
        pygame.display.flip()


        # Si klase yra isvesta/pavledeta is pygame.sprite.Group(). Ji pratesia draw() metoda kuris seka pasikeitusias vietas ekrane.
        self.animacijos = pygame.sprite.RenderUpdates()

        
        self.animacijos_atnaujinimui = pygame.sprite.RenderUpdates()




    
        # 5. Ateiname is 5 punkto ir kad sukurtume zaidimo lauka
        
        #################################################
        #-----------------------------------------------#
        #       Kuriame bloko klase 
        #-----------------------------------------------#
        #################################################   
        
        # jau 5 pnkte mums prireikia zaidimo lauko, kuris sudarytas is kvadrateliu su 'Blokas' klases pagalba
        
        self.zaidimo_laukas = [[Blokas(5,(0,0)) for y in range (0,DYDIS_Y,1)] for x in range (0,DYDIS_X,1)]

        # Sukureme zaidimo_lauka, kurio kiekvienas kvadratelis tures penkta tipa ir bus sudarytas vien is 5 tipo kvadrateliu

        #print(self.zaidimo_laukas[0][0])
        #print(self.zaidimo_laukas[0][0].bloko_tipas)


        # Piesime is virsaus i apacia kas kiekviena stulpeli
        
        x_koordinate = 60 # pradine piesimo x koordinate
        
        for i in range (0,DYDIS_X,1): #ciklas eis nuo 0 iki musu zemelapio dydzio X

            x_koordinate += BLOKO_ILGIS #piesime kas kiekvieno bloko ilgi i X puse
            y_koordinate = 50 # pradine piesimo y koordinate
            
            for j in range(0,DYDIS_Y,1): #vidinis ciklas eis nuo 0 iki musu zemelapio dydzio Y
                
                self.zaidimo_laukas[i][j].rect.topleft = x_koordinate , y_koordinate

                self.zaidimo_laukas[i][j].indexes=i,j


                # I animacijas pridedam bet kokio tipo atnaujinimus, musu kvadratelis bus pridetas prie atnaujintu grupes
                self.animacijos.add(self.zaidimo_laukas[i][j])
                
                y_koordinate += BLOKO_ILGIS #piesime kas kiekvieno bloko ilgi i Y puse


        
        self.figura = [] # tures keturiu bloku informacija savyje


        
    # 7. Is septinto punkto ateiname cia ir kuriame funkcija kuri kontroliuos ivykius(pagal musu paspaustus mygtukus)
    def IvykiuReguliavimas(self):
        for ivykis in pygame.event.get():
            if ivykis.type == pygame.QUIT:
                return False
            # Jeigu esame paspaude bet koki mygtuka ir tik tuo atveju jei nauja figura yra sukurta, tada einame i salyga
            elif ivykis.type == pygame.KEYDOWN and self.figura:


            # 8.0 Susikuriame metoda "judintiFigura" nuo kurio priklausys musu figuros judejimas


                if ivykis.key == pygame.K_RIGHT:
                    # 8.1 jeigu musu nuspaustas mygtukas yra "desnysis" tai i metoda "judintiFigura" paduosime parametra "desinen"
                    self.judintiFigura("desinen")
                        
                elif ivykis.key == pygame.K_LEFT:
                    # 8.2 jeigu musu nuspaustas mygtukas yra "kairysis" tai i metoda "judintiFigura" paduosime parametra "kairen"
                     self.judintiFigura("kairen")

                elif ivykis.key == pygame.K_DOWN:
                    # 8.3 jeigu musu nuspaustas mygtukas yra "apacion" tai i metoda "judintiFigura" paduosime parametra "tiesiai_apacion"
                    self.judintiFigura("tiesiai_apacion")
                    
                elif ivykis.key == pygame.K_UP:
                    # 9. Susikuriam metoda "pasuktiTetra" kuris pasuktu musu figura i tam tikra puse
                    self.pasuktiTetra()
                    
                #  Nustatysime timer'i kokio veiksmo laukti ir kiek laukti (Susikursim LAIKO KINTAMAJI virs klasiu)       
                pygame.time.set_timer(pygame.KEYDOWN, LAUKIMO_LAIKAS)

        # Graziname True jei zaidimas nesustoja
        return True


    # 11. Ateiname is devinto punkto sukurti metodo, figuros bloku uzpaisymui/istrinimui
    def pasalintiBlokusApsukimui(self):
        "Paverciam duotus figuros listo blokus i 5, t.y zaidimo bloku tipa"
        self.zaidimo_laukas[self.figura[0][0]][self.figura[0][1]].transformavimas(5)
        self.zaidimo_laukas[self.figura[2][0]][self.figura[2][1]].transformavimas(5) 
        self.zaidimo_laukas[self.figura[3][0]][self.figura[3][1]].transformavimas(5)

        
    # 12. Ateiname taip pat is devinto punkto ir kuriame si metoda, kuris pavers blokus i reikiama tipa
    def transformuotiBlokusApsukimui(self, b_tipas):
        self.zaidimo_laukas[self.figura[0][0]][self.figura[0][1]].transformavimas(b_tipas)  ### --------------- PAZIURETI
        self.zaidimo_laukas[self.figura[2][0]][self.figura[2][1]].transformavimas(b_tipas)  ### --------------- PAZIURETI
        self.zaidimo_laukas[self.figura[3][0]][self.figura[3][1]].transformavimas(b_tipas)  ### --------------- PAZIURETI


    # 10. Is devinto punkto ateiname cia ir kuriame metoda "arUzpildyta" kuris grazins True arba False
    def arUzpildyta(self, blokas1, blokas2, blokas3):
        "Patikriname ar blokai yra uzpildyti ir ar indeksai yra neneigiami"

        # Paduodame 

        # cikle eisime per tris blokus, kuriuos suksime
        for i in (blokas1,blokas2,blokas3):
            
            # Jeigu bent vienas is triju tikrinamu bloku cikle yra uzpildytas ne penktu tipu ir jis taip pat nera dabartines figuros liste
            if self.zaidimo_laukas[i[0]][i[1]].bloko_tipas != 5 and i not in self.figura:

                # Kadangi zinome tipa, mums uztenka, kad salyga atitiktu bent blokas, t.y. kad jis butu uzpildytas

                # Jeigu blokas atitinka musu reikalavimus, graziname True
                return True

        # Jeigu bent vieno is pries tai tikrintu bloku tipas buvo 5 arba vienas is bloku jau buvo dabartines figuros liste
        for i in (blokas1,blokas2,blokas3):

            # Tokiu atveju tikrinsime ar musu bloku x'ai ir y'ai ir mazesni uz 0, t.y. ar jie vienas is ju nesusikures uz ribu
            if i[0]<0 or i[1]<0:
                
                return True
        return False
    

    # 9. Is devinto punkto ateiname cia ir kuriame apsukimo metoda
    def pasuktiTetra(self):

        # Naujas figuros tipas bus musu zemelapio_Lauko pirmo figuros keturkampio x ir y tipas
        b_tipas = self.zaidimo_laukas[self.figura[0][0]][self.figura[0][1]].bloko_tipas

        # Pirma atmesim salyga kai musu tikrinamasis tipas nera pirmas(nes pirmo nereikia apsukti, todel kad apsukta 2x2 figura vistiek liks 2x2 figura)
        if b_tipas != 1:

            # Ir tada tikrinsime visus likusius figuru tipus (t.y 2,3,4)
            if b_tipas == 2:


                # Jeigu musu figuros liste - pirmo(su 0 indeksu) kvadratelio y'as yra lygus su sekantcios(t.y. 2 arba su 1 indeksu) figuros y'u
                if self.figura[0][1]+1 == self.figura[1][1]:

                    
                    #sukdami mes visa laika suksime 0, 2 ir 3 indekso blokus, o 1 paliksime vietoje


                    # i metoda "arUzpildyta" paduodam skirtingas antro kvadratelio(su indeksu 1) x reiksmes, primenu x ir y koord indeksai 0 ir 1
                        # Bandom apsukti is stataus i gulscia
                    if not self.arUzpildyta([self.figura[1][0]-1,self.figura[1][1]],
                                          [self.figura[1][0]+1,self.figura[1][1]],
                                          [self.figura[1][0]+2,self.figura[1][1]]):
                        # Einame daryti metodo arUzpildyta

                        
                        # Ivykus salygai, tose vietose kur dabar yra figura, pasaliname blokus palikdami 1 su indeksu(1) kuriame "pasalintiBlokusApsukimui"                    
                        self.pasalintiBlokusApsukimui()



                        # Idedame i figuru lista naujas kvadrateliu koordinates is kuriu bus sudeliota/perpiesta naujoji figura
                        self.figura[0]=[self.figura[1][0]-1,self.figura[1][1]]
                        self.figura[2]=[self.figura[1][0]+1,self.figura[1][1]]
                        self.figura[3]=[self.figura[1][0]+2,self.figura[1][1]]

                        
                        # Kadangi istryneme/pakeiteme tipa triju kvadrateliu is figuros listo, todel dabar pakeisime i tipa naujose pozicjose esanciu kvadrateliu
                        # Kuriame "transformuotiBlokusApsukimui" ir paduodame dabartini tipa
                        self.transformuotiBlokusApsukimui(b_tipas)
                
                # Labai panasiai darysime su gulscia figura kai ja apsuksime i stacia
                else :
                    if not self.arUzpildyta([self.figura[1][0],self.figura[1][1]-1],
                                          [self.figura[1][0],self.figura[1][1]+1],
                                          [self.figura[1][0],self.figura[1][1]+2]):

                        # Apsukame
                        self.pasalintiBlokusApsukimui()
                        
                        # Keiciame pozicijas nauju kvadrateliu
                        self.figura[0]=[self.figura[1][0],self.figura[1][1]-1]
                        self.figura[2]=[self.figura[1][0],self.figura[1][1]+1]
                        self.figura[3]=[self.figura[1][0],self.figura[1][1]+2]
                        
                        # Transformuojame naujose pozicijose esancius kvadrateliu
                        self.transformuotiBlokusApsukimui(b_tipas)

            
            # 3 tipas 'T' raides formos figura pasukta i visas puses, tikrinsime keturis atvejus kaip sia figura galime pasukti, t.y kas 90 laipsniu   
            elif b_tipas == 3:


                # Nors ir bus keturi atvejai, tikrinimas tu atveju bus labai panasus


                # Pirma blokelis issikises i apacia (kaip 'T' raideje) ir viskas analogiskai
                if self.figura[0][0]+1 == self.figura[1][0]:
                    if not self.arUzpildyta([self.figura[1][0],self.figura[1][1]+1],
                                          [self.figura[1][0],self.figura[1][1]-1],
                                          [self.figura[1][0]+1,self.figura[1][1]]):
                        
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0],self.figura[1][1]+1]
                        self.figura[2]=[self.figura[1][0],self.figura[1][1]-1]
                        self.figura[3]=[self.figura[1][0]+1,self.figura[1][1]]
                        ##
                        self.transformuotiBlokusApsukimui(b_tipas)
                

                # Tada blokelis issikises i desine puse ( vizualiai |- ) ir viskas analogiskai
                elif self.figura[0][1]-1 == self.figura[1][1]:
                    if not self.arUzpildyta([self.figura[1][0]+1,self.figura[1][1]],
                                          [self.figura[1][0]-1,self.figura[1][1]],
                                          [self.figura[1][0],self.figura[1][1]-1]):
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0]+1,self.figura[1][1]]
                        self.figura[2]=[self.figura[1][0]-1,self.figura[1][1]]
                        self.figura[3]=[self.figura[1][0],self.figura[1][1]-1]
                        ##
                        self.transformuotiBlokusApsukimui(b_tipas)


                # Treciu atveju blokelis issikises i viruse ( aukstyn kojom parasyta 'T' ) ir viskas analogiskai                       
                elif self.figura[0][0]-1 == self.figura[1][0]:
                    if not self.arUzpildyta([self.figura[1][0],self.figura[1][1]-1],
                                          [self.figura[1][0],self.figura[1][1]+1],
                                          [self.figura[1][0]-1,self.figura[1][1]]):
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0],self.figura[1][1]-1]
                        self.figura[2]=[self.figura[1][0],self.figura[1][1]+1]
                        self.figura[3]=[self.figura[1][0]-1,self.figura[1][1]]
                        ##
                        self.transformuotiBlokusApsukimui(b_tipas)


                # Paskutiniu atveju blokelis issikises i desine puse (  vizualiai  -| ) ir viskas analogiskai   
                elif self.figura[0][1]+1==self.figura[1][1]:
                    if not self.arUzpildyta([self.figura[1][0]-1,self.figura[1][1]],
                                          [self.figura[1][0]+1,self.figura[1][1]],
                                          [self.figura[1][0],self.figura[1][1]+1]):
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0]-1,self.figura[1][1]]
                        self.figura[2]=[self.figura[1][0]+1,self.figura[1][1]]
                        self.figura[3]=[self.figura[1][0],self.figura[1][1]+1]
                        ##
                        self.transformuotiBlokusApsukimui(b_tipas)


            # Ketvirtas tipas fuguros S raide, du budai kuriuos tikrinsim , tiesiog ir pasukta S    
            elif b_tipas == 4:

                # Papratsa S ir viskas toliau analogiskai
                if self.figura[2][1]-1 == self.figura[1][1]:
                    if not self.arUzpildyta([self.figura[1][0]+1,self.figura[1][1]+1],
                                          [self.figura[1][0]+1,self.figura[1][1]],
                                          [self.figura[1][0],self.figura[1][1]-1]):
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0]+1,self.figura[1][1]+1]
                        self.figura[2]=[self.figura[1][0]+1,self.figura[1][1]]
                        self.figura[3]=[self.figura[1][0],self.figura[1][1]-1]
                        ##
                        self.transformuotiBlokusApsukimui(b_tipas)

                # Papratsa S ir viskas toliau analogiskai     
                elif self.figura[2][0]-1 == self.figura[1][0]:
                    if not self.arUzpildyta([self.figura[1][0]-1,self.figura[1][1]+1],
                                          [self.figura[1][0],self.figura[1][1]+1],
                                          [self.figura[1][0]+1,self.figura[1][1]]):
                        self.pasalintiBlokusApsukimui()
                        ##
                        self.figura[0]=[self.figura[1][0]-1,self.figura[1][1]+1]
                        self.figura[2]=[self.figura[1][0],self.figura[1][1]+1]
                        self.figura[3]=[self.figura[1][0]+1,self.figura[1][1]]
                        ##                 
                        self.transformuotiBlokusApsukimui(b_tipas)
                        

                
    def atnaujintiPiesima(self):

        for animacija in self.animacijos_atnaujinimui:
            animacija.update() #
   
        self.animacijos.draw(self.fonas)

        # piesiame fona ant lango
        self.langas.blit(self.fonas,(0,0))

        # atnaujiname visa vaizda
        pygame.display.flip() #

        

    # 5. Ateiname is penkto punkto cia kurti metoda, kuris sukurtu nauja figura
    def sukurtiDabartineFigura(self):
        "Jeigu bus imanoma sukurti norima figura metodas grazins -True-. Jeigu paciame virsuje musu zemelapio nebera vitos naujos figuros kurimui grazinama -False-"



        # 5.1 susikuriam dabartini tipa, kuris bus visiskai random sudarytas is RANDOM SKAICIU nuo 1 iki 4
        
        dabartinis_tipas = random.randint(FIGURU_PASIRINKIMAI[0],FIGURU_PASIRINKIMAI[1])
        # kur 1 bus 2x2 keturkampis, 2 bus 1x4 staciakampis , 3 bus aukstyn kojom parasyta 'T' formos figura, 4 bus 'S' formos figura


        ###########################################################################################################################################
        #-----------------------------------------------------------------------------------------------------------------------------------------#        
        # Prasides musu pagrindinio listo "self.figura" kurimas, kuris bus sudarytas is keturiu kvadrateliu poziciju atskiruose listuose
        #-----------------------------------------------------------------------------------------------------------------------------------------#         
        ###########################################################################################################################################


        # 5.2 Visu keturiu tipu atveju mes tikrinsime ar musu zaidimo_laukas kintamajam reikiamose pozicijose yra tuscios vietos
            # Pas mus tuscios vietos yra zymimos 5 tipu, nes musu visas zaidimo laukas yra sudarytas is 5 tipo kvadrateliu

        # Jeigu sugeneruotas tipas yra pirmas (1)
        
        if dabartinis_tipas == 1: # 2x2 keturkampis
            if (self.zaidimo_laukas[4][0].bloko_tipas == 5 and self.zaidimo_laukas[5][0].bloko_tipas == 5
                and self.zaidimo_laukas[4][1].bloko_tipas == 5 and self.zaidimo_laukas[5][1].bloko_tipas == 5):
                self.figura.append([4,0])
                self.figura.append([4,1])
                self.figura.append([5,0])
                self.figura.append([5,1])
            else:
                return False # jeigu nesukuriam figuros, grazinsim 'False'


        # Jeigu sugeneruotas tipas yra antras (2)
                
        elif dabartinis_tipas == 2:# 1x4 staciakampis
            if (self.zaidimo_laukas[4][0].bloko_tipas == 5 and self.zaidimo_laukas[4][2].bloko_tipas == 5
                and self.zaidimo_laukas[4][1].bloko_tipas == 5 and self.zaidimo_laukas[4][3].bloko_tipas == 5):
                self.figura.append([4,0])
                self.figura.append([4,1])
                self.figura.append([4,2])
                self.figura.append([4,3])
            else:
                return False # jeigu nesukuriam figuros, grazinsim 'False'

    
        # Jeigu sugeneruotas tipas yra trecias (3)
          
        elif dabartinis_tipas == 3:# aukstyn kojom parasyta 'T' formos figura
            if (self.zaidimo_laukas[4][0].bloko_tipas == 5 and self.zaidimo_laukas[5][0].bloko_tipas == 5
                and self.zaidimo_laukas[5][1].bloko_tipas == 5 and self.zaidimo_laukas[6][0].bloko_tipas == 5):
                self.figura.append([4,0])
                self.figura.append([5,0])
                self.figura.append([6,0])
                self.figura.append([5,1])
            else:
                return False # jeigu nesukuriam figuros, grazinsim 'False'


        # Jeigu sugeneruotas tipas yra ketvirtas (4)

        elif dabartinis_tipas == 4: # 'S' formos figura
            if (self.zaidimo_laukas[5][0].bloko_tipas == 5 and self.zaidimo_laukas[6][0].bloko_tipas == 5
                and self.zaidimo_laukas[4][1].bloko_tipas == 5 and self.zaidimo_laukas[5][1].bloko_tipas == 5):
                self.figura.append([4,1])
                self.figura.append([5,0])
                self.figura.append([5,1])
                self.figura.append([6,0])
            else:
                return False # jeigu nesukuriam figuros, grazinsim 'False'
        
        # Naujai sukurtoje figuroje pakeisime tipa is 5 i dabartini randomini 
        for indeksas in self.figura:
            self.zaidimo_laukas[indeksas[0]][indeksas[1]].transformavimas(dabartinis_tipas) # ir transformuojam paciame zaidimo lauke atitinkamus keturkampius
        return True # Galiausiai graziname -True- nes sukureme figura
        

    # 8. ateiname is astunto punkto ir kuriame si metoda, kuris musa figura perpies, zemyn/kairen/desinen     
    def judintiFigura(self, judejimas):

        # kuriames laikino figuros lista, kad patikrinus ar galima bus judinti figura tam tikra kryptimi, i si lista ta figura ir patalpintume
        laikina_figura = []
        try:
            # Paziurime ar nesame pralaimeje, nes jei esame, tai neturesime figuros ir negalesime susikurti tipo
            dabartinis_tipas = self.zaidimo_laukas[self.figura[0][0]][self.figura[0][1]].bloko_tipas
            
        except IndexError:
            # Tokiu atveju pass'insim praleisim funkcijos veikima
            pass
        
	# Jei sekmingai susikureme tipa tikriname i koks judejimas yra paduotas
        if judejimas == "zemyn":        
            for indeksas in self.figura:

                if indeksas[1] + 1 <= DYDIS_Y - 1:
                    
                    if self.zaidimo_laukas[indeksas[0]][indeksas[1]+1].bloko_tipas == 5 or [indeksas[0],indeksas[1]+1] in self.figura:
                        
                        laikina_figura.append([indeksas[0],indeksas[1]+1])                        
                    else:
                        self.figura = []
                        return False
                else:
                    self.figura = []
                    return False

        elif judejimas == "tiesiai_apacion":
            while True:
                if not self.judintiFigura("zemyn"):
                    break
                
        elif judejimas == "kairen":
            for indeksas in self.figura:
                if indeksas[0]-1 >= 0:
                    if self.zaidimo_laukas[indeksas[0]-1][indeksas[1]].bloko_tipas==5 or [indeksas[0]-1,indeksas[1]] in self.figura:
                        
                        laikina_figura.append([indeksas[0]-1,indeksas[1]])
                    else:
                        return False
                else:
                    return False
                
        elif judejimas == "desinen":
            for indeksas in self.figura:
                if indeksas[0]+1 <= DYDIS_X-1:
                    if self.zaidimo_laukas[indeksas[0]+1][indeksas[1]].bloko_tipas==5 or [indeksas[0]+1,indeksas[1]] in self.figura:
                        laikina_figura.append([indeksas[0]+1,indeksas[1]])        
                    else:
                        return False
                else:
                    return False



        for indeksas in self.figura:
            self.zaidimo_laukas[indeksas[0]][indeksas[1]].transformavimas(5)
            
        for indeksas in laikina_figura:
            self.zaidimo_laukas[indeksas[0]][indeksas[1]].transformavimas(dabartinis_tipas)
        self.figura = laikina_figura + []
        
	# Darome "atnaujintiPiesima() funkcija"
        self.atnaujintiPiesima()
        return True


# 55. Sukuriame funkcija "valytiLinijas"
    def valytiLinijas(self):
        
        arLinijaPilna = False
        for y in range (DYDIS_Y-1,-1,-1):
            # Jeigu linija pilna tai paziuresim ar po jos einanti tokia
            if arLinijaPilna:
                y+=1
            else:
                arLinijaPilna = True
                
            for x in range(0,DYDIS_X,1):
                if self.zaidimo_laukas[x][y].bloko_tipas == 5:
                    arLinijaPilna = False
                    break
                
            if arLinijaPilna:
                # Jeigu linija uzpildyta, tai einam nuo jus i virsu ir transformuojam z+1 i z linija
                for z in range (y-1,-1,-1):
                    for x in range(0,DYDIS_X,1):
                        self.zaidimo_laukas[x][z+1].transformavimas(self.zaidimo_laukas[x][z].bloko_tipas)

                # Tetrio virsutine linija pasidaro tuscia
                for x in range(0,DYDIS_X,1):
                        self.zaidimo_laukas[x][0].transformavimas(5)
                        
                self.rezultatas += 1
                self.tekstas1 = self.sriftas1.render('Rezultatas: %s'%self.rezultatas, 1, BALTA)
                self.fonas.fill(PILKA,self.rect1)
                self.fonas.blit(self.tekstas1, self.rect1)
                self.langas.blit(self.fonas, (0,0))
                
        self.atnaujintiPiesima()


    # 2. Darome metoda "leisti"

    def leisti(self):
        eina = True # susikuriam zaidimo veikimo kintamaji
        pralaimejo = False # susikuriam kintamaji pralaimejimui
        
        #3. Paleisim zaidimo cikla, zaidimas veiks kol 'eina' bus -True- ir pralaimejo -False-
        while eina and not pralaimejo:

            self.laikrodis.tick(FPS) #  self.laikrodis susikursime __init__ metode ir FPS kitamaji susikursime pradzioje(virs klasiu)


            # 4. Tesime zaidimo logika, kolkas listas "figura" yra tuscias, todel i sia salyga         
            if not self.figura:

                # 5. Musu metodas "sukurtiDabartineFigura()" grazins -True- jei sukurs figura, -False- jei nebera vietos musu zemelapio virsuje
                if not self.sukurtiDabartineFigura():
  
                    # I sitos salygos vidu ateiname, jeigu nebera vietos sukurti naujai figurai, tokiu atveju pralaimime


                    # Kintamajam "tekstas1" kuri taip pat sukursime __init__ priskiriame skrifta ir tai ka piesime
                    self.tekstas1 = self.sriftas1.render("Pralaimetojas. Rezultatas: %s"%self.rezultatas, 1, BALTA)

                    
                    # PIESIAME MUSU INTERFACE


                    # Fona uzpildome pilka spalva. Kintamaji 'PILKA' susikursime pradzioje(virs klasiu), o self.rect1 - nuo kur piesime susikursime __init__
                    self.fonas.fill(PILKA ,self.rect1)

                    # ant fono piesiame teksta 'self.tekstas1' parodys koki teksta piesime, 'self.rect1' parodys nuo kur piesime
                    self.fonas.blit(self.tekstas1, self.rect1)

                    # galiausiai ant musu sukurto zaidimo lango 'self.langas' kuri susikursime __init__ piesime fona
                    self.langas.blit(self.fonas, (0,0))

                    # ir kintamajam 'pralaimejo' priskirsime reiksme -True- nes nebegalime sukurti naujos figuros ir pralaimejome
                    pralaimejo = True

            
            # 6. Jei jau nauja figura yra sukurta einame i sita salyga       
            else:
                
                # 7. Kintamajam 'eina' priskiriame metodo 'IvykiuReguliavimas' reiksme, jei eina == False, musu zaidimo ciklas sustos
                eina = self.IvykiuReguliavimas()

                
		# KURSIME METODA "judintiFigura" paduodamas argumentas metodui - (pradine kryptis kur judes figura zaidimui prasidejus)
                self.judintiFigura("zemyn")


	    # jeigu ne figura tai darome funkcija "valytiLinijas"
            if not self.figura:
                self.valytiLinijas()
                
			# 56. Nustatom zaidimo pavadinima
            pygame.display.set_caption('TETRIS')


		# 57. Logika su pralaimejimu          
        while pralaimejo:
            pralaimejo = self.IvykiuReguliavimas()
        pygame.quit()
        sys.exit()

################################################################################
##################----------------------------------------######################
##################    PRADEDAME KURTI TETRI               ######################
##################----------------------------------------######################
################################################################################

# 1. Kaip iprasta, cia bus musu mainas is kurio kviesime zaidima

if __name__ == '__main__':
    zaidimas = Zaidimas() # sukuriame objekta, taip pat virsuje susikuriame klase 'Zaidimas'
    zaidimas.leisti() # paleidziame metoda / funkcija "leisti"
