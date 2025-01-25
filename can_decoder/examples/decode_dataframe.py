import can_decoder
import mdf_iter
import matplotlib.pyplot as plt

from pathlib import Path


def setup_fs():
    """Helper function to setup the file system for the examples.
    """
    from fsspec.implementations.local import LocalFileSystem
    
    fs = LocalFileSystem()
    
    return fs


def example_decode_using_dateframe_j1939_a():
    """Example of loading a file and using the dataframe decoder to perform bulk operations on the data.
    """
    
    # Specify path to the DBC file containing the decoding rules.
    dbc_path = Path(__file__).parent / "CSS-Electronics-SAE-J1939-DEMO.dbc"

    # Import the decoding rules.
    db = can_decoder.load_dbc(dbc_path)
    
    # Create decoder.
    dataframe_decoder = can_decoder.DataFrameDecoder(db)
    
    # Setup filesystem and which log file to decode.
    fs = setup_fs()
    device = "LOG/EEEE0005"
    log_file = "{}/00000001/00000001.MF4".format(device)
    
    with fs.open(log_file, "rb") as handle:
        # Open the file and extract a dataframe with the raw CAN records.
        mdf_file = mdf_iter.MdfFile(handle)
        
        df = mdf_file.get_data_frame()
    
    # Decode the dataframe in a bulk operation.
    decoded_result = dataframe_decoder.decode_frame(df)
    
    print("Found a total of {} decoded messages".format(len(decoded_result)))
    print(decoded_result)
    
    return


def example_decode_using_dateframe_j1939_b():
    """Example of loading a file and using the dataframe decoder to perform bulk J1939 decoding. Uses SPNs instead
    of signal names, and drops the raw data column."""
    
    # Specify path to the DBC file containing the decoding rules.
    dbc_path = Path(__file__).parent / "CSS-Electronics-SAE-J1939-DEMO.dbc"
    
    # Import the decoding rules.
    db = can_decoder.load_dbc(dbc_path, use_custom_attribute="SPN")
    
    # Create decoder.
    dataframe_decoder = can_decoder.DataFrameDecoder(db)
    
    # Setup filesystem and which log file to decode.
    fs = setup_fs()
    device = "LOG/EEEE0005"
    log_file = "{}/00000001/00000001.MF4".format(device)
    
    with fs.open(log_file, "rb") as handle:
        # Open the file and extract a dataframe with the raw CAN records.
        mdf_file = mdf_iter.MdfFile(handle)
        
        df = mdf_file.get_data_frame()
    
    # Decode the dataframe in a bulk operation.
    decoded_result = dataframe_decoder.decode_frame(df, columns_to_drop=["Raw Value"])
    
    print("Found a total of {} decoded messages".format(len(decoded_result)))
    print(decoded_result)
    
    return


def example_decode_using_dateframe_obd2():
    """Example of loading a file and using the dataframe decoder to perform bulk J1939 decoding. Uses SPNs instead
    of signal names, and drops the raw data column."""
    
    dbc_path = Path(__file__).parent / "CSS-Electronics-OBD2-v1.3.dbc"
    
    db = can_decoder.load_dbc(dbc_path)
    
    dataframe_decoder = can_decoder.DataFrameDecoder(db)
    
    fs = setup_fs()
    device = "LOG/EEEE0005"
    log_file = "{}/00000001/00000001.MF4".format(device)
    
    with fs.open(log_file, "rb") as handle:
        mdf_file = mdf_iter.MdfFile(handle)
        
        df = mdf_file.get_data_frame()
    
    decoded_result = dataframe_decoder.decode_frame(df, columns_to_drop=["Raw Value"])
    
    valid_indices = ~decoded_result["Signal"].isin(["response", "length"])
    decoded_result = decoded_result[valid_indices]
    
    print("Found a total of {} decoded messages".format(len(decoded_result)))
    print(decoded_result)
    plot_decoded_data(decoded_result)
    
    return

def plot_decoded_data(decoded_result):
    """Vẽ đồ thị từ dữ liệu đã giải mã."""
    engine_rpm_data = decoded_result[decoded_result["Signal"] == "S1_PID_0C_EngineRPM"]
    
    if engine_rpm_data.empty:
        print("No data found for Engine RPM")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(engine_rpm_data.index, engine_rpm_data["Physical Value"], label="Engine RPM", color='b')
    
    plt.title("Engine RPM over Time", fontsize=16)
    plt.xlabel("Timestamp", fontsize=12)
    plt.ylabel("Engine RPM", fontsize=12)
    plt.xticks(rotation=45)
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    example_decode_using_dateframe_j1939_a()
    example_decode_using_dateframe_j1939_b()
    example_decode_using_dateframe_obd2()
    pass
