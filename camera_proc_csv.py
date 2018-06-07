# !/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

import os


class camera_csv_processor:
    result_str = []

    def __init__(self):
        self.clear_csv_data_buf()
        pass

    def clear_csv_data_buf(self):
        self.result_str.clear()

    def read_color_resut(self, color_file_list):
        # awb_err = []
        snr_result = []
        exposure_err = []
        noise_result = [[], [], [], []]
        # currently we can handle 4 color files at most, ie, 4 rows of noise result at most
        color_sat = []
        color_delta_c_mean_corr = []
        color_delta_c_max_corr = []
        color_delta_c_mean_uncorr = []
        color_delta_c_max_uncorr = []
        color_delta_e_mean_uncorr = []
        color_delta_e_max_uncorr = []

        awb_err_fmt_5 = []
        awb_err_fmt_6 = []
        awb_err_fmt_7 = []
        awb_err_fmt_8 = []
        awb_err_fmt_9 = []
        awb_err_fmt_10 = []

        file_name_del_ext = [None, None, None, None]
        processed_color_test_file_count = 0

        """ If we just take the needed data from input color test files (".csv" type),
        the program will be simpler, and this variable would be useless.
        
        This variable is used to add title left for easy reading.
        """
        flag_add_for_left_title = True

        for i, color_file in enumerate(color_file_list):
            if color_file is None:
                continue

            """ Wrong files can not be processed correctly. So if file selected is not expected type or
                expected format, an error dialog will prompt out to notify users.
                
                As for the wrong files, we can judge by file extensions (should be ".csv" files), and 
                file titles (1st row) in content.  
                
                For those files with correct extensions, file titles, but unexpected data format,
                the program can not handle. It can not predict what the content in files would be like, 
                so it can not set proper judgement in advance. 
                 
            """
            if os.path.splitext(color_file)[1] != '.csv':
                return -(10+i+1)

            # print("os.path.splitext(color_file)[0] = %s , os.path.splitext(color_file)[1] = %s" %
            #      (os.path.splitext(color_file)[0], os.path.splitext(color_file)[1]))
            # if color_file is None:
            #    continue
            else:
                print('color file : ' + color_file)
                file_path_without_ext = os.path.splitext(color_file)[0]
                file_name = os.path.split(file_path_without_ext)[1]
                print('color file without extension is  : ' + file_name)

                file_name_del_ext.append("")

                with open(color_file, mode='r', newline='') as fd_read_color_csv:
                    reader = csv.reader(fd_read_color_csv)
                    row_sel = 0

                    print("in file %s " % color_file)

                    for row in reader:
                        """ use the title in row 1 for a rough check : whether users choose wrong csv file"""
                        if (row_sel == 0):
                            if (len(row) >= 3 and row[2].rfind("Colorcheck") != -1) or (
                                    len(row) >= 4 and row[3].rfind("Colorcheck") != -1):
                                pass
                            else:
                                return -(i + 1)

                        if (row_sel == 5):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            print("flag_add_for_left_title = %d" % flag_add_for_left_title)
                            if flag_add_for_left_title:
                                print('Line %03d, column %02d :  Add item title to left' % (row_sel, 9))
                                awb_err_fmt_5.append('awb error result')
                            awb_err_fmt_5.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 6):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            if flag_add_for_left_title:
                                awb_err_fmt_6.append('awb error result')
                            awb_err_fmt_6.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 7):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            if flag_add_for_left_title:
                                awb_err_fmt_7.append('awb error result')
                            awb_err_fmt_7.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 8):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            if flag_add_for_left_title:
                                awb_err_fmt_8.append('awb error result')
                            awb_err_fmt_8.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 9):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            if flag_add_for_left_title:
                                awb_err_fmt_9.append('awb error result')
                            awb_err_fmt_9.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 10):
                            # awb_err_fmt_item.append('awb_err   ')
                            # awb_err_fmt_item.append(row[9].strip())
                            print('Line %03d, column %02d :  %s' % (row_sel, 9, row[9].strip()))
                            if flag_add_for_left_title:
                                awb_err_fmt_10.append('awb error result')
                            awb_err_fmt_10.append(row[9].strip())
                            # awb_err.append([awb_err_fmt_5])

                        if (row_sel == 49):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                snr_result.append('SNR result: ')
                            snr_result.append(row[1].strip())

                        if (row_sel == 133):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                exposure_err.append('exposure_error')
                            exposure_err.append(row[1].strip())

                        if (row_sel == 135):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))

                            not_used_str = "_summary"
                            if file_name is not None:
                                index = file_name.rfind(not_used_str)
                                if (index == -1):
                                    noise_result[i].append('Avg_noise : ' + file_name)
                                else:
                                    noise_result[i].append('Avg_noise : ' + file_name[:index])

                            noise_result[i].append(row[1].strip())
                            noise_result[i].append(row[2].strip())
                            noise_result[i].append(row[3].strip())
                            noise_result[i].append(row[4].strip())

                        if (row_sel == 136):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_sat.append('Saturation')
                            color_sat.append(row[1].strip())

                        if (row_sel == 137):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_c_mean_corr.append('Delta-C mean corr')
                            color_delta_c_mean_corr.append(row[1].strip())

                        if (row_sel == 139):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_c_max_corr.append('Delta-C max corr')
                            color_delta_c_max_corr.append(row[1].strip())

                        if (row_sel == 140):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_c_mean_uncorr.append('Delta-C mean uncorr')
                            color_delta_c_mean_uncorr.append(row[1].strip())

                        if (row_sel == 142):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_c_max_uncorr.append('Delta-C max uncorr')
                            color_delta_c_max_uncorr.append(row[1].strip())

                        if (row_sel == 143):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_e_mean_uncorr.append('Delta-E mean uncorr')
                            color_delta_e_mean_uncorr.append(row[1].strip())

                        if (row_sel == 145):
                            print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                            # result_str.append(([row[9]]))
                            if flag_add_for_left_title:
                                color_delta_e_max_uncorr.append('Delta-E max uncorr')
                            color_delta_e_max_uncorr.append(row[1].strip())
                            break

                        row_sel = row_sel + 1

                    """ I am not sure whether the code below will be executed in case 
                        that failing to open or read color test file (".csv" type).
                        
                        If it will be executed, the code below should be moved to the 
                        "for loop" above, and we should make sure it will be executed 
                        exactly one time during reading a color test file.
                        
                        For example, we can put it to the place where one row is being read,
                        such as "row == 0" (the 1st row) , or "row == 145" (the last row we need)
                    """

                    file_name_del_ext[i] = file_name
                    processed_color_test_file_count = processed_color_test_file_count + 1

                flag_add_for_left_title = False
                # print(row)

        # result_str.append(awb_err)
        # result_str.extend(awb_err)

        """ When there is no color test file added, the function will return 
        in case that global variable "result_str" is filled with unexpected, useless 
        string or wrong string.  
        """
        if processed_color_test_file_count == 0:
            print(" None color test file is added ")
            return 0

        """
        output format : add top title for easy reading 
        We will remove '_summary' string in file name
        """

        top_file_title = [""]
        not_used_str = "_summary"
        for name in file_name_del_ext:
            if name is not None:
                index = name.rfind(not_used_str)
                if (index == -1):
                    top_file_title.append(name)
                else:
                    top_file_title.append(name[:index])
        self.result_str.append(top_file_title)
        self.result_str.append([])

        self.result_str.append(awb_err_fmt_5)
        self.result_str.append(awb_err_fmt_6)
        self.result_str.append(awb_err_fmt_7)
        self.result_str.append(awb_err_fmt_8)
        self.result_str.append(awb_err_fmt_9)
        self.result_str.append(awb_err_fmt_10)
        self.result_str.append([])

        # add top title
        self.result_str.append(top_file_title)
        self.result_str.append([])

        self.result_str.append(snr_result)
        self.result_str.append([])

        # add top title
        self.result_str.append(top_file_title)
        self.result_str.append([])
        self.result_str.append(exposure_err)
        self.result_str.append([])

        # add top title for noise
        noise_top_title = ["", "R", "G", "B", "Y"]
        self.result_str.append(noise_top_title)
        self.result_str.append([])

        # highlight : should use extend, not append
        # self.result_str.extend(noise_result)

        """ Need to do some test to confirm : for example, add 1st and 4th color file """
        for i in noise_result:
            if i is not []:
                self.result_str.append(i)
        self.result_str.append([])

        # add top title
        # add top title
        self.result_str.append(top_file_title)
        self.result_str.append([])
        self.result_str.append(color_sat)
        self.result_str.append(color_delta_c_mean_corr)
        self.result_str.append(color_delta_c_max_corr)
        self.result_str.append(color_delta_c_mean_uncorr)
        self.result_str.append(color_delta_e_max_uncorr)
        self.result_str.append(color_delta_e_mean_uncorr)
        self.result_str.append(color_delta_e_max_uncorr)
        self.result_str.append([])

        return processed_color_test_file_count

    def read_shading_result(self, shading_file_list):
        """
        lens_shading = [None, None, None, None]
        for i, shading_file in enumerate(color_file_list):
            if (shading_file is None) or (os.path.splitext(color_file)[1] != '.csv'):
                continue

        """
        if shading_file_list[0] is None:
            return 0

        if os.path.splitext(shading_file_list[0])[1] != '.csv':
            return -10

        print("process shading file : " + shading_file_list[0])
        with open(shading_file_list[0], mode='r', newline='') as fd_read_shading_csv:
            shading_result_reader = csv.reader(fd_read_shading_csv)

            row_sel = 0
            lens_shading = ['lens_shading mean']

            for row in shading_result_reader:

                """ use the title in row 1 for a rough check : whether users choose wrong csv file"""
                if (row_sel == 0):
                    if len(row) >= 4 and row[3].rfind("Falloff") != -1:
                        pass
                    else:
                        return -1

                if (row_sel == 15):
                    print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                    # result_str.append(([row[9]]))
                    lens_shading.append(row[1].strip() + '%')
                if (row_sel == 33):
                    print('Line %03d, column %02d :  %s' % (row_sel, 1, row[1].strip()))
                    lens_shading.append(('%.1f' % (float(row[1].strip()) * 100)) + '%')
                    break
                row_sel = row_sel + 1

        # add top title for shading result
        shading_result_top_title = ["", "Lens Shading", "Color Shading"]
        self.result_str.append(shading_result_top_title)
        self.result_str.append([])
        self.result_str.append(lens_shading)
        self.result_str.append([])

        return 1   # support only 1 shading test file

    def read_stepchart_result(self, stepchart_file_list):
        if stepchart_file_list[0] is None:
            return 0

        if os.path.splitext(stepchart_file_list[0])[1] != '.csv':
            return -10

        print("process step chart file : " + stepchart_file_list[0])
        with open(stepchart_file_list[0], mode='r', newline='') as fd_read_stepchart_csv:
            stepchart_result_reader = csv.reader(fd_read_stepchart_csv)

            one_step = 8.0
            row_sel = 0
            stepchart_result_str = []
            stepchart_list = []

            stepchart_result_str.append('stepchart ( max, min, range, num )')

            for row in stepchart_result_reader:
                """ use the title in row 1 for a rough check : whether users choose wrong csv file"""
                if row_sel == 0:
                    if len(row) >= 4 and row[3].rfind("Stepchart") != -1:
                        print("It may be a correct step test file")
                        pass
                    else:
                        print("The file is not step test file")
                        return -1

                if row_sel >= 8 and row_sel <= 25:
                    print('Line %03d, column %02d :  %s' % (row_sel, 1, ('%.1f' % float(row[1].strip()))))
                    # result_str.append(([row[9]]))
                    stepchart_list.append(float(row[1].strip()))
                    # stepchart_list.append(float('%.1f' % float(row[1].strip())))  # same as above , useless
                row_sel = row_sel + 1

        step_num = 1

        max_lumi = max(stepchart_list)
        min_lumi = min(stepchart_list)
        lumi_range = max_lumi - min_lumi

        for i in range(0, len(stepchart_list) - 1):
            print('stepchart list %02d : %f' % (i, stepchart_list[i]))
            if (stepchart_list[i] - stepchart_list[i + 1] >= one_step):
                step_num = step_num + 1

        stepchart_result_str.append(max_lumi)
        stepchart_result_str.append(min_lumi)
        stepchart_result_str.append(lumi_range)
        stepchart_result_str.append(step_num)

        # add top title for step chart result
        step_chart_title = ["", "Max", "Min", "Range", "Step num"]
        self.result_str.append(step_chart_title)
        self.result_str.append([])
        self.result_str.append(stepchart_result_str)
        self.result_str.append([])

        return 1   # support only 1 step chart test file

    def decide_file_save_path(self, color_file_list, step_file_list, shading_file_list):
        print("decide file save path (last added file) ")

        temp_path = None

        if shading_file_list[0] is not None:
            temp_path = shading_file_list[0]
        elif step_file_list[0] is not None:
            temp_path = step_file_list[0]
        else:
            i = 3
            while i >= 0:
                if color_file_list[i] is not None:
                    temp_path = color_file_list[i]
                    break
                i = i - 1

        """ Add only for debug
            if temp_path is None:
                print(" No file is selected to process, do nothing")
            else:
                print(" file save path is " + temp_path)
    
        return os.path.join(os.path.split(temp_path)[0], "result.csv")
    
        r"C:/Users/linchao/.spyder/Normal-Cap-SNR/Results \ result.csv"
    
        we expect it output "C:/Users/linchao/.spyder/Normal-Cap-SNR/Results/result.csv",
        however, it outputs strange path
    
        """

        if temp_path is None:
            return None
        else:
            return os.path.split(temp_path)[0] + r"/" + "result.csv"

    def write_result_csv(self, file_path):
        print("Save result to file result.csv to the last added file path on UI")

        if file_path is None:
            print(" No file is selected to process, do nothing")
        else:
            print("file will be saved under path: " + file_path)
            print("check abs path call : " + os.path.abspath(file_path))
            file_path_title = ["result file : ", os.path.abspath(file_path)]

            try:
                with open(file_path, mode='w', newline='') as fd_write_result_csv:
                    writer = csv.writer(fd_write_result_csv)
                    writer.writerow(file_path_title)
                    writer.writerow([])  # add blank line to sep different content
                    # writer.writerows(self.result_str)
                    for i in self.result_str:
                        writer.writerow(i)
            except IOError:
                print("Result file is opened, please close it before writing contents")
                return -10

            """
            If we use os.path.join, we will get path with double slash . 
            To use 'join' function of string , or connector "+" may be a good solution
            """
            last_path_config = os.getcwd() + os.path.sep + "last_data_path.txt"
            print("check default config file path :　%s " % last_path_config)

            try:
                with open(last_path_config, mode="w") as fd_last_path:
                    print("write last work dir to config file last_data_path.txt ")
                    print("last work dir =   " + os.path.split(os.path.abspath(file_path))[0])
                    print("try os dir name  =  " + os.path.dirname(file_path))
                    fd_last_path.write(os.path.split(file_path)[0])
            except IOError:
                print("Result file is opened, please close it before writing contents")
                return -20

        return 0

if __name__ == "__main__":
    color_file_path = [
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\D65-Cap_summary.csv',
        # r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\CWF-Cap_summary.csv',
        # r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\TL84-Cap_summary.csv',
        r'C:\Users\linchao\.spyder\Normal-Cap-SNR\Results\A-Cap_summary.csv']

    step_file_path = [
        r'C:\Users\linchao\.spyder\Grayscale\Results\flare_104_summary.csv', None]
    shading_file_path = [
        r'C:\Users\linchao\.spyder\Shading-Setting-0.8-Ratio-32\Results\DNP-Normal-Cap-Ratio-32_LF_Y.csv', None]

    csv_handler = camera_csv_processor()
    csv_handler.read_color_resut(color_file_path)
    csv_handler.read_shading_result(shading_file_path)
    csv_handler.read_stepchart_result(step_file_path)

    file_save_path = csv_handler.decide_file_save_path(color_file_path, step_file_path, shading_file_path)
    csv_handler.write_result_csv(file_save_path)
