from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel
from mininet.node import Controller
from mininet.cli import CLI

def run():
    net = Mininet(topo=SingleSwitchTopo(k=3), controller=Controller)
    net.start()

    print("\n--- Packet Logger Running ---\n")

    h1, h2, h3 = net.hosts

    # Generate traffic
    print("Pinging all hosts...\n")
    net.pingAll()

    print("\nStarting TCP traffic (iperf)...\n")
    h1.cmd('iperf -s &')
    print(h2.cmd('iperf -c ' + h1.IP()))

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
