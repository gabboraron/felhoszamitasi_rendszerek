 # Felhőszámítási rendszerek
>
> ***Államvizsgás tárgy!***
>

Ajánlott irodalom:

- [Matt Dorn: Preparing for the Certified OpenStack Administrator Exam, Packt, 2017](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam)
  - [coa-aio-newton.ova](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam/blob/master/coa-aio-newton.ova) *fájlt letöltve fut a demo VM `openstack` a login és jelszó weben `admin` a login és jelszó*
- [Anne Gentle, Diane Fleming, Everett Toews, Joe Topjian, Jonathan Proulx, Lorin Hochstein, Tom Fifield: OpenStack Operations Guide. O`Reilly, 2014 (elektronikus jegyzet)](http://www.stilson.net/documentation/OpenStack%20Operations%20Guide.pdf)
- [Scott Adkins, John Belamaric, Vincent Giersch, Denys Makogon, Jason E. Robinson: OpenStack Cloud Application Development. Wiley, 2016 (elektronikus jegyzet)](https://allitbooks.net/download-file.html)


> **Beadandó:**
> 
> - **féléves feladat**ra 5 oldal dokumentáció, és érdemes a diplomamunkával összekötni és egy részét megvalósítani és azt leadni
> - 12. hét vasárnap éjjfél a határidő
> - prezentáció 5 perc
> - 5 oldalas doksi
> - 7. hét végig leadni
> 12. héten zh (szóbeli is lehet (8 perc ~ 1 téma) online oktatás esetén) offline esetén írásbeli
> 
> **Vizsga**
>
> vizsgáztatás ábrákkal, mutatni vagy akár felrajzolni
>

-------

## GY1

[OpenStack](https://www.openstack.org)el fogunk foglalkozni a félév során, mert az a legelterjedtebb.

*záróvizsgán érdemes környezetbe helyezni az openstacket ha az a tétel, OpenStack block diagram című dia a téma* ![OpenStack block diagram](https://www.researchgate.net/profile/Claus-Pahl/publication/319413970/figure/fig3/AS:563749434413056@1511419747357/An-OpenStack-block-diagram.png)

A háttérben egy Flask futtat Python kódokat igazából a legtöbb esetben.

## EA1
- 2008 -ban még nem tartották jelentősnek a felhőt (Richard Stallman)
- 2010 -ben márinnovatívnak tartották (Stevve Ballmer)
- 2011 -ben 112$ milliárd dollárra tette a következő 6 évre a felhő szempontjából a költségvetését az iparnak (Gartner) 

A felhő egy modell, on-demand alapú, konfigurálható számítási kapacitással, tárhelyel, szolgáltatásokkal

![felhők fajtái](https://www.researchgate.net/publication/241195178/figure/fig2/AS:400869486022664@1472586141957/NIST-Visual-Model-of-Cloud-Computing-a-Service-Models-Cloud-computing-can-be-classified.png)

- felskálázás (rapid elasticity): mikor szabadon vltoztatjuk a 
- kiskálázás (horizontális skálázás): mikor ugyanolyan technológiából használok többet.

### szolgáltatási modellek:
- IaaS (Infrastructure as a Service) pl a virtualizálás maga, VMware
- PaaS (platform as a Service) Cuda, itt a szolgáltatás maga érhető el
- SaaS (Software as a Service) szoftvevrkezelő tudásra van szükség, pl GDrive, Dropbox, Netflix

![pizza analógia](https://miro.medium.com/max/1400/1*peN3l27025YUoY0FEqllVA.jpeg)

- on-promise rendszereknek vannak előnyei, olcsóbb elhet, ha sokat és nagy hozzáértéssel használjuk (pl ha van jó csapatunk aki megcsinálja)
- ha viszont nekem az időm drágább akkor SaaS jobb

https://www.optimizely.com/insights/blog/pizza-as-a-service/

## GY2

belépés `eth0` címmel a b​öngészőben

## GY2
### Keystone

A keystoneban lévő `user`hez lehet jogosultságokat rendelni, tehát az abba való authentikációt nem az kezeli.

Az openstacken létrehozott domainek között nincs átláthatóság
A domaineken belül hozunk létre projekteket amikhez hozzárendelünk erőforrásokat. Ezekhez a projektekhez rendelhetünk usereket.


| | |
| ------------- |:-------------:| 
| Az openstacken létrehozott domainek között nincs átláthatóság | ![projekt alfelosztás](https://s3.amazonaws.com/madorn.com/images/ss.png)|
| A domaineken belül hozunk létre projekteket amikhez hozzárendelünk erőforrásokat. Ezekhez a projektekhez rendelhetünk usereket.| ![domain-projekt kapcsolat](https://s3.amazonaws.com/madorn.com/images/Screen%20Shot%202014-01-08%20at%201.04.26%20PM.png)|
| Az openstacken létrehozott domainek között nincs átláthatóság | ![projekt alfelosztás](https://s3.amazonaws.com/madorn.com/images/ss.png)| |

A felhasználókhoz szerepeket köthetünk.

beSSHzunk Puttyal `openstack@ip`.


1 vCPU mellé 2gb RAM
egy gép min 2 vCPU - 4gb RAM

hard limit az, hogy gey copmute serveren milyen gépet hozunk létre!

#### konfiguráció webes guin át
> a gui csak az adott ipn található openstackel tud kommunikálni
`Project` > `instances` itt látszanak a gépek
`Project` > `Ovierview` itt a megadott hardware megk​tések látszanak
`Identity` > `Projects` létrehozott projektek és azokhoz tartozó allokált hardware k​​vetelmények

#### konfiguráció parancssoron át
> a parancssori kliens bármely openstacket tudja kezelni

`openstack` parancs, jelszó `openstack`
- `source`
- `openrc`

mindig copy az eredeti settings fájlt és azt módosítsuk!
