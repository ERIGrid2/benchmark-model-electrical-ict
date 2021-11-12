from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange,dumpNodeConnections
import time

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():
    NODE2_IP='192.168.56.1'
    CONTROLLER_IP='127.0.0.1'
    net = Mininet( topo=None, build=False)
    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    # Switch to external gateway
    s777 = net.addSwitch( 's777' )

    # Switch to control center
    s999 = net.addSwitch( 's999' )

    # Switches in substation
    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )
    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )

    # Add host in control center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('ccdb', ip='100.0.0.12')

    # Add hosts in substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:01')
    s06m2 = net.addHost('s06m2', ip='100.6.0.12', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:02')
    s06m3 = net.addHost('s06m3', ip='100.6.0.13', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:03')
    s06m4 = net.addHost('s06m4', ip='100.6.0.14', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:04')
    s06m5 = net.addHost('s06m5', ip='100.6.0.15', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:05')
    s06m6 = net.addHost('s06m6', ip='100.6.0.16', cls=CPULimitedHost, cpu=.1, mac='00:00:00:00:00:06')
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21', mac='00:00:00:00:00:0a')
    s06db = net.addHost('s06db', ip='100.6.0.22', mac='00:00:00:00:00:0b')
    s06gw = net.addHost('s06gw', ip='100.6.0.23', mac='00:00:00:00:00:0c')
    hacker = net.addHost('hacker', ip='100.6.0.99', mac='00:00:00:00:00:0f')

    # add hosts in substation 7
    s07m1 = net.addHost('s07m1', ip='100.7.0.11', cls=CPULimitedHost, cpu=.1)
    s07m2 = net.addHost('s07m2', ip='100.7.0.12', cls=CPULimitedHost, cpu=.1)
    s07m3 = net.addHost('s07m3', ip='100.7.0.13', cls=CPULimitedHost, cpu=.1)
    s07m4 = net.addHost('s07m4', ip='100.7.0.14', cls=CPULimitedHost, cpu=.1)
    s07m5 = net.addHost('s07m5', ip='100.7.0.15', cls=CPULimitedHost, cpu=.1)
    s07m6 = net.addHost('s07m6', ip='100.7.0.16', cls=CPULimitedHost, cpu=.1)
    s07m7 = net.addHost('s07m7', ip='100.7.0.17', cls=CPULimitedHost, cpu=.1)
    s07m8 = net.addHost('s07m8', ip='100.7.0.18', cls=CPULimitedHost, cpu=.1)
    s07m9 = net.addHost('s07m9', ip='100.7.0.19', cls=CPULimitedHost, cpu=.1)
    s07m10 = net.addHost('s07m10', ip='100.7.0.20', cls=CPULimitedHost, cpu=.1)
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    # Link switches between substations 
    net.addLink(s61,s62)
    net.addLink(s63,s62)
    net.addLink(s71,s72)
    net.addLink(s73,s72)
    net.addLink(s61,s999)
    net.addLink(s71,s999)

    # Link control center to switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link substation 06 merging unit to switch
    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m2,s63, intfName1='s06m2-eth1', params1={'ip':'100.6.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m3,s63, intfName1='s06m3-eth1', params1={'ip':'100.6.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m4,s63, intfName1='s06m4-eth1', params1={'ip':'100.6.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m5,s63, intfName1='s06m5-eth1', params1={'ip':'100.6.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06m6,s63, intfName1='s06m6-eth1', params1={'ip':'100.6.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s06cpc,s62)
    net.addLink(s06db,s62)
    net.addLink(s06gw,s61, intfName1='s06gw-eth1', params1={'ip':'100.6.0.23/24'})
    net.addLink(hacker,s61)

    # Link Substation 07 Merging unit to Switch
    net.addLink(s07m1,s73, intfName1='s07m1-eth1', params1={'ip':'100.7.0.11/24'})
    net.addLink(s07m2,s73, intfName1='s07m2-eth1', params1={'ip':'100.7.0.12/24'})
    net.addLink(s07m3,s73, intfName1='s07m3-eth1', params1={'ip':'100.7.0.13/24'})
    net.addLink(s07m4,s73, intfName1='s07m4-eth1', params1={'ip':'100.7.0.14/24'})
    net.addLink(s07m5,s73, intfName1='s07m5-eth1', params1={'ip':'100.7.0.15/24'})
    net.addLink(s07m6,s73, intfName1='s07m6-eth1', params1={'ip':'100.7.0.16/24'})
    net.addLink(s07m7,s73, intfName1='s07m7-eth1', params1={'ip':'100.7.0.17/24'})
    net.addLink(s07m8,s73, intfName1='s07m8-eth1', params1={'ip':'100.7.0.18/24'})
    net.addLink(s07m9,s73, intfName1='s07m9-eth1', params1={'ip':'100.7.0.19/24'}) 
    net.addLink(s07m10,s73, intfName1='s07m10-eth1', params1={'ip':'100.7.0.20/24'})   
    net.addLink(s07cpc,s72)
    net.addLink(s07db,s72)
    net.addLink(s07gw,s71, intfName1='s07gw-eth1', params1={'ip':'100.7.0.23/24'})

    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 6 switch to external gateway
    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.6.11/16'})
    net.addLink(s06m2,s777, intfName1='s06m2-eth0', params1={'ip':'10.0.6.12/16'})
    net.addLink(s06m3,s777, intfName1='s06m3-eth0', params1={'ip':'10.0.6.13/16'})
    net.addLink(s06m4,s777, intfName1='s06m4-eth0', params1={'ip':'10.0.6.14/16'})
    net.addLink(s06m5,s777, intfName1='s06m5-eth0', params1={'ip':'10.0.6.15/16'})
    net.addLink(s06m6,s777, intfName1='s06m6-eth0', params1={'ip':'10.0.6.16/16'})
    net.addLink(s06gw,s777, intfName1='s06gw-eth0', params1={'ip':'10.0.6.23/16'})

    # Link Host Substation 7 switch to external gateway
    net.addLink(s07m1,s777, intfName1='s07m1-eth0', params1={'ip':'10.0.7.11/16'})
    net.addLink(s07m2,s777, intfName1='s07m2-eth0', params1={'ip':'10.0.7.12/16'})
    net.addLink(s07m3,s777, intfName1='s07m3-eth0', params1={'ip':'10.0.7.13/16'})
    net.addLink(s07m4,s777, intfName1='s07m4-eth0', params1={'ip':'10.0.7.14/16'})
    net.addLink(s07m5,s777, intfName1='s07m5-eth0', params1={'ip':'10.0.7.15/16'})
    net.addLink(s07m6,s777, intfName1='s07m6-eth0', params1={'ip':'10.0.7.16/16'})
    net.addLink(s07m7,s777, intfName1='s07m7-eth0', params1={'ip':'10.0.7.17/16'})
    net.addLink(s07m8,s777, intfName1='s07m8-eth0', params1={'ip':'10.0.7.18/16'})
    net.addLink(s07m9,s777, intfName1='s07m9-eth0', params1={'ip':'10.0.7.19/16'})
    net.addLink(s07m10,s777, intfName1='s07m10-eth0', params1= {'ip':'10.0.7.20/16'})
    net.addLink(s07gw,s777, intfName1='s07gw-eth0', params1={'ip':'10.0.7.23/16'})


    # Build and start Network
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    # Configure GRE Tunnel
    s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')
    info( net[ 's06m1' ].cmd( 'python3 as06m1.py &amp' ) )
    info( net[ 's06m2' ].cmd( 'python3 as06m2.py &amp' ) )
    info( net[ 's06m3' ].cmd( 'python3 as06m3.py &amp' ) )
    info( net[ 's06m4' ].cmd( 'python3 as06m4.py &amp' ) )
    info( net[ 's06m5' ].cmd( 'python3 as06m5.py &amp' ) )
    info( net[ 's06m6' ].cmd( 'python3 as06m6.py &amp' ) )
    info( net[ 's07m1' ].cmd( 'python3 as07m1.py &amp' ) )
    info( net[ 's07m2' ].cmd( 'python3 as07m2.py &amp' ) )
    info( net[ 's07m3' ].cmd( 'python3 as07m3.py &amp' ) )
    info( net[ 's07m4' ].cmd( 'python3 as07m4.py &amp' ) )
    info( net[ 's07m5' ].cmd( 'python3 as07m5.py &amp' ) )
    info( net[ 's07m6' ].cmd( 'python3 as07m6.py &amp' ) )
    info( net[ 's07m7' ].cmd( 'python3 as07m7.py &amp' ) )
    info( net[ 's07m8' ].cmd( 'python3 as07m8.py &amp' ) )
    info( net[ 's07m9' ].cmd( 'python3 as07m9.py &amp' ) )
    info( net[ 's07m10' ].cmd( 'python3 as07m10.py &amp' ) )
    CLI( net )
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

    
