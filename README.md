 # Felhőszámítási rendszerek
>
> ***Államvizsgás tárgy!***
>

Ajánlott irodalom:

- [Matt Dorn: Preparing for the Certified OpenStack Administrator Exam, Packt, 2017](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam)
  - [coa-aio-newton.ova](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam/blob/master/coa-aio-newton.ova) *fájlt letöltve fut a demo VM `openstack` a login és jelszó weben `admin` a login és jelszó*, belépés `eth0` címmel a böngészőben
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

# EA2
![cloud reference model i](https://www.researchgate.net/profile/Abbas_Strommen-Bakhtiar/publication/278657825/figure/fig7/AS:790968647299072@1565593029417/IaaS-vs-PaaS-vs-SaaS-Source-Kates-Comments-2010-4.png)


> ### Privát felhő:
> 
> Egy szervezet férhet hozzá a felhőhöz, de annak helye nem feltétlen a szervezetnél van, ki lehet szervezve akár! A felhő akár adott projekthez van konfigurálva ilyen esetben.

> ### Közösségi felhő
> 
> Szintén csak a szervezetférhet hozzá, de szintén nem feltétlen van helyileg a szervezetnél, de olyannak van felkonfigurálva ami pont a szervezet ígényeit elégíti ki.


> ### Publikus felhő
> 
> Bárki hozzáférhet, kivéve akiknek nem engedjük (Irán, tálibok, stb)


> ### Hibrid felhő
> - Publikus és Privát felhők kapcsolata hálózatba rendezve.
> - Az adatok/alkalmazások eloszlanak a különböző felhők között.
>
> ![hybrid cloud](https://nttdata-solutions.com/wp-content/usermedia/blog-what-is-a-hybrid-cloud-infographic.png)

![felhők használatának tipikus mintái](https://labs.eleks.com/wp-content/uploads/2012/12/cc-patterns.png)

> ### Predictable bursting
> Egy híroldal terheltsége más órákban nő meg mint egy könyvelő szerveré, tehát a felhő mögötte az képes egyneletesen "leterhelődni".

## Felhő felhasználás előnyei
- alacsony költség, merta szolgáltatóknak megvan a technológiája hozzá, sok felhasználóval
- Könnyű felhasználhatóság: hamar elérhetőek licenszes termékek akár
- Guality of service: 99,999% hogy egy s3as trolón nincs adatvesztés.
- megbízhatóság
- kiszervezett IT menedzsment:it szzolgáltatások kiszervezése olcsóbb mint saját it állományt fenntartani.
- simplified mantenece and upgrade: könnyen és gyorsan elérhetőek a frissítések.
- nagyon olcsón lehet hozzákezdeni

## Felhőt szolgáltatni miért jó
- profit
- optimalizálás: egyébként kihasználatlanul álló gépeket megnyitunk publikusnak
- stratégia: fenchise védelem, windows  azure
- kiszervezés: IBM-hez kiszervezi a számítást, könyvelést
- brand szempontjából terület megjelölés: Google app engine
- platform: kapcsolat a vevőkkel: salesforce.com force.com  

## GY3
### Glence
Amikor kérünk egy gépet a felhőben akkor annak általában nincs operációs rendszere vagy ha van nem olyan mint szeretnénk, ezért érdemes olyant telepíteni amit szeetnénk telepíteni.
Telepíthetjük az [ubuntu cloud image](http://cloud-images.ubuntu.com/releases/focal/release/) innen a `kvm` szót tartalmazót ha telepítjük, mert ha virtualboxosat telepítünk akkor a `.ova` fájl kell. [Debian](http://cloud.debian.org/images/cloud/)ra is létezik felhős image.

> #### Hogy tudunk a felhasználónak előre elkészítnei egy ubuntut pl dockerrel:
> 1. leteöltjük a vmet, azt futtatjuk, majd azon belül tlepítjük a dockert és az így keletkezett vm-et leállítjuk és feltöltjük.
> 2. [openstack disk image builder](https://docs.openstack.org/diskimage-builder/latest/) projektét használva, de csak openstacken működik, szóval AWSre pl nem alkalmas.
> 3. [hashicorp packer](https://www.packer.io/) ugyanaz mint az openstackes csak nem felhő függő, használható bármilyen felhőhöz. Azért előnyös mert könnyen lehet frissítéseket bepipeolni a felhőbe a különböző imagek frissítéséhez pl.
> 4. [oracle virtualbox](https://www.virtualbox.org/)

> #### image formátumok:
>  - **QCOW2:** tömöríti az imaget, és növeli addig amíg eléri amximum beállított értéket, tehát ha 10gb a max és 1gb van használva akkor 1gb-t foglal fizikailag, de erőforrás ígényes az egész
> - **RAW:** mindent tárol, 10gb-ra foglaltat 10gbra foglala akkor is ha 1gb van benne, de nem erőforrás ígényes.
> - **VHD és VHDK:** Hyper-V és azure kedvenc formátuma.

#### Glence architektúra
Glence api port `9292 TCP`-n hallgat. Minden usernek van egy adatbázisa, amivel kommunikál a `glence registry` komponens ami a glence adatbázis`hoz kapcsolódik. Ebben az adatbázisban van az összes image neve, mérete, felhasználója, stb. Glence `api` a feltöltését kezeli, a `glence registry` a feltöltéseket tárolja, pl VM.

![glence struktúra](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/b0ea275a-efab-4185-9c48-6109ceb2da94.jpg)

##### Új virtuális gép a UI-n keresztül:
1. letöltjük az imaget
2. `Images` > `Create Image`
   - megadjuk a nevét
   - a leírását
   - feltöltjük az image fájlt.
   - megadjuk a formátumát *(pl QCOW2)*
   - megadjuk az architektúráját *(pl: x82/64)*
   - next: további metainformációk, *pl: hyperviser, pythonverzó, stb*
3. frissjtjük az oldalt és megjelenik az imagek között az új.




