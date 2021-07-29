from scyjava import config, jimport

config.add_endpoints('io.github.egonw.bacting:managers-cdk:0.0.20')
workspace_root = '.'
CDK = jimport('net.bioclipse.managers.CDKManager')
cdk = CDK(workspace_root)


