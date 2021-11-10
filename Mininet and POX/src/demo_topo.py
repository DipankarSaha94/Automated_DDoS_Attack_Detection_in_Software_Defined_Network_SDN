#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node, OVSKernelSwitch, UserSwitch, IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from time import sleep

def sampleTopo():
    net = Mininet(topo = None,
                  build = False,
                  ipBase = '10.0.0.0/8')

    info('Adding Controller...\n')
    c0 = net.addController(name = 'c0',
                           controller = RemoteController,
                           ip = '127.0.0.1',
                           protocol = 'tcp',
                           port = 6666)

    info('Adding switches...\n')
    s1 = net.addSwitch('s1', cls = OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls = OVSKernelSwitch)

    info('Adding hosts...\n')
    h1 = net.addHost('h1', cls = Host, ip = '10.0.0.91', defaultRoute = None)
    h2 = net.addHost('h2', cls = Host, ip = '10.0.0.92', defaultRoute = None)

    info('Creating links...\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)

    info('Starting the Network...\n')
    net.build()

    info('Starting Controllers...\n')
    for controller in net.controllers:
        controller.start()

    info('Starting Switches...\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])

    info('Pinging all hosts from all hosts...\n')
    net.pingAll()
    net.stop()

setLogLevel('info')
sampleTopo()

