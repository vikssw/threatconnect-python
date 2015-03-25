from working_init import *

""" Working with Threats """

""" Toggle the Boolean to enable specific examples """
enable_example1 = False
enable_example2 = False
enable_example3 = False
enable_example4 = False
enable_example5 = False


def show_data(result_obj):
    """  """
    pd('Threats', header=True)
    pd('Status', result_obj.get_status())
    pd('Status Code', result_obj.get_status_code())
    pd('URIs', result_obj.get_uris())

    if result_obj.get_status().name == "SUCCESS":
        for obj in result_obj:
            pd('Threat Data', header=True)
            pd('_api_request_url', obj.get_request_url())
            pd('_matched_filters', obj.get_matched_filters())

            # print resource data using dynamic method calls
            for method_data in sorted(obj.get_methods()):
                method = getattr(obj, method_data['method_name'])
                pd(' %s' % method_data['name'], method())
    pd('Stats', header=True)
    pd('Result Count (Total)', result_obj.get_result_count())
    pd('Result Count (Filtered)', len(result_obj))


def main():
    """ """
    # get all owner names
    owners = tc.owners()
    owners.retrieve()
    owners.get_owner_names()

    if enable_example1:
        """ get threats for owner org """

        # optionally set max results
        tc.set_max_results("500")

        # threats object
        threats = tc.threats()

        # retrieve indicators
        threats.retrieve()

        # show indicator data
        show_data(threats)

    if enable_example2:
        """ get threats for filtered owners """

        # optionally set max results
        tc.set_max_results("500")

        # threats object
        threats = tc.threats()

        # get filter
        filter1 = threats.add_filter()
        owners = ['Acme Corp']
        filter1.add_owner(owners)

        # check for any error on filter creation
        if filter1.error:
            for error in filter1.get_errors():
                pd(error)
            sys.exit(1)

        # retrieve indicators
        threats.retrieve()

        # show indicator data
        show_data(threats)

    if enable_example3:
        """ get threats by id """

        # optionally set max results
        tc.set_max_results("500")

        # threats object
        threats = tc.threats()

        # get filter
        filter1 = threats.add_filter()
        owners = ['Acme Corp']
        filter1.add_owner(owners)
        filter1.add_id(728252)

        # check for any error on filter creation
        if filter1.error:
            for error in filter1.get_errors():
                pd(error)
            sys.exit(1)

        # retrieve indicators
        threats.retrieve()

        # show indicator data
        show_data(threats)

    if enable_example4:
        """ get threats by indicator/indicator_type """

        # optionally set max results
        tc.set_max_results("500")

        # threats object
        threats = tc.threats()

        # get filter
        filter1 = threats.add_filter()
        owners = ['Acme Corp']
        filter1.add_owner(owners)
        filter1.add_indicator('felixos.com')
        filter1.add_tag('China')

        # check for any error on filter creation
        if filter1.error:
            for error in filter1.get_errors():
                pd(error)
            sys.exit(1)

        # retrieve indicators
        threats.retrieve()

        # show indicator data
        show_data(threats)

    if enable_example5:
        """ get threats by multiple filters """

        # optionally set max results
        tc.set_max_results("500")

        # threats object
        threats = tc.threats()

        # get filter
        filter1 = threats.add_filter()
        owners = ['Acme Corp']
        filter1.add_owner(owners)
        filter1.add_tag('ShellShock')

        # check for any error on filter creation
        if filter1.error:
            for error in filter1.get_errors():
                pd(error)
            sys.exit(1)

        # get filter
        filter2 = threats.add_filter()
        owners = ['Acme Corp']
        filter2.add_owner(owners)
        filter2.add_indicator('67.229.128.88')

        # check for any error on filter creation
        if filter1.error:
            for error in filter1.get_errors():
                pd(error)
            sys.exit(1)

        # retrieve indicators
        threats.retrieve()

        # show indicator data
        show_data(threats)

if __name__ == "__main__":
    main()
