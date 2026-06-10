from mininet.node import OVSBridge
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel


class HybridWorkTopo(Topo):
    def build(self):

        # Remote Users
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Corporate Hosts
        corp_user = self.addHost('corp1')
        server1 = self.addHost('srv1')
        server2 = self.addHost('srv2')
        cloud = self.addHost('cloud')

        # Network Devices
        home_router = self.addSwitch('s1')
        internet = self.addSwitch('s2')
        firewall = self.addSwitch('s3')
        vpn_gateway = self.addSwitch('s4')
        corporate_lan = self.addSwitch('s5')

        # Remote Users -> Home Router
        self.addLink(h1, home_router,
                     cls=TCLink,
                     bw=50,
                     delay='10ms',
                     loss=1)

        self.addLink(h2, home_router,
                     cls=TCLink,
                     bw=50,
                     delay='15ms',
                     loss=1)

        self.addLink(h3, home_router,
                     cls=TCLink,
                     bw=50,
                     delay='20ms',
                     loss=2)

        # Network Path
        self.addLink(home_router, internet,
                     cls=TCLink,
                     bw=40,
                     delay='35ms',
                     loss=1)

        self.addLink(internet, firewall,
                     cls=TCLink,
                     bw=30,
                     delay='40ms',
                     loss=1)

        self.addLink(firewall, vpn_gateway,
                     cls=TCLink,
                     bw=25,
                     delay='30ms',
                     loss=1)

        self.addLink(vpn_gateway, corporate_lan,
                     cls=TCLink,
                     bw=100,
                     delay='10ms',
                     loss=0)

        # Corporate LAN
        self.addLink(corporate_lan, corp_user)
        self.addLink(corporate_lan, server1)
        self.addLink(corporate_lan, server2)

        # Cloud
        self.addLink(internet, cloud,
                     cls=TCLink,
                     bw=50,
                     delay='45ms',
                     loss=1)


def run():
    topo = HybridWorkTopo()

    net = Mininet(
    topo=topo,
    link=TCLink,
    switch=OVSBridge,
    controller=None
)

    net.start()

    print("\nTesting connectivity...\n")
    net.pingAll()

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
