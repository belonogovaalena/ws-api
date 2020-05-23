from WSService import WSService


if __name__ == '__main__':
    service = WSService(export_log=True)
    for i in range(4):
        model = service.get_model()
        print(model.to_string())
