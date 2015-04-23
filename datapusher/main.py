import os

import ckanserviceprovider.web as web

import jobs

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

# check whether jobs have been imported properly
assert(jobs.push_to_datastore)


def serve():
    web.init()
    
    if web.app.config.get('DOCKER'):
        http_server = HTTPServer(WSGIContainer(web.app))
        http_server.listen(web.app.config.get('PORT'))
        IOLoop.instance().start()

    else:
        web.app.run(web.app.config.get('HOST'), web.app.config.get('PORT'))



def serve_test():
    web.init()
    return web.app.test_client()


def main():
    import argparse

    argparser = argparse.ArgumentParser(
        description='Service that allows automatic migration of data to the CKAN DataStore',
        epilog='''"He reached out and pressed an invitingly large red button on a nearby panel.
                The panel lit up with the words Please do not press this button again."''')

    argparser.add_argument('config', metavar='CONFIG', type=file,
                           help='configuration file')
    args = argparser.parse_args()

    os.environ['JOB_CONFIG'] = os.path.abspath(args.config.name)
    serve()

if __name__ == '__main__':
    main()
