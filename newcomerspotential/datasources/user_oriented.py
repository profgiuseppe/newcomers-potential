"""
Implements a set of datasources oriented off of a single user.

.. autodata:: newcomerspotential.datasources.user_oriented.user

"""
from ..dependencies import DependentSet
from .datasource import Datasource

##same as revision_oriented
class User(DependentSet):
    """
    Represents a user's id and name/ip
    """

    def __init__(self, name, include_info=True,
                 include_first_session_revision=True,
                 include_first_session_edits=True,
                 include_first_session_uploads=False,
                 include_first_session_page_moves=False):
        super().__init__(name)
        self.id = Datasource(name + ".id")
        "`int` : The id of the user who saved the edit.  0 for IPs."
        self.text = Datasource(name + ".text")
        "`str` : The user's name or IP address"

        if include_info:
            self.info = UserInfo(name + ".info")
            """
            :class:`~newcomerspotential.datasources.user_oriented.UserInfo` :
            Information about the user.
            """
        
        if include_first_session_revision:
            self.first_session_edits = UserFirstSessionRevision(name + \
            ".first_revision")
                
        
        if include_first_session_edits:
            self.first_session_edits = UserFirstSessionEdits(name + \
            ".first_session")
            
        if include_first_session_uploads:
            self.first_session_uploads = UserFirstSessionUploads(name + \
            ".uploads")
            
        if include_first_session_page_moves:
            self.first_session_modes = UserFirstSessionMoves(name + ".moves")

class UserInfo(DependentSet):
    """
    Represents a user's information
    """

    def __init__(self, name):
        super().__init__(name)
        self.editcount = Datasource(name + ".editcount")
        "`int` : A count of edits the user has ever saved"
        self.registration = Datasource(name + ".registration")
        ":class:`mwtypes.Timestamp` : The date the user registered"
        self.groups = Datasource(name + ".groups")
        "`set` ( `str` ) : The groups the user is a member of"
        self.emailable = Datasource(name + ".emailable")
        "`bool` : `True` if the users is emailable, `False` otherwise"
        self.gender = Datasource(name + ".gender")
        "`str` : A string representing the user's ``gender`` preference."

class UserFirstSessionRevision(DependentSet):
    """
    Represents a user's first session revision
    """
    
    def __init__(self, name):
        super().__init__(name)
        self.revisions = Datasource(name + ".revision")
        """`list` ( `:class:Revision` ) : 
        The first revision belonging to user
        """


class UserFirstSessionEdits(DependentSet):
    """
    Represents a user's first session edits
    """
    
    def __init__(self, name):
        super().__init__(name)
        self.revisions =Datasource(name + ".edits")
        """`list` ( `:class:Revision` ) : 
        The revisions belonging to user's first session'
        """
        
class UserFirstSessionUploads(DependentSet):
    """
    Represents a user's first session file uploads
    """
    
    def __init__(self, name):
        super().__init__(name)
        self.revisions =Datasource(name + ".uploads")

class UserFirstSessionMoves(DependentSet):
    """
    Represents a user's first session page moves
    """
    
    def __init__(self, name):
        super().__init__(name)
        self.revisions =Datasource(name + ".page_moves")
