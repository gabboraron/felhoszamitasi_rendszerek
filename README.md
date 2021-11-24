 # Felhőszámítási rendszerek
>
> ***Államvizsgás tárgy!***
>

**Ajánlott irodalom:**
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
- **IaaS** *(Infrastructure as a Service)* pl a virtualizálás maga, VMware
- **PaaS** *(Platform as a Service)* Cuda, itt a szolgáltatás maga érhető el
- **SaaS** *(Software as a Service)* szoftvevrkezelő tudásra van szükség, pl GDrive, Dropbox, Netflix

![pizza analógia](https://miro.medium.com/max/1400/1*peN3l27025YUoY0FEqllVA.jpeg)

- on-promise rendszereknek vannak előnyei, olcsóbb lehet, ha sokat és nagy hozzáértéssel használjuk (pl ha van jó csapatunk aki megcsinálja)
- ha viszont nekem az időm drágább akkor SaaS jobb

[Pizza as a Service analogy: On Prem, IaaS, PaaS & SaaS](https://www.optimizely.com/insights/blog/pizza-as-a-service/)

## GY2
### Keystone
> A keystoneban lévő `user`hez lehet jogosultságokat rendelni, tehát az abba való authentikációt nem az kezeli.
>
> Az openstacken létrehozott domainek között nincs átláthatóság
> A domaineken belül hozunk létre projekteket amikhez hozzárendelünk erőforrásokat. Ezekhez a projektekhez rendelhetünk usereket.

| | |
| ------------- |:-------------:| 
| Az openstacken létrehozott domainek között nincs átláthatóság | ![projekt alfelosztás](https://s3.amazonaws.com/madorn.com/images/ss.png)|
| A domaineken belül hozunk létre projekteket amikhez hozzárendelünk erőforrásokat. Ezekhez a projektekhez rendelhetünk usereket.| ![domain-projekt kapcsolat](https://s3.amazonaws.com/madorn.com/images/Screen%20Shot%202014-01-08%20at%201.04.26%20PM.png)|

> A felhasználókhoz szerepeket köthetünk.
> 
> beSSHzunk Puttyal `openstack@ip`.
>
> - 1 vCPU mellé 2gb RAM
> - egy gép min 2 vCPU - 4gb RAM
>
> **hard limit** az, hogy egy copmute serveren milyen gépet hozunk létre!

#### konfiguráció webes guin át
> a gui csak az adott `ip`n található openstackel tud kommunikálni
> 
> - `Project` > `instances` itt látszanak a gépek
> - `Project` > `Ovierview` itt a megadott hardware megk​tések látszanak
> - `Identity` > `Projects` létrehozott projektek és azokhoz tartozó allokált hardware k​​vetelmények

#### konfiguráció parancssoron át
> a parancssori kliens bármely openstacket tudja kezelni
>
> - `openstack` parancs, jelszó `openstack`
> - `source`
> - `openrc`
> 
> *mindig `copy` az eredeti settings fájlt és azt módosítsuk!*

# EA2
![cloud reference model i](https://www.researchgate.net/profile/Abbas_Strommen-Bakhtiar/publication/278657825/figure/fig7/AS:790968647299072@1565593029417/IaaS-vs-PaaS-vs-SaaS-Source-Kates-Comments-2010-4.png)


> ### Privát felhő:
> 
> Egy szervezet férhet hozzá a felhőhöz, de annak helye nem feltétlen a szervezetnél van, ki lehet szervezve akár! A felhő akár adott projekthez van konfigurálva ilyen esetben.

> ### Közösségi felhő
> 
> Szintén csak a szervezet férhet hozzá, de szintén nem feltétlen van helyileg a szervezetnél, de olyannak van felkonfigurálva ami pont a szervezet ígényeit elégíti ki.


> ### Publikus felhő
> 
> Bárki hozzáférhet, kivéve akiknek nem engedjük (Irán, tálibok, stb)


> ### Hibrid felhő
> - Publikus és Privát felhők kapcsolata hálózatba rendezve.
> - Az adatok/alkalmazások eloszlanak a különböző felhők között.
>
> ![hybrid cloud](https://nttdata-solutions.com/wp-content/usermedia/blog-what-is-a-hybrid-cloud-infographic.png)



> ### Felhők terhelése
> | _**Predictable bursting:**_ Egy híroldal terheltsége más órákban nő meg mint egy könyvelő szerveré, tehát a felhő mögötte az képes egyneletesen *"leterhelődni"*. | ![felhők használatának tipikus mintái](https://labs.eleks.com/wp-content/uploads/2012/12/cc-patterns.png) |
> | ------------- |:-------------:| 

## Felhő felhasználás előnyei
- **alacsony költség**, mert a szolgáltatóknak megvan a technológiája hozzá, sok felhasználóval
- **Könnyű felhasználhatóság:** hamar elérhetőek licenszes termékek akár
- **Quality of service:** 99,999% hogy egy S3-as tárolón nincs adatvesztés.
- **megbízhatóság**
- **kiszervezett IT menedzsment**: it szzolgáltatások kiszervezése olcsóbb mint saját it állományt fenntartani.
- **simplified maintenance and upgrade**: könnyen és gyorsan elérhetőek a frissítések.
- **nagyon olcsó**n lehet hozzákezdeni

## Felhőt szolgáltatni miért jó
- **profit**
- **optimalizálás**: egyébként kihasználatlanul álló gépeket megnyitunk publikusnak
- **stratégia**: franchise védelem, windows  azure
- **kiszervezés**: IBM-hez kiszervezi a számítást, könyvelést
- **brand szempontjából terület megjelölés**: Google app engine
- **platform**: Ha egyébként is szükség lenne hasonló eszközre
- **kapcsolat a vevőkkel**: salesforce.com force.com  

## GY3
### Glence
Amikor kérünk egy gépet a felhőben akkor annak általában nincs operációs rendszere vagy ha van nem olyan mint szeretnénk, ezért érdemes olyant telepíteni amit szeretnénk telepíteni.
Telepíthetjük az [ubuntu cloud image](http://cloud-images.ubuntu.com/releases/focal/release/) innen a `kvm` szót tartalmazót ha telepítjük, mert ha virtualboxosat telepítünk akkor a `.ova` fájl kell. [Debian](http://cloud.debian.org/images/cloud/)ra is létezik felhős image.

> #### Hogy tudunk a felhasználónak előre elkészítnei egy ubuntut pl dockerrel:
> 1. letöltjük a VMet, azt futtatjuk, majd azon belül telepítjük a dockert és az így keletkezett VM-et leállítjuk és feltöltjük.
> 2. [openstack disk image builder](https://docs.openstack.org/diskimage-builder/latest/) projektét használva, de csak openstacken működik, szóval AWSre pl nem alkalmas.
> 3. [hashicorp packer](https://www.packer.io/) ugyanaz mint az openstackes csak nem felhő függő, használható bármilyen felhőhöz. Azért előnyös mert könnyen lehet frissítéseket bepipeolni a felhőbe a különböző imagek frissítéséhez pl.
> 4. [oracle virtualbox](https://www.virtualbox.org/)

> #### image formátumok:
>  - **QCOW2:** tömöríti az imaget, és növeli addig amíg eléri amximum beállított értéket, tehát ha 10Gb a max és 1Gb van használva akkor 1Gb-t foglal fizikailag, de erőforrás ígényes az egész
> - **RAW:** mindent tárol, 10Gb-ra foglaltat 10Gb-ra foglal akkor is ha 1Gb van benne, de nem erőforrás ígényes.
> - **VHD és VHDK:** Hyper-V és Azure kedvenc formátuma.

#### Glance architektúra
> Glance api port `9292 TCP`-n hallgatózik. Minden usernek van egy adatbázisa, amivel kommunikál a `glence registry` komponens ami a `glence adatbázis`hoz kapcsolódik. Ebben az adatbázisban van az összes image neve, mérete, felhasználója, stb. Glance `api` a feltöltését kezeli, a `glence registry` a feltöltéseket tárolja, pl VM.
>
> ![glance struktúra](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/b0ea275a-efab-4185-9c48-6109ceb2da94.jpg)

##### Új virtuális gép a UI-n keresztül:
1. letöltjük az imaget
2. `Images` > `Create Image`
   - megadjuk a nevét
   - a leírását
   - feltöltjük az image fájlt.
   - megadjuk a formátumát *(pl QCOW2)*
   - megadjuk az architektúráját *(pl: x82/64)*
   - next: további metainformációk, *pl: hypervisor, python verzó, stb*
3. frissítjük az oldalt és megjelenik az imagek között az új.

# EA3
## Felhő használatával szembeni aggályok:
> - másoknak adjuk át az adatainkat
> - nincs meg a kontroll
> - nem anonim
> - nem ingyenes
> - a bevezetéséhez sokmindenen kell változtatni
> - jobb szeretjük ami a miénk mint amit csak használatra kapunk
>
> ![there is no cloud just someone else's computer](https://i.redd.it/f4f4tcoo8wu21.png)
>
> - status quo kérdés a saját felhő
> - rengeteg plusz döntést kell meghozni, hogy milyen szinten alkalmazzuk a felhőt
> - komoly pénzügyi kérdések sora

![](https://d3i71xaburhd42.cloudfront.net/f8d43395f5ead76fd1a7823c4c9b169ddf823fcf/4-Table1-1.png)

**data privacy:** az eus GDPR és az amerikai szabályoknak és a lokális szabályoknak is eleget kell tegyen 

**monitoring:** Saját felhő monitorozása 

**network bottlenecks:** kicsi a sávszél de sok adatom van amit fel szeretnék tenni, ekkor fizikailag elszállítjuk az adathordozót és átadjuk a felhő szolgáltatónak.

| ![felhő1](https://www.computersciencezone.org/wp-content/uploads/2016/01/CloudFlavors.jpg) | ![felhő2](https://www.computersciencezone.org/wp-content/uploads/2015/04/cloud-computing.jpg)|
| ------------- |:-------------:| 

## Openstack alapok
> IaaS szinten nézve
> 
> ![reminder cloud structure](https://www.researchgate.net/publication/327284357/figure/fig1/AS:664938364280832@1535545068694/Figure-3-NIST-cloud-computing-definition-40.png)
> 
> | ![opnstack parts](https://www.techplayon.com/wp-content/uploads/2018/11/Open-Stack-Components.png) | ![openstack](https://static.packt-cdn.com/products/9781783986965/graphics/B01770_01_03.jpg) |
> | ------------- |:-------------:| 
> 
> 1. Ahhoz, hogy létrehozzunk egy VMet, kell egy `.img` fájl
> 2. A `nova` megmondja, hogy mekkora mérettel hozzuk létre a VM-et
> 3. A külső hálózat eléréséhez a `neutron` segít
> 4. külső adat hozzárendelése `cinder`rel
> 5. A `keystone` authentikál mindent és adja a biztonsági réteget
> 6. a végfelhasználó a `horizon`on keresztül fér hozzá
>  
> ![](https://www.researchgate.net/profile/Shilpa-Sonawani/publication/305297793/figure/fig1/AS:394201872257025@1470996458219/Loosely-coupled-architecture-of-OpenStack.png)

### Keystone
> - token alapú katalógus szolgáltatások http frontenden keresztül
> - részletes beállításokat ad
> - domainek létrehozása
>   - lehet felhasználókat csoportokat projekteket defininálni
>   - egy felhashnáló több projekthez férhet hozzá, de egyszerre csak egyet használhat
>   - külső szerverrel is azonosíthatunk
>   - mindenkinek saját egyedi UUIDja van
> - lehet `user group`okat létrehozni amikre szabályokat alkalmazunk
> - kvótákat is beálíthatunk egy-egy projekthez
> - katalógus/végpont elérést állíthatunk be
> ![](https://s3.amazonaws.com/madorn.com/images/Screen%20Shot%202014-01-08%20at%201.58.09%20PM.png)

# GY4 ~ NOVA
1. a user kér egy api hozzáférést
2. a `nova conductor` eltárolja
3. a `nova scheduler` létrehozza
4. a `nova compute` létrehozza a VM-et és kezeli is azt indítás/leállítás/stb
5. `rabbbitmq-server` puffereli a kéréseket, és a komoponenesek elévégzik amikor van rá szabad kapacitásuk.

- vmc proxy 
- az egyes fizikai gépeken ott van a `nova compute`, és az kezeli, hogy egy Hyper-V vagy VMware vagy bármi más jól működjön és elfedve legyen a felsőbb réteg elől

| ![nova copmute macro](https://access.redhat.com/webassets/avalon/d/Red_Hat_OpenStack_Platform-13-Instances_and_Images_Guide-en-US/images/1323ccc0b16e5c84f0964b52b2abe8a9/openstack-libvirt-images.png) | ![nova compute](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2uvhNH1UiYihr0AwbkPjDLThjTjPeiln-jyCTjfiXD0N0W5QAQkOftePkF370BE_K74k&usqp=CAU) |
|:---:|:---:|

- VM törlése `Instaces`>`select all`>`delete`
- privátkulcsgenerálás: `ssh-keygen -b 2048 -t rsa -f cloud-key`

# GY5 ~ NEUTRON
https://docs.openstack.org/neutron/latest/
> **A hálózati elérést valósítja meg openstacken belül.**
> 
> teljes SDN (*software defined network*) hálózatot valósít meg

![projectnetwork-phisicalnetwork](https://docs.openstack.org/neutron/latest/_images/NetworkTypes.png)![intenet-vm connection](https://docs.openstack.org/ocata/install-guide-ubuntu/_images/network2-overview.png)

- **NeutronDatabes** - itt tároljuk a network, stb specifikus információkat
- **neutronlinuxbradge-agent** - két virtualizált server közötti kommunikációt old meg az `A` virtuális gép és a `B` virtuális gép között az `A` fizikai gép fizikai interfésze és `B` fizikai gép fizikai interfésze közötti kapcsolatot oldja meg.
  - a **nova compute**tal együtt csinálja az egészet.
- **neutron-dhcp-agent** - ez osztja ki a VM-eknek az ip címeket.
- **neutron-l3-agent** - layer3mas szolgáltatásokat virtualizál
 
## tűzfalazás
> - VM instancen belül egy OS fut amin van egy tűzfal amit konfigurálhatunk, ez VM specifikus szigroításokat tesz lehetővé
> - Az openstacknek van külön tűzfala is, amivel akár csoportoknak adhatunk szabályokat, stb
>
> 1. create network
>    a. ha *shared* akkor több projekt között is megosztható 
> 3. subnet 

# EA5 - Glance / Nova / Neutron
## Glance
> ![](https://www.oreilly.com/library/view/deploying-openstack/9781449311223/httpatomoreillycomsourceoreillyimages875415.png)
> 
> **hogy hozhatunk létre imaget:**
> - openasack disk image builder
> - haricorp
> - VMware
>
> **image formátumok:**
> - `ISO` - `ISO9660`: hagyományos lemez alapú
> - `VMDK` - saját virtuális gép telepítésekor VMware alatt
> - `VHD` - `VHDX`: HyperV virtualizált formátuma
> - `RAW` - nagy formátum, mindent tárol, sok üres helyet is
>
> **Architektúra:**
> ![](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/b0ea275a-efab-4185-9c48-6109ceb2da94.jpg)

## Nova
> - különböző hypervisorokkal múködik a nova `HyperV`, `VMware`, stb..
> - mindig a már foglalt serverre rakja, ha tudja
> 
> ![](https://www.oreilly.com/library/view/deploying-openstack/9781449311223/httpatomoreillycomsourceoreillyimages875419.png)


## Neutron
> ![](https://www.oreilly.com/library/view/preparing-for-the/9781787288416/assets/9cb27fc5-b634-4e7b-b1b6-efc68476674e.jpeg)
> 
> - Horizonon keresztül kezelhetjük
> - neutron server bonyoslítja a kapcsolatot a fizikai és virtuális illetv virtuális-virtuális világ között
> - dhcp: a szokásos
> - l3: routerek
> - bridge: szokásos hálózatis bridge

# GY6 - Cinder
> Digitális köteteket hozhatunk létre amiket `block storage` szinten tudunk felmountolni.
>
> A `compute node`okban kicsi a tároló kapacitás alapvetően, de vannak compute nodeok és strage nodeok is, és ezeket vonjuk össze. Ez az ***e**lastic **b**lock **s**otorage*. Ez jelenik meg *sbc* partició néven. Az I/O műveletek sebessége kétséges.
> 
> Ezzel a megoldással a `compute node`on is tárolunk és a `storage node`on is tárolunk adatot. A `compute node`on csak annyit amennyi épp szükséges
> 
> ![storage network](http://platform9.com/wp-content/uploads/2015/12/Cinder-1-1-1024x559.png)

Minden volumenak van egy azonosítója, mennyi adat tárolható, ki hozta létre, stb metaadatattal, A *cinder-scheduler* dönti el mennyi hely áll még rendelkezésünkre. A *cinder-volume* viszont minden szerveren futni fog, ez kerül be minden VM-hez. A *cinder-backup*ban a volumeokról készíthetünk backupot.

![](https://accelazh.github.io/images/cinder-architecture.png)

![](https://image.slidesharecdn.com/storagebasedonopenstackmariocho-160220082601/95/storage-based-onopenstackmariocho-23-638.jpg?cb=1455958139)![](https://wiki.openstack.org/w/images/thumb/b/bb/SharedLVMsupport.png/600px-SharedLVMsupport.png)

**Cinderen belül tudunk**
- *volumeokat*: definiálni, ezek az egyes storage gépekhez tartozak, kb mint egy tradicionális hard drive. Ezeket felmountolhatjuk, vagy akár külön VMként is használhatjuk.
- *snapshot*: a VMről készítünk egy másolatot, technikailag ez is egy volume, de nincs felmountolva!
- *backup*: egy tömörített formátuma a volumenak.

```shell
sudo mkfs.ext3 dev/vdb
sudo mount dev/vdb mnt
```

# EA6 ~ Cinder és swift
Ha a virtuális gépet hackertámadás éri/leáll akkor a fájlok kvázi elvesztek a külső világ számára.

**=>** csináljunk egy perzisztens tárolót *block objektum*ok tárolására. 
- a felhasználó megmondja hány kötetre, mekkora tárolási területre van szüksége a VMhez, és ezt mountoljuk mint egy hagyományos adathordozót a VM-re
- de így a `storage network` köti össze ezeket aminél magas lesz a latency

![storage and compute nodes cinder](http://platform9.com/wp-content/uploads/2015/12/Cinder-1-1-1024x559.png)

## Cinder
> ![openstack block diagram block storage](https://docs.openstack.org/project-deploy-guide/openstack-ansible/ocata/_images/production-storage-cinder.png)
> 
>  A `cinder` kötet szinten kezeli a fájlokat
>
> - **cinder-api**:ezen át kommunikál a cinderrel a user
> - **rabbitmq server**: összeköti az apit a schedulerel
> - **cinder-scheduler**: a storage nodeot kezeli gyakorlatilag
> - **cinder- volume**: ez manageli a köteteket
> - **cinder backup**: egy-egy kötetet mint objektumot lehet átteni a swiftbe
>
> ### Cinder használt technológiái
>> - LVM: ezzel hozunk létre logikai köteteket amik már felhasználhatóak lesznek a sinderrel egy NetApp
>> - NFS: sriverekkel lehet cindereket létrehozni
>
> ### Cinder concepts
>> - volume: a raw tárolt block amit a Nován használunk
>> - snapshot: adott pillanatban készített másolat a kötet tartalmáról, ez az épp elérrhető állapotban levő kötetekről készíthető
>> - backup: archiváltuk, tömörítve, akár másik felhőn vagy fizikailag nálunk  van
> 
> ### Object storage
>> - távioli storage ami ftp szerverekhez ad hozzáférést, vagy dropbox/pinterest/stb oldlak háttere.
>> - lehet adott időre megadni a tárolási jogot, és utána töröljük

## Swift
> minden egy objektum, nincs fájlrendszer
>
> - access control list 
> - static webhost
> - admin

> - **object server**: a swift clusteren kezelt objektumokat kezeli
> - **auditor**: a felső manager, az objektumokat is kezeli, egy sqllite adatbázisba tesi a bejárt állományokat
> - **object expirer**: időzített törléekkel foglalkozik

# GY7 Swift vs volume
- `sudo fdisk -l` 
- `df -h`
- `sudo mkfs.ext3 dev/vdb` fájlrendszer létrehozása a disken
- `sudo fdisk -l` -el látszik
- `sudo mount dev/vdb mnt/` felmountoljuk a dev/vdb -t az mnt alá
- `sudo touch mnt/test_file.txt` <- így a tárolt adatok perzisztensen maradnak a felhőben

Az adattárolási megoldások a háttérben egy `block device`t használnak. Az `object store` inkább egy újabb, de eléggé feladat specifikus megoldásként használhatóak.

> **Konténerek:** egy mappa amikben több objektumot (fájlokat) tudunk eltárolni.
- `sat openrc`
- `cp openrc openrc-oerations`
- `nano openrc-opreations`
- `sourc openrc-operations`
- `swift list`
- `swift list countainer-dashboard`
- `swift download contaner-dashboard object-dashboard.txt`
- `cat object-dashboard.txt`
- `swift post container-cli`
- `swift list`
- `swift stat containers-dashboard`
- `swift post --read-acl ".r*,.rlistings" container-dashboard`
- `swift stat containers-dashboard`
- `swift opnestack api-endpoint`
- A container publikus api endpointjára hivatkozunk.

## EA7 - AWS, EC2, S3
https://azure.microsoft.com/en-us/free/students/

- `AWS`, `EC2` - számítási szolgáltatás 
- `S3` - tárolási

**IaaS szint**
| ![https://www.researchgate.net/publication/299982137/figure/fig1/AS:350755232993286@1460637972927/NIST-Visual-model-of-cloud-computing-definition.png](https://www.researchgate.net/publication/299982137/figure/fig1/AS:350755232993286@1460637972927/NIST-Visual-model-of-cloud-computing-definition.png)      | ![](https://cloud.netapp.com/hs-fs/hubfs/QWERTYUIUIOPOP.png?width=600&name=QWERTYUIUIOPOP.png) |
| ------------- |:-------------:| 

[AWS High Availability: Compute, SQL and Storage](https://cloud.netapp.com/blog/understanding-aws-high-availability-compute-sql-and-storage)

Azért kell nagy ram a VMekhez mert a DB server ramban tartja a DB-t, hogy gyorsabb legyen a lekérdezés.

### Amazon elastic compute cloud (EC2)
> ![EC2 lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/ami_lifecycle.png)
> 
> 1. kiválasztjuk mi az os
> 2. instence type
> 3. instence konfigurálás
>    -biztonsági modellek 
> 4. tárhely hozzáadása
> 5. portok megadása
> 6. security group
> 7. elasztikus IP megadása
>
> ajánlott irodalom: [Cloud Computing Bible](https://arpitapatel.files.wordpress.com/2014/10/cloud-computing-bible1.pdf)

## GY8 - Heat orchestration service
> **felhőfüggő megoldás:** csinálunk egy leíró fájlt *(infrastructure as a code)* és azt adjuk oda az értelmezőnek VM létrehozásához, így automatizáljuk a folyamatot
>
> **felhőfüggetlen megoldás:** külső eszközökkel hozzuk létre a fájlt, amik sok esetben más szolgltatásokat is adnak.
> 
> - `heat api`
> - `heat api cfn` 
> - `heat engine`
>
> ![heat orchestrator](https://cloudinfrastack.com/articles_img/openstack_02.jpg)
>
> `.yaml` fájlokkal definiljuk: megadjuk a `paraméter`eket, `servereket`, `volumeattach`, `output`:
> - **`paraméter`**: *string*, *description* itt változókat hozunk létre
> - **`resources`**: *string*; *type* - `OS::Nova::Server` - ezzel egy openstack novával létrehozunk egy szerver VM-et; *properties*: név, image fájl, network amihez csatlakozik; *volumeattach1*: megadjuk, hogy melyik volumeot csatoljuk fel a VMhez
>
> nem feladat az, hogy miképp fut le a az erőforrás, a konfig menedzsmentnek meg nem feladat az erforrás létrehozása, ilyen tool pl a cloud init

## EA8 - high availability - load balancing - autoscaling patterns (AWS)
> ajánlott irodalom: [Implementing Cloud Design Patterns for AWS](https://www.oreilly.com/library/view/implementing-cloud-design/9781782177340/)

Mi a *nagy rendelkezésre állás*:
- **rendelkezésre állás:** a rendszer reszponzivitása *(hogy kapjunk választ a kérdésekre)* nagyon fontos => ***néma gyereknek anyja se érti a szavát***
    - **monolitikus rendszer**eken nehezen megvalósítható
    - **multiserver - multi database rendszer** megnöveli a rendszer rendelkezésre állását
![AWS implementation - load balancer -ec2 instances](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2019/10/06/illustration-2.png)

### Multiserver 
> #### 1. EC2 instance
> 1. végy egy linux servert
> 2. SSH-n konfiguráljuk
>    - *ehhez saját észrevételek:*
>    - *hozz létre virtuális hálózatot (VPC) [e szerint a leírás szerint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html#CHAP_Tutorials.WebServerDB.CreateVPC.SecurityGroupEC2), persze válaszd ki előbb melyik opció kell neked ebből mert itt sok féle van, van dbhez is meg ec2höz is*
>     - *én nem csak inboundnak hanem outnak is megcsinaáltam mindent mert inbundként nem ment, ileltve mindnehova `0.0.0.0`-t adtam meg, mert úgy működött, ha saját IPt használtam akkor nem, de valszeg más volt az oka, szóval működnie kell saját ipvel is az SSH-s résznél* 
>     - *az ec2-t hozd létre [e szerint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html)*
>     - *amikor beSSHzol PUTTYal akkor azt [e szerint tudod](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) és itt usernek nem azt az `i-akármi`t adod ahogy írja hanem [ebből a listából](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html#TroubleshootingInstancesConnectingPuTTY) kiválasztod ami a te VM-ed és azzal be tudsz lépni. a többi lépést kövesd a leírás szerint és akkor oké.*
>
> #### 2. ELB létrehozása - elastic low balance server *(terhelés elosztó)*
> 1. megadjuk a **port**ot 
> 2. megadhatunk **helth chakc**et, hogy ellenőrizze a kapcsolatot az instanceokhoz, itt trasholdot is megadhatunk a betöltésekhez
> 3. megadjuk az **EC2 instance**ot az ELB alá.
> 4. **status chack** - ellenőrizzük az instanceok állapotát (fut/nem fut stb)
>
> #### 3. clone EC2
> klónozzuk akár virtualboxnál
> 
> #### 4. Új instance hozzáadása az ELB-hez
> hozzáadunk akárhány újat.
> 
> #### 5. Tesztelünk
> tesztelhetünk az AWS consolon, vagy 

### Multidata center pattern
> kihelyezhetjük több zónába a rendszert így karbantartáskor sem áll le.

### Auto scaleing pattern
![aws autoscaling pattern](https://static.packt-cdn.com/products/9781782177340/graphics/7340OT_02_08.jpg)
> [Scale out pattern](https://subscription.packtpub.com/book/web-development/9781782177340/2/ch02lvl1sec17/scale-out-pattern)
>
> Egy `Cloud watch` ha túlterhelődik az instance szól az `Autoscaling group`nak ami létrehoz egy új isntanceot az ELB-n
> 
> **1. launch config**
> **2. cloudWatch beállítása**
>    ```yaml
>    #!/bin/bash
>    yum install -y httpd stress
>    service iptables stop #Turn off firewall because it is enabled on ELB
>    echo welcome > /var/www/html/index.html #Makes a valid ELB helth check service httpd start
>    ```
>    
> **3. konfiguráljuk a lounch configot, pl az alábbi scripttel:**
>    ```yaml
>    #!/bin/bash
>    yum install -y httpd stress
>    service iptables stop
>    echo welcome > /var/www/html/index.html
>    service httpd start
>    ```
>    a `request stop instances` beállításával licitálunk a kihasználatlan rendszerkapacitásért. Olcsóbb példányokat kapunk, ha nyerünk a liciten, de a legtöbbet ajánló kapja meg.
>    
> **4. autoskálázási csoport létrehozása**
>    - megadhatjuk, hogy hány isntanceon induljon a csoport
>    - adhatunk alhálózatot
>    - load balancert állítunk be
>    - helth check típusát is mgeadhatjuk
>    
> **5. sklázási irányleveket adhatunk meg**
>    - megadhatjuk hány példány között skálázódik 
>    - risasztásokat hozhatunk létre amikt példányokhoz rendelhetjük, *pl: ha 5 percen keresztül a memóra használat x fölé emelkedik szól*  
>    - skálázási csoportokat is megadhatunk amik a riasztásokra váalaszolva pl kikapcsolják az adott túlterhelt VM-et
>    - *60s szabály*

## EA9 - Microsoft Azure
Ajánlott irodalom:
- [Barrie Sosinsky - cloud computing bible](https://arpitapatel.files.wordpress.com/2014/10/cloud-computing-bible1.pdf)
- [Windows Azure lépésről lépésre](https://docplayer.hu/730732-Windows-azure-lepesrol-lepesre.html)

> platform szolgltatóként az egyik legerősebb
> 
> ![azure services](https://mountainss.files.wordpress.com/2016/06/azure-services.jpg)
> 
> Platform as a Service model: *valahol a felhőben úgy futtatunk szolgáltatásokat, hogy a felhő egyéb szolgáltatsáokt integrál alá, pl SQL adaatbázis, ahol nem látjuk milyen VM fut alatta, csak azt, hogy tudunk lekérdezést indítani.*

### Számítási szolgáltatások - IaaS
> - A Microsoft elsődlegesen a saját virtualizációs technikáját használja, ez a HyperV.
> - `load balancer` engedi rá a felhasználót a VM-ekre.
> 
> #### Azure websites
> *IIS (Internet Information Server)* kommunikál a tárolóval.
> ![](https://mountainss.files.wordpress.com/2014/09/azure.jpg)
> 

### Adatkezelés
> *felhasznál* szempontjából nézve:
> 1. load balancer/web role instance
> 2. quee
> 3. worker roles
> 4. database
> 
> #### Azure SQL database
> - [docs.microsoft.com](https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview)
> 
> ![](https://docs.microsoft.com/en-us/azure/azure-sql/media/azure-sql-iaas-vs-paas-what-is-overview/sqliaas_sql_server_cloud_continuum.png)
> 
> A háttérben replikák készülnek az adatbázisról, azaz mi, felhasználóként egy adatbázist látunk, de gyakorlatilag több különböző helyen vannak tárolva.
> 
> **DTU**: Data Transaction Unit, egy tranzakció objektuma, benne az írási/olvasási műveletekkel. Az adatbázis "jóságának" mértékegyége, hogy hány műveletet tud végrehajtani teljes terhelés alatt, azaz hány DTU-ra képes
> 
> **eDTU**: elasztikus DTU, azaz egy adatbázisom van, de időnként nagyobb terhelést kap mint máskor, ekkor egy poolt hozunk létre az adatbázisainkból és ezekre használunk különböző standardokat:
> - basic: 0-5 eDTU
> - standard: 100-1200 eDTU
> - premium: 125-1500 eDTU

### Networking
### IT szolgáltatások
> ![services](![](https://i.pinimg.com/736x/15/6c/79/156c79e7f1a08575169d5b316940ca94.jpg))
### CDN
### [HADOOP](https://hadoop.apache.org/) - Bigdatához
> ![nist model of cloud computing](https://www.researchgate.net/publication/299982137/figure/fig1/AS:350755232993286@1460637972927/NIST-Visual-model-of-cloud-computing-definition.png)

## GY10 - Docker I
| ![](https://docs.docker.com/engine/images/architecture.svg)| ![](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/bltb6200bc085503718/5e1f209a63d1b6503160c6d5/containers-vs-virtual-machines.jpg) | ![](https://docs.docker.com/storage/images/types-of-mounts-volume.png) |
| ------------- |:-------------:| -----:|

> ***Ha a konténer futó progrmja bezárul akkor a konténer is bezárul!***

## EA10 ~ konzultáció
¯\\_( ͡❛ ͜ʖ ͡❛)_/¯

## GY11 - Docker II
> - `docker imager --help`
> - buildelés: `docker image build [path]`
> - `-d` detached
> - `--rm` remove
> 
> ***Nem törölhetünk docker imaget amíg konténer hivatkozik rá!***
> 
> **takarítás:**
> 1. töröljünk kontéreket: `docker container prune`
> 2. töröljünk imgeket
> 
> `docker run -it ubuntu20.04 bash` letöltjük az ubuntu 20.04 imaget és elindítjuk a `bash`-t
> 
> **docker image létrehozása:**
> 
> javasolt a hivatalos alap imagekből kiindulni!
> 
> ```python
> FROM python3.8 slim
> Workdir /app
> ADD . / app
> RUN pip install flask redis
> EXPOSE 80
> CMD ["python", "app.py"]
> ```
> - mentés `ctrl`+`o`
> - `dcker run -d -p 8080:80 --name app python-app:latest`
> - `docker ps`
> - `curl localhost:8080`
> - `docker stop app`
> - `docker rm app`
> - `ls -alh`
> - `docker images`

-----

# Záróvizsga tételek
## 1. Felhőszámítási rendszerek alapjai: definíciók, szolgáltatási és kialakítási modellek, felhasználási mintázatok
## 2. Felhőszámítási rendszerek alapjai: előnyök (felhasználói és szolgáltatói oldalról), technikai, üzleti és emberi tényezők
## 3. OpenStack felhő: architektúra és alapvető működési mechanizmusok
## 4. OpenStack Keystone: biztonsági jellemzők, alapkoncepciók és mechanizmusok
## 5. OpenStack Nova és Glance: virtuális gépekre vonatkozó jellemzők, alapkoncepciók és mechanizmusok
## 6. OpenStack Neutron: hálózati jellemzők, alapkoncepciók és mechanizmusok
## 7. OpenStack Cinder és Swift: tárolási jellemzők, alapkoncepciók és mechanizmusok
## 8. AWS IaaS megoldások (EC2 & tárolási szolgáltatások): jellemzők, alapkoncepciók és mechanizmusok (kifejezetten virtuális gépek menedzsmentjére vonatkozóan)
## 9. Magas rendelkezésre állás, terheléselosztás és automatikus skálázás az AWS-ben
## 10. Microsoft Azure / PaaS megoldások: jellemzők, alapkoncepciók és mechanizmusok (adatbázisok)
