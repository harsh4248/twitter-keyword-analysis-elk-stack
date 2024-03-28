import twint

def main():
    #configuration
    config = twint.Config()
    config.Search = "bitcoin"
    config.Lang = "en"
    config.Limit = 10
    config.Store_json = True
    config.Output = "custom_out.json"
    #running search
    # twint.run.Search(config)
    
if __name__ == '__main__':
    main()