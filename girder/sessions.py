import cherrypy
import datetime
import pickle


class PatchedCherrypySession(cherrypy.lib.sessions.FileSession):
    """
    Implementation of Cherrypy FileSession with the _save method fixed.

    The original implementation has an assert checking that the session is loaded before an
    automatic save. But we handle the locking/unlocking ourselves, making that check useless.

    These sessions are automatically cleaned after expiration thanks to a thread created by
    cherrypy.

    Inspired from https://github.com/cherrypy/cherrypy/pull/1834
    """

    def _save(self, expiration_time):
        if not self.locked:
            return
        with open(self._get_file_path(), 'wb') as f:
            pickle.dump((self._data, expiration_time), f, self.pickle_protocol)

    def save(self):
        """Save session data."""
        # If session data has never been loaded then it's never been
        #   accessed: no need to save it
        if self.loaded:
            t = datetime.timedelta(seconds=self.timeout * 60)
            expiration_time = self.now() + t
            if self.debug:
                cherrypy.log('Saving session %r with expiry %s' %
                             (self.id, expiration_time),
                             'TOOLS.SESSIONS')
            self._save(expiration_time)
        else:
            if self.debug:
                cherrypy.log(
                    'Skipping save of session %r (no session loaded).' %
                    self.id, 'TOOLS.SESSIONS')

    def get(self, key, default=None):
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
        self.load()
        return self._data.get(key, default)
