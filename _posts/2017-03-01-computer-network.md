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