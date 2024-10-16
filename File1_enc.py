# ENCODED BY RIZzY
import marshal, base64, zlib
rizzy = '''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AI9yAAAAjnJ6cALabWUC2gAAAI1yc3NjA9oLKQAAAAtyAAAACnJORUtPVF9URUcJ2gAAAIpyAAAAHnIAAABecgAAAIRyAAAAg3IAAACCcgAAAIFyAAAAJnIAAAAIcgAAAC9yAAAAW3IAAACFcgAAACNyAAAAInIAAAAhcgAAACByAAAAH3IUKQAAAAHpLm5pYWdhIHlydCBlc2FlbFAgIW5vaXRwTyBkaWxhdm5JbTc5OzFbGyBdbTc5OzFbGyFtNzk7MVsbW203OTsxWxtBegAAADVyIDogZWlrb29DIF0rWw16AAAAGnIuc2xhaXRuZWRlcmMga2NlaGMgZXNhZWxQIC5uZWtvdCBldmVpcnRlciB0b24gZGx1b0MgOnJvcnJFOnogIXJldG5FIHNzZXJQIF0rWxF6bTc5OzFbGwd6bTI5OzFbGyA6IG5la29UIHJ1b1kgXZOc4lsAAAAadW5la290X3NzZWNjYQzaAAAAdXIAAAB2cgIpbmlnb2wvaHR1YS9tb2Mua29vYmVjYWYuaHBhcmctYi8vOnNwdHRoJ3pkcm93c3NhcAjabGlhbWUF2nlla19pcGEH2gAAAG9yAAAAbnIAAABpcgYpZDQxY2RkMTIwYTc5ZmIyMDc4OWFkMTYzMDk0OGEyODgg2nJlbGRuYUhodHVBYTRiRi5sb2NvdG9ycC5uaWdvbC50bnVvY2NhLmtvb2JlY2FmLm1vYzN6ZXRhY2l0bmVodHVhDNpuaWdvbC5odHVhCnpkZXRhUi1vcmVaCnp5dGlyb2lyUAjaeXJ0ZVItc0ktbm9naVQtWBB6c2dhVC1zY2l0eWxhbkEtdHNldXFlUi1iRi1YG3oEKQAAABtyaSAsMz11Bnplc2xhRgXabndvbmtudQfaAAAAUXIAAABQcgAAAE9yIDogZHJvd3NzYVAgXStbD3ogOiBsaWFtRSBdK1sMegAAABhyAAAAA3IAAAArcncB2gAAACxyAAAAdXIBKQAAADZydWRuYWdEWHphaVIvcHBhLmxlY3Jldi5yb2hjLW5la290Ly86c3B0dGgpeiA6IG5la29UIF0rWwx6AAAAR3IgOmVzb29oQyBdP1sMeiBuZWtvVCBodGlXIG5pZ29MIF0zWxV6IGVpa29vQyBtb3JGIG5la29UIHRlRyBdMlsaeiBkcm93c3NhUCAmIGRpVSBt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dHNlbWl0X3JldnJlcxHaZGlfZWNhcnRfdG5laWxjD9pzZ2F0X3NjaXR5bGFuYV9pcGFfYmYV2nNzYWxjX3JlbGxhY19pcGFfYmYT2mVtYW5feWxkbmVpcmZfcWVyX2lwYV9iZhjac2VsYmFpcmF2Cdp0YW1yb2YG2nl0dGVycAbaZWxhY29sBtpkb2h0ZW0G2mRpX2NvZF90bmVpbGMN2nRuZWdBLXJlc1UKeg2paGN0ZWYF2mV1cnQE2jg1ZWQ3YzU1ZTg3Zi03M2E5LWRmZjQtOWJjZi03M2I3YjY0NiT6XSJzZWNpdnJlU2hwYXJHIiwibm9pdGNlbm5vQ190QSJbIfplY2l2cmVzaHBhcmcM2nlyZXVRdG5ldG5vQ3RzaUxkbmVpckZzbm9pdHNlZ2d1UyHafTAwNTI6InRzcmlmX2duaXRhbmlnYXBfc2RuZWlyZl9ub2l0c2VnZ3VzIiws+joiZGlfZWxpZm9ycCJ7Dvpub3NqBNplc2xhZgXaU1VfbmUF2nRzb3AE2jgwMjkyNzI1OTQ2NTg0MDgyODk4ODY5ODMwMDI0HdpdOzEvV0ZfQkY7fTAyNTE9dGhnaWVoLDAyNz1odGRpdywwLjI9eXRpc25lZHsvTURCRjtpYmFlbXJhOmE3di1pYmFlbXJhL0FDQkY7MC4wLjExL1ZTQkY7WPovVkRCRjtzcGlsaWhwL0RCQkY7c3BpbGlocC9GTUJGOzU0NTc2NDc2L1ZCQkY7aXJlYmFLL1JDQkY7U1VfbmUvQ0xCRjthY3JvLmtvb2JlY2FmLm1vYy9OUEJGOzg0LjEuMCAuZPovVkFCRjtkaW9yZG5BLWFjck8vTkFCRlsY+mh0Z25lTC10bmV0bm9DDnplcHlULXRuZXRub0MMem5la29ULW5vaXRjZW5ub0MtYkYtWBV6cmV0c3VsQy1yZXZyZVMtYkYtWBN6cEktdG5laWxDLWJGLVgOemVuaWduRS1wdHRILWJGLVgQegapNzY1A9pkZWRvY25lbHJ1LW1yb2Ytd3d3LXgvbm9pdGFjaWxwcGEh+mV1clQE2nJlZ2lMBdpTMDE4QS1NUwh6TDAxNkctTVMIejAwMTZHLU1TCHoDqQAAAYnpAAAAZelOJikBdwBZA3gAdwBTAFkCYwBnAAEAAAAAAAABqyVkAAAAAAAAAAAXdAABEHIAJAAA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'''

exec(marshal.loads(base64.b64decode(rizzy)[::-1]))
