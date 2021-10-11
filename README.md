 # Felhőszámítási rendszerek
>
> ***Államvizsgás tárgy!***
>

Ajánlott irodalom:

- [Matt Dorn: Preparing for the Certified OpenStack Administrator Exam, Packt, 2017](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam)
  - [coa-aio-newton.ova](https://github.com/PacktPublishing/Preparing-for-the-Certified-OpenStack-Administrator-Exam/blob/master/coa-aio-newton.ova) *fájlt letöltve fut a demo VM `openstack` a login és jelszó weben `admin` a login és jelszó*, belépés `eth0` címmel a böngészőben, vagy `ip add show eth0`
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
Glence api port `9292 TCP`-n hallgat. Minden usernek van egy adatbázisa, amivel kommunikál a `glence registry` komponens ami a `glence adatbázis`hoz kapcsolódik. Ebben az adatbázisban van az összes image neve, mérete, felhasználója, stb. Glence `api` a feltöltését kezeli, a `glence registry` a feltöltéseket tárolja, pl VM.

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

## EA3
### Felhő használatával szembeni aggályok:
> - másoknak adjuk át az adatainkat
> - nincs meg a kontroll
> - nem anonim
> - nem ingyenes
> - a bevezetéséhez sokmindnene kell változtatni
> - jobb szeretjük ami a miénk mint amit csak használatra kapunk
>
> ![there is no cloud just someone else's computer](https://i.redd.it/f4f4tcoo8wu21.png)
>
> - status quo kérdés a saját felhő
> - rengeteg plusz döntést kell meghozni, ohgy milyen szinten alkalmazzuk a felhőt
> - komoly pénzügyi kérdések sora

![](https://d3i71xaburhd42.cloudfront.net/f8d43395f5ead76fd1a7823c4c9b169ddf823fcf/4-Table1-1.png)

**data privacy:** az eus gdpr és az amerikai szabályoknak és a lokális szabályoknak is elget kell tegyen 

**monitoring:** Saját felhő monitorozása 

**network bottlenecks:** kicsi a sávszél de sok adatom van amit fel szeretnék tenni, ekkor fizikailag elszállítjuk az adathordozót és átadjuk a felhő szolgáltatónak.

| | |
| ------------- |:-------------:| 
| ![felhő1](https://www.computersciencezone.org/wp-content/uploads/2016/01/CloudFlavors.jpg) | ![felhő2](https://www.computersciencezone.org/wp-content/uploads/2015/04/cloud-computing.jpg)|

### Openstack alapok
> Iaas szinten nézve
> 
> ![reminder cloud structure](https://www.researchgate.net/publication/327284357/figure/fig1/AS:664938364280832@1535545068694/Figure-3-NIST-cloud-computing-definition-40.png)
>
> ![opnstack parts](https://www.techplayon.com/wp-content/uploads/2018/11/Open-Stack-Components.png)
> 
> ![openstack](https://static.packt-cdn.com/products/9781783986965/graphics/B01770_01_03.jpg)
>
> 1. Ahhoz, hogy létrehozzunk egy vmet, kell egy img fájl
> 2. nova megmondja, hogy mekkora mérettel hozzuk létrea VM-et
> 3. A külső hálózat eléréséhez a neutron segít
> 4. külső adat hozzárendelése ceilinderrel
> 5. A keystone authentikál mindent és adja a biztonsági réteget
> 6. a végfelhasználó egy horizonon keresztül fér hozzá
>  
> ![](https://www.researchgate.net/profile/Shilpa-Sonawani/publication/305297793/figure/fig1/AS:394201872257025@1470996458219/Loosely-coupled-architecture-of-OpenStack.png)

#### Keystone
- token alapú katalógus szolgáltatások http frontenden keresztül
- részletes beállításokat ad
- domainek létrehozása
  - lehet felhasználókat csoportokat projekteket defininálni
  - egy felhashnáló több projekthez férhet hozzá, de egyszerre csak egyet használhat
  - külső szerverrel is azonosíthatunk
  - mindenkinek saját egyedi UUIDja van
  - lehet user groupokat létrehozni amikre szabályokat alkalmazunk
  - kvótákat is beálíthatunk egy-egy projekthez
  - ![](https://s3.amazonaws.com/madorn.com/images/Screen%20Shot%202014-01-08%20at%201.58.09%20PM.png)
  - katalógus/végpont elérést állíthatunk be


### GY4 ~ NOVA
1. a user kér egy api hozzáférést
2. a nova conductor eltárolja
3. a nova scheduler létrehozza
4. a nova compute létrehozza a vm-et és a nova compute kezeli is azt indítás/leállítás/stb
5. rabbbitmq-server puffereli a kéréseket, és a komopőonenesek elévégzik amikor van rá szabad kapacitásuk.

- vmc proxy 
- az egyes fizikai gépeken ott van a nova compute,és az kezeli, hogy egy Hyper-V vagy vmware vagy bármi más jól működjön és elfedve legyen a felsőbb réteg elől

![nova copmute macro](https://access.redhat.com/webassets/avalon/d/Red_Hat_OpenStack_Platform-13-Instances_and_Images_Guide-en-US/images/1323ccc0b16e5c84f0964b52b2abe8a9/openstack-libvirt-images.png)![nova compute](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2uvhNH1UiYihr0AwbkPjDLThjTjPeiln-jyCTjfiXD0N0W5QAQkOftePkF370BE_K74k&usqp=CAU)

- VM törlése `Instaces`>`select all`>`delete`
- privátkulcsgenerálás: `ssh-keygen -b 2048 -t rsa -f cloud-key`

### GY5 ~ NEUTRON
https://docs.openstack.org/neutron/latest/
> A hálózati elérést valósítja meg openstacken belül. 
> 
> teljes SDN (*software defined network*) hálózatot valósít meg

![projectnetwork-phisicalnetwork](https://docs.openstack.org/neutron/latest/_images/NetworkTypes.png)![intenet-vm connection](https://docs.openstack.org/ocata/install-guide-ubuntu/_images/network2-overview.png)

- **NeutronDatabes** - itt tároljuk a network, stb specifikus információkat
- **neutronlinuxbradge-agent** - két virtualizált server közötti kommunikációt old meg az `A` virtuális gép és a `B` virtuális gép között az `A` fizikai gép fizikai interfésze és `B` fizikai gép fizikai interfésze közötti kapcsolatot oldja meg.
  - a **nova compute**tal együtt csinálja az egészet.
- **neutron-dhcp-agent** - ez osztja ki a VM-eknek az ip címeket.
- **neutron-l3-agent** - layer3mas szolgáltatásokat virtualizál
 
#### tűzfalazás
> VM instancen belül egy OS fut amin van egy tűzfal amit konfigurálhatunk, ez VM specifikus szigroításokat tesz lehetővé
> 
> Az openstacknek van külön tűzfala is, amivel akár csoportoknak adhatunk szabályokat, stb

1. create network
   a. ha *shared* akkor több projekkt között is megosztható 
3. subnet
4. 

## EA5
### Glace
![](https://www.oreilly.com/library/view/deploying-openstack/9781449311223/httpatomoreillycomsourceoreillyimages875415.png)
> **hogy hozhatunk létre imaget:**
> - openasack disk image builder
> - haricorp
> - VMware

> **image formátumok:**
> - ISO - ISO9660 : hagyom-nyos lemez laapú
> - VMDK - saját virtuális gép telepíttésekor vMware alatt
> - VHD-VHDX: hyperV virtualizált formátuma
> - RAW - nagy formátum, mindent tárol, sok üres helyet is

Architektúra:
> ![](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/b0ea275a-efab-4185-9c48-6109ceb2da94.jpg)

### Nova
> különböző hypervisorokkal múködik a nova hyper V, vmware, stb..
>
> ![](https://www.oreilly.com/library/view/deploying-openstack/9781449311223/httpatomoreillycomsourceoreillyimages875419.png)
> mindig a már foglalt sefrverre rakja, ha tudja

### Neutron
- Horizonon keresztül kezelhetjük
![](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/9cb27fc5-b634-4e7b-b1b6-efc68476674e.jpeg)
- neutron server bonyoslítja a kapcsolatot a fizikai és virtuális illetv virtuális-virtuális világ között
- dhcp: a szokásos
- l3: routerek
- bridge: szokásos hálózatis bridge

## GY6 - Cinder
> Digitális köteteket hozhatunk létre amiketblock storage szinte tudunk felmountolni.
>
> A compute nodeokban kicsia tároló kapacitás alapvetően, de vannak compute nodeok és strage nodeok is, és ezeket vonjuk össze. Ez az ***e**lastic **b**lock **s**otorage*. Ez jelenik meg *sdc* partició néven. Az I/O műveletek sebesssége kétséges.
> 
> ![storage network](http://platform9.com/wp-content/uploads/2015/12/Cinder-1-1-1024x559.png)
> 
> Ezzel a megoldással a compute nodeon is tárolunk mega storage nodeon is tárolunk adatot. A compute nodeon csak anynit amennyi épp szükséges

Mindne volumenak van egy azonosítója, mennyi adat tárolható, ki hozta létre, stb metaadatattal, A *cinder-scheduler* dönti el mennyi hely áll még rendelkezésünkre. A *cinder-volume* viszonty minden szerveren futni fog, ez ekrül be mindne VM-hez. A *cinder-backup*ban a vloumeokról készíthetünk backupot.

![](https://accelazh.github.io/images/cinder-architecture.png)

![](https://image.slidesharecdn.com/storagebasedonopenstackmariocho-160220082601/95/storage-based-onopenstackmariocho-23-638.jpg?cb=1455958139)![](https://wiki.openstack.org/w/images/thumb/b/bb/SharedLVMsupport.png/600px-SharedLVMsupport.png)

Cinderen belül tudunk 
- *volumeokat*: definiálni, ezek az egyes storage gépekhez tartozak, kb mint egy tradicionális harddrive. Ezeket felmountolhatjuk, vagy akár külön VMként is használhatjuk.
- *snapshot*: a VMről készítünk egy másolatot, technikailag ez is egy volume, de nincs felmountolva!
- *backup*: egy tömörített formátuma a volumenak.

```shell
sudo mkfs.ext3 dev/vdb
sudo mount dev/vdb mnt
```
