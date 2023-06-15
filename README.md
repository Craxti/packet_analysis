# Packet Analysis


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Bugs](#Bugs)
- [Contributing](#contributing)
- [License](#license)

* Read pcap package, print detailed icmp/tcp/udp protocol

* Read pcap packets or network interfaces

 1. Print detailed tcp session/udp message data, currently supports mysql/pgsql/smtp/ftp/redis/mongodb authentication protocol analysis, http/dns complete protocol analysis

 2. IP packet statistics information, used to monitor abnormal network traffic






# Install

 `pip install -r requirements.txt`


* [pynids](https://github.com/craxti/packet_analysis.git)

   * mac

   `brew install libnids`

   * linux

   `sudo apt-get install libnet1-dev libpcap-dev`

   `git clone https://github.com/craxti/packet_analysis.git`

   `cd pynids`

   `sudo python setup.py build`

   `sudo python setup.py install`

* [dpkt](http://dpkt.readthedocs.io/en/latest/index.html)

   `pip install dpkt`

   or

   `git clone https://github.com/kbandla/dpkt.git`


# Usage
* Read pcap package, print detailed icmp/tcp/udp protocol


    `python print_pcap.py --help`

    `python print_pcap.py --pcapfile=data/pcap_pub/http_gzip.pcap  --assetport=80`



* Read pcap packets or network interfaces, print detailed tcp session data


   Step 1: specify the configuration
   [server.yaml](etc/server.yaml)


   Step 2:
   `python print_tcp_session.py`



# Bugs
## libnids
1. Packets in ipv6 format are not supported


2. When server.yaml is configured to recombine bidirectional traffic


    `data_stream_direct: 2`

    The data will be printed only when the tcp flag is RST or FIN


3. Does not support multi-process


# Example

<code>python print_tcp_session.py</code>
=====================

<b> 1. UDP-DNS</b>

    pcap_file: data/pcap_pub/dns/netforensics_evidence05.pcap

    UDP-DNS protocol analysis

        {
      "ts": 1268758265.098157,
      "src_ip": "192.168.23.2",
      "src_port": 53,
      "dst_ip": "192.168.23.129",
      "dst_port": 52499,
      "header": {
        "aa": 0,
        "qr": 1,
        "num_of_answers": 1,
        "tc": 0,
        "num_of_additional": 4,
        "rd": 1,
        "opcode": "QUERY",
        "ra": 1,
        "num_of_authority": 4,
        "rcode": "NOERROR",
        "id": 48291,
        "num_of_questions": 1
      },
      "questions": [
        {
          "qclass": "IN",
          "qtype": "A",
          "qname": "freeways.in."
        }
      ],
      "answers": [
        {
          "ttl": 5,
          "rname": "freeways.in.",
          "rtype": "A",
          "rclass": 1,
          "rdata": "212.252.32.20"
        }
      ],
      "authority": [
        {
          "ttl": 5,
          "rname": "freeways.in.",
          "rtype": "NS",
          "rclass": 2,
          "rdata": "ns4.everydns.net."
        }
      ],
      "additional": [
        {
          "ttl": 5,
          "rname": "ns4.everydns.net.",
          "rtype": "A",
          "rclass": 1,
          "rdata": "208.76.60.100"
        }
      ]
    }


<b> 2. TCP-HTTP Protocol Details </b>

    pcap_file: data/pcap_pub/cve/cve-2016-4971.pcap

    {
      "ts_start": 1467904494.307728,
      "ts_end": 1467904494.392242,
      "src_ip": "192.168.186.128",
      "src_port": 41352,
      "dst_ip": "192.168.186.128",
      "dst_port": 80,
      "req_method": "GET",
      "req_uri": "/file",
      "req_version": "1.1",
      "req_headers": {
        "user-agent": "Wget/1.17 (linux-gnu)",
        "accept": "*/*",
        "accept-encoding": "identity",
        "host": "192.168.186.128",
        "connection": "Keep-Alive"
      },
      "req_body": "",
      "resp_version": "1.0",
      "resp_status": "301",
      "resp_reason": "Moved Permanently",
      "resp_headers": {
        "server": "SimpleHTTP/0.6 Python/2.7.12",
        "date": "Thu, 07 Jul 2016 15:14:54 GMT",
        "location": "ftp://anonymous@192.168.186.128:21/.wgetrc"
      },
      "resp_body": ""
    }

<b> 3. IP packet meta information</b>

    Packet Direction Timestamp Protocol Type Source IP: Source Port (IP Attribution) (Service Type) Destination IP: Destination Port (IP Attribution) (Service Type) Packet Size


    IN	2017-08-18 13:23:41 TCP 58.217.200.117:14000(Nanjing City, Jiangsu Province-None-None-NONE)(scotty-ft) 10.0.0.2:58747(LAN-None-None-NONE)(NONE) 240

    OUT 2017-08-18 13:23:41 TCP 10.0.0.2:58747(LAN-None-None-NONE)(NONE) 58.217.200.117:14000(Nanjing City, Jiangsu Province-None-None-NONE)(scotty-ft ) 40


   Remarks: 14000(scotty-ft) protocol for sending audio files for WeChat and QQ


<code>python print_pcap.py</code>
===================

1. UDP packet

   <code>python print_pcap.py --pcapfile=data/pcap_pub/dns/dns.pcap</code>

        [UDP]	[1112201545.38	2005-03-30 16:52:25]	217.13.4.24:53(00:12:a9:00:32:23) ----->192.168.170.56:1711(00:60:08:45:e4:55)	ttl=58	DATA_BINARY=76 63 85 83 00 01 00 00 00 00 00 00 05 47 52 49 4d 4d 0b 75 74 65 6c 73 79 73 74 65 6d 73 05 6c 6f 63 61 6c 00 00 01 00 01	LEN=41

2. TCP message

    <code>python print_pcap.py --pcapfile=data/pcap_pub/cve/httpoxy.pcap</code>

        [TCP]   [1469135972.46  2016-07-21 21:19:32]    192.168.235.135:55034(00:0c:29:92:67:d7) ----->192.168.235.136:8080(00:0c:29:79:fd:94)  SEQ=618963631   ACK=2424513936  FLAGS=['ACK', 'PSH']    WIN=229 DATA=GET /index.py HTTP/1.1
        Host: 192.168.235.136:8080
        User-Agent: curl/7.43.0
        Accept: */*
        Proxy: 192.168.235.135:11000

3. ICMP message


        [ICMP_Unreach]	[1500285748.08	2017-07-17 10:02:28]	10.0.0.5:500(98:01:a7:9e:dd:c1) ----->10.0.0.2:63816(58:f3:9c:51:90:c7)	3:3[host:port unreachable]	ttl=43	DATA_BINARY=	LEN=0


