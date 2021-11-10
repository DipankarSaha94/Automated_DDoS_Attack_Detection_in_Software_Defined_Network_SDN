from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def sampleTopo():

    net = Mininet( controller=RemoteController )
    info('Adding controller...\n' )
    net.addController( 'c0', controller = RemoteController, ip="10.0.2.15",port = 6666)

    info('Adding hosts...\n' )
    h1 = net.addHost( 'h1', ip = '10.0.0.21' )
    h2 = net.addHost( 'h2', ip = '10.0.0.22' )
    h3 = net.addHost( 'h3', ip = '10.0.0.23' )

    info('Adding switches...\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    info('Creating links...\n')
    net.addLink( h1, s1 )
    net.addLink( s3, h3 )
    net.addLink( s2, h2 )
    net.addLink( s1, s2 )
    net.addLink( s2, s3 )
    net.addLink( s1, s3 )

    info('Starting network...\n')
    net.start()

    info('Running CLI...\n')
    CLI(net)

    info('Stopping network...\n')
    net.stop()

setLogLevel( 'info' )
sampleTopo()
