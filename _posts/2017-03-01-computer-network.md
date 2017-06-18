---
title: Computer-Network?
---

<p class="lead"> From this class, I just want to know more about network</p>
[youtube vedio](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)

>This teacher-ravula-is so good...

## Chapter: Computer Network and IP address.##
><br>ip address contains network ip and host ip. The total ip address is 2^32 which means we use 32 bits to represent.
<br>network ip address is divided into five classes(A-[1-126] B-(128-191) C-(192-223) D maybe for group? and E maybe for army)  A(8|network 24|host)
B(16|nework 16|host) C(24|network 8|ip)
<br>Casting(unicast(one ip to another) Broadcast[limited-255.255.255.255] Directed BC- Network ip + 255.)

ex what is 200.1.10.100-(Class C and network ip:200.1.0.0 ) and DBA(200.1.10.255) and LBA(255.255.255.255)

Limited BA means broadcast to yourself, but DB is broadcast to another network

## Chapter: Subnets, Subnets Mask, Routing.##
><br>network|subnet|host, subnets mask to find the right subnet. Subnet mask(network-1 host-0) Routing(network|subnet Mask interface)
<br>how we clarify the DBC and into subnet... if the user is in the same network- then do it as in the same network(we assume he knows the subnet)...But if outside, we assume he don't know the subnet inside the network
<br>The largest match to get the right interface. VLSM(variable length subnet masking) can divide the network into different size.(255.255.255.128 255.255.255.192)
<br>why use the leading number as subnet-cause we want s consistant range..
<br>255.255.255.192 in CA-{host ip(2^6-2) subnet(2^[18-8])}..in CB..in CC..

if the ip 200.5.2.24- which means he belongs the CC, if the mask is 255.255.255.192, then the network 200.5.2.0, subnet 200.5.2.0, and divide the network into 4 parts... we can find the subnet and host ip...

## Chapter: Classless Inter Domain Routing.##
><br>if we divide the whole network into Class(A-0,B-10,C-110,D-1111,E-1110) which means we can't choose the size of internet as we want. So CIDR shows.
<br>NID HID, the size of Network can be any 2^n u want. (200.2.1.20|27) means 27 for BID or NID then 5 bits for HID. SO the range of this network should be 200.2.1.0-200.2.1.31(2^5) and the first one(200.2.1.0 is used as BID and 200.2.1.31 is used as Direct Broadcasting so the avaible ip size is 32-2=30)
<br>(NID HID) so that the ip address can be comntinuous.  (100.1.2.40/28) we can find the whole network ip..(100.1.2.32-100.1.2.47)

The advantage of Class is that we already knows the network size and then can find the subnet host directly. However we can't divide the whole network as we what. CIDR is for any size of network size../

## Chapter: Subnetting in CIDR, VLSM in CIDR##
><br>(1)20.30.40.10/25 which means we have network id(20.30.40.0) and host ip to(20.30.40.127) total 2^7=128 ip address avaible. Then we can divide the network into 2/4/8...subnet work just needs to know the new one:20.30.40.10/26.
Which means the subnet mask is 255.255.255.96
<br>(2)The total network can also be devide by VLSM (which means not every subnet size is same..0/10/11)
<br>(3)In the computer we needs to know ipv4-(from ISP) DGW-(router) SM-(subnet mask) DNS-(change the domain to ip address). why we needs to know SM?(in previous, we know SM is for router to find the right interface then transmit the data to the right subnet)...Because if I_a add SM is same as Destination_IP add this SM, then we can say that they are at the same subnet, then A will send the data directly to B not router. Otherwise A will send it to router. (And maybe this assumption is not right.)
<br>(4)SM is 255.255.255.255 then which means A will always send the data to router..DBA- which just make host id to 1. so that only knows the DBA can't find the network ip....

## Chapter: Superneting##
><br><1>Combine some of the network together to get a superneting, so that other routers don't need to know any of the subnet. So that the condition for some of networks can combine togeher are: contiguous - -. exam:(200.1.0.0/24 200.1.1.0/24 200.1.2.0/24 200.1.3.0/24 can combine get:200.1.0.0/25). If we only wants to know whether this network belongs to the superneting, we just needs to change the SM to 255.255.255.192

another exam is : 100.1.2.0/25 100.1.2.128/26 100.1.2.192/26 also can combine to get a superneting 100.1.2.0/24 so that the SM will also changed. The SM of superneting is 255.255.255.0


## Chapter: Dela in Computer Network and Flow control Stop and Wait##
><br>(1)**Transmission Delay** **Tp**

## Chapter12: Capacity of pipe and pipline##
><br>(1)thick channel(pipe)- disadvantage at stop-and-read,  so using pipeling
<br>(2)<img src="https://lupingX.github.io/materials/computer-network/2.png" width = "300" height = "200" alt="capacity" align=center />
Capacity is BW*TP, which is associated with the length of the pipe and the width of the pipe. FULL duplex: means can transmit forward and backward,
Half duplex: means can only transmit forward.
<br>(2)(https://lupingX.github.io/materials/computer-network/1.png)
Stop-and-read protocol: one package transmit to the channel, then waiting for the response from server. efficiency:1/(1+2*w)=1/4
<br>(3)https://lupingX.github.io/materials/computer-network/3.png)
Pipeline: if the size of the sequence can be chose, then u can have efficiency of 100%.
The window size should be 1+2a which equals to the number of sequence u needed.
Then the field of the sequence should be log2(number of sequence).
But as the second figure, if u prefix the field of sequnce, then the efficient could decrease as showed in picture.