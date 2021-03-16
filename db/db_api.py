

def dependent_id_to_manager_id(messenger_dependent_id):
    from db.mymodels import ManagerToDependent, Subscription
    dependent = Subscription.get(messenger_user_id=messenger_dependent_id).account
    manager = ManagerToDependent.get(dependent=dependent).manager
    return Subscription.get(account=manager).messenger_user_id