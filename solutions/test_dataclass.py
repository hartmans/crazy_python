# Solution:
import random
import math
import urllib.parse as uri_parse

MUMBLAGE= ('goo', 'moe', 'ven', 'arep', 'N!q', 'Qvep', 'VeNa', 'zo', 'oz', 've')

def root_password_gen():
      # Okay, I was having fun with this. It does generate reasonably
      # secure passwords, but they are worse than random strings in
      # terms of memorizability,and this is an overly complex way to
      # generate passwords that hard to remember.
    l = len(MUMBLAGE)
    bits = 160
    rand = random.getrandbits(bits)
    password = ""
    while bits > 0:
        password += MUMBLAGE[rand%l]
        rand = rand//l
        bits -= math.log2(l)
    return password


@dataclasses.dataclass(unsafe_hash=True)
class LinuxMachine:

    hostname: dataclasses.InitVar(str) = dataclasses.field(compare=True, hash=True, init=False)
    root_password: str = dataclasses.field(hash=False,compare=False, repr=False, default_factory=root_password_gen)

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, val):
        if hasattr(self, '_hostname'):
            raise AttributeError('hostname cannot be changed')
        self._hostname = val

    hostname:str =  dataclasses.field(compare=True, hash=True, default=hostname)
    root_password: str = dataclasses.field(hash=False,compare=False, repr=False, default_factory=root_password_gen)

    def __post_init__(self):
        if self.hostname is self.__class__.hostname:
            raise TypeError('hostname is required')
        
@dataclasses.dataclass(unsafe_hash=True)
class WebServer(LinuxMachine):

    uri: url_parse.ParseResult = dataclasses.field(compare=False, hash=False, kw_only=True)

    def __post_init__(self, ):
        if not isinstance(self.uri, uri_parse.ParseResult):
            self.uri = uri_parse.urlparse(self.uri)
        if self.hostname != self.uri.netloc:
            raise ValueError('Hostname and the host component of the URI must match')

