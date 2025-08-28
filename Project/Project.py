import streamlit as st

# Thiết lập phong cách cho giao diện
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #333;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
    }
    .result {
        color: #004085;
        background-color: white;
        border: 1px solid white;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dữ liệu chuỗi ADN của các loài
adn_sequences = {
    "Con người": "GCGTAAACCAATCCACTGATTTCGACCACTGATGCCTAGCACAGTCTCACTGTCCCCGCTCATGGTTCTCTAAACCACACGTCTTGTTTCCTTCCTGTCCCTTGATTACATTTTCATCTATGTACTTTTCCTACTTGTTTTTTAATTATTCACCTTATTTTAAATTTCTAAACATAAAATTGTTCCTATGTTTTATATAC",
    "Con tinh tinh": "GCGTAAACCAATCCACTGATTTCGACCACTGATGCCTAGCACAGTCTCACTGTCCCCGCTCATGGTTCTCTAAACCACACGTCTTGTTTCCTTCCTGTCCCTTGATTACATTTTCATCTATGTACTTTTCCTACTTGTTTTTTAATTATTCACCTTATTTTAAATTTCTAAACATAAAATTGTTCCTATGTTTTATATAC",
    "Con chó nhà": "GCCCCCGCCTCACTCCCCGGGACGCAGGAAACCCGGGCGCCTGCGAGCAGCGGCTCCTCCTGGCTCCAAGGAGCCCAGGCCGTTGTTCGTGCCCTCCGGGTCTTTAAAGTCTGACTCTCATCTTCCCAAATTCCCTTCTCGGTGGAGGTTGCGAAGGAAAGCCCGAGGTAGGGCGCGCGATGCTGAGGGCTCGATGGGGA",
    "Sói sám": "GTGTCCATAGTATATATTAATATCTTTCTGGCATTCATTCTTTCTCTAATAGGTATACTTGTTTATCGATCACACCTAATATCATCGCTACTATGCTTAGAGGGCATAATATTATCACTATTTGTAATAATATCTGTAACTATTCTCAACAATCACCTCACATTAGCCAGCATGATACCAATCGTACTACTAGTATTTGC",
    "Hổ": "ATGGATTACTACAGAAAATATGCAGCTGTCATTCTGGCCATACTCTCTGTGTTTCTGCATATTCTCCATTCTTTTCCTGATGGAGAGTTTACAATGCAGGGTATGTGACCAAACAGATTTTCAGCAATAGGGAAAACACACACTTCTAGATATATGTCAATAACTCCATTAATTACATTTCTACTTCCTTTTTAAATGTG",
    "Mèo": "AGGCAGATAAGAAATCCTGGGGAGGGGGAGGGCCCCTTATATAGTGTGGGGGGACGGGTCCTGCTCAGATCCTCCTTGGGTGGCCTGTGACTGCTCAGATCCTGGTGTGATCTCTCTCAAGATGCCTGAGCCGGGGAAGAAGCCAGGTAGCCGCAGGTCTAGGGTTGGGGCTGAGTGGGGGGCCAGGGGGGCTGGGGCAT",
    "Hà mã": "ATAAATCCCTTCGTCTCTGTCATTATCTACACAACCATCATCCTGGGGACCATAATTGTAATAACTAGCTCTCACTGACTATTAACTTGAACCGGGTTCGAAATAAACATGCTAGCTATTATCCCCATCATAATGAAATCACCCAACCCACGAGCCACAGAAGCCTCCGTTAAATACTTCATAACCCAAGCCACCGCCTC",
    "Cá nhà táng": "AGCTGTCGGAGCCAGGACACCCGGTCAGCCCACTCTCGCTCTTCTTCTCTTCTTCAGACTGTGCCATGGTGCTCAGCGAGGGAGAATGGCAGTTGGTTCTGCACGTCTGGGCGAAGGTGGAGGCTGATGTCGCAGGCCATGGGCAGGACATCCTCATCAGGTAAGAGGAAGAAATTCCATTGCCCCTATCACCTACTTCC",
    "Hoa hồng": "TTGGAATTGTGGGTTTGTCTCAATCTATACAAAGACTGAGAGCAGCAGCTCATCTTGTAGTTTAGTATGACACTCGTGTCCTTATAATTTTCTAATTGTTAATTTGTTGTGGTAATACTTGATTCAGAAGTGTTGGAATGTGGTGAAAGAGGGTCAGAGTCAGACCATCCTATGTTAAATGACCACTGCAAAAGGGGTGA",
    "Dâu tây": "CCTGGTTTTTGCGATCAGCGAGGTATAGAGTTCCTACGTTCATTATAAATTCGTAGGAACTTCATACTGTGCTCTTTGTAGACAAAAAAACAAACAAGCCTGGTTTTTGCCATCAGCGTGGAATAGAGTTCGTACGTACATTATGAACTCGGAGGAACTTCAGACCGTGCTCTTGGAAGACCAAAAAACAAACAAG"
}

# Dữ liệu RNA của các loài
rna_sequences = {
    "Con người": "CGCAUUUGGUUAGGUGACUAAAGCUGGUGACUACGGAUCGUGUCAGAGUGACAGGGGCGAUACCAGAUGAUUUGGUGUGCAGAACAAAGGAAGGACAGGGAAUCAAUGUAAAAGUAGAUACAUGAAAAGGAUGAACAAGAAAAAUUAAUAAGUGGAAUAAAACUUUAAGAUUUGUAUUUUAACAAGGAUACAAAAUAUAUG",
    "Con tinh tinh": "CGCAUUUGGUUAGGUGACUAAAGCUGGUGACUACGGAUCGUGUCAGAGUGACAGGGGCGAUACCAGAUGAUUUGGUGUGCAGAACAAAGGAAGGACAGGGAAUCAAUGUAAAAGUAGAUACAUGAAAAGGAUGAACAAGAAAAAUUAAUAAGUGGAAUAAAACUUUAAGAUUUGUAUUUUAACAAGGAUACAAAAUAUAUG",
    "Con chó nhà": "GCCCCCGCCUCACUCCCCGGGACGCAGGAAACCCGGGCGCCUGCGAGCAGCGGCUCCUCCUGGCUCCAAGGAGCCCAGGCCGUUGUUCGUGCCCUCCGGGUCUUUAAAGUCUGACUCUCAUCUUCCCAAAUUCCCUUCUCGGUGGAGGUUGCGAAGGAAAGCCCGAGGUAGGGCGCGCGAUGCUGAGGGCUCGAUGGGGA",
    "Sói sám": "GUGUCCAUAGUAUAUAAUUAUAUCUUUCUGGCAUUGAUUCUUUCUCUAAUAGGUAUACUUGUUUAUCGAUCACACCUAAUAUCAUCGAUACUAUGCUUAAGUGGGUAUUAUAAUAGUGAUAAACAUUAUAUAGACAUUGAUAAGAGUUGUUAGUGGAGUGUAAUCGGUCGUACUAUGGUUAGCAUGAUGAUCAUAAACG",
    "Hổ": "AUGGAUUACUACAGAAAAUAUGCAGCUGUCAUUCUGGCCAUACUCUCUGUGUUUCUGCAUAUUCUGGAUUCUUUUCCUGAUGGAGAGUUUACAAUGCAGGGUAUGUGACCAAACAGAUUUUCAGCAAUAGGGAAAACACACACUUCUAGAUAUAUGUCAAUAACUCCAUUAAUUACAUUUCUACUUCCUUUUUAAAUGUG",
    "Mèo": "AGGCAGAUAAGAAAUCCUGGGGAGGGGGAGGGCCCCUUAUAUAGUGUGGGGGGACGGGUCCUGCUCAGAUCCUCCUUGGGUGGCCUGUGACUGCUCAGAUCCUGGUGUGAUCUCUCUCAAGAUGCCUGAGCCGGGGAAGAAGCCAGGUAGCCGCAGGUCUAGGGUUGGGGCUGAGUGGGGGGCCAGGGGGGCGGGGCAC",
    "Hà mã": "AUAAAUCCCUUCGUCUCUGUCAUUAUCUACACAACCaucaucCUGGGGACCAUAAUUGUAAUAACUAGCUCUCACUGACUAUUAACUUGAACCGGGUUCGAAAAUAAACAAUGCUAGCUAUUAUCCCCAUGAUAAUGAAAUCACCCAACCCACGAGCCACAGAAGCCUCCGUUAAAUACUUCAUAACCCAAUCCACCGCCUC",
    "Cá nhà táng": "AGCUGUCGGAGCCAGGACACCCGGUCAGCCCACUCUCGCUCUUCUUCUCUUCUUCAGACUGUGCCAUGGUGCUCAGCGAGGGAGAAUGGCAGUUGGUUCUGCACGUCUGGGCGAAGGUGGAGGCUGAUGUCGCAGGCCAUGGGCAGGACAUCCUCAUCAGGUAAGAGGAAGAAAUUCCAUUGCCCCUAUCACCUACUUCC",
    "Hoa hồng": "UUGGAAUUGUGGGUUUGUCUCAAUCUAUGCAAAGACUGAGAGCAGCAGCUCAUCUUGUAGUUUAGUAUGACACUCGUGUCCUUAUAAUUUUCUAAUUGUUAAUUUGUUGUGGUAAUACUUGAUUCAGAAGUGUUGGAAUGUGGUGAAAGAGGGUCAGAGUCAGACCAUCCUAUGUUAAAUGACCACUGCAAAAGGGGUGA",
    "Dâu tây": "CCUGGUUUUUGCGAUCAGCGAGGUAUAGAGUUCCUACGUUCAUUAUAAAUUCGUAGGAACUUCAUACUGUGCUCUUUGUAGACAAAAAAACAAACAAGCCUGGUUUUUGCCAUCAGCGUGGAAUAGAGUUCGUACGUACAUUAUGAACUCGGAGGAACUUCAGACCGUGCUCUUGGAAGACCAAAAAACAAACAAG"
}

# Hàm kiểm tra nếu hai loài thuộc cùng một họ
def is_same_group(species1, species2):
    groups = {
        "Họ Người (Hominidae)": ["Con người", "Con tinh tinh"],
        "Họ Chó (Canidae)": ["Con chó nhà", "Sói sám"],
        "Họ Mèo (Felidae)": ["Hổ", "Mèo"],
        "Họ Hà mã (Hippopotamidae)": ["Hà mã"],
        "Họ Cá voi (Physeteridae)": ["Cá nhà táng"],
        "Họ Hoa hồng (Rosaceae)": ["Hoa hồng", "Dâu tây"]
    }
    for group_name, group_species in groups.items():
        if species1 in group_species and species2 in group_species:
            return True, group_name
    return False, None

# Hàm tìm độ dài chuỗi con chung dài nhất bằng thuật toán backtracking
def lcs_backtracking(seq1, seq2):
    m, n = len(seq1), len(seq2)
    max_length = 0

    def backtrack(i, j, current_length):
        nonlocal max_length
        if i == m or j == n:
            max_length = max(max_length, current_length)
            return

        if seq1[i] == seq2[j]:
            backtrack(i + 1, j + 1, current_length + 1)
        else:
            max_length = max(max_length, current_length)
            backtrack(i + 1, j, 0)
            backtrack(i, j + 1, 0)

    backtrack(0, 0, 0)
    return max_length

# Hàm tính toán độ tương đồng dựa trên độ dài chuỗi con chung dài nhất
def calculate_similarity(seq1, seq2):
    lcs_length = lcs_backtracking(seq1, seq2)
    similarity = (lcs_length / min(len(seq1), len(seq2))) * 100
    return similarity

# Giao diện Streamlit
# Giao diện Streamlit
st.markdown("<div class='title'>Xác định tổ tiên chung qua so sánh chuỗi ADN và RNA</div>", unsafe_allow_html=True)
st.write("<div class='subtitle'>Chọn hai loài để bắt đầu so sánh</div>", unsafe_allow_html=True)

species_options = list(adn_sequences.keys())
species1 = st.selectbox("Chọn loài thứ nhất", species_options)
species2 = st.selectbox("Chọn loài thứ hai", species_options)

# Thêm lựa chọn để so sánh ADN hay RNA
comparison_type = st.selectbox("Chọn loại so sánh:", ["ADN", "RNA"])

# Hiển thị chuỗi ADN hoặc RNA của loài đã chọn
cols = st.columns(2)

if comparison_type == "ADN":
    cols[0].code(f"ADN của {species1}:\n{adn_sequences[species1]}", language="plaintext")
    cols[1].code(f"ADN của {species2}:\n{adn_sequences[species2]}", language="plaintext")
else:
    cols[0].code(f"RNA của {species1}:\n{rna_sequences[species1]}", language="plaintext")
    cols[1].code(f"RNA của {species2}:\n{rna_sequences[species2]}", language="plaintext")

# Kiểm tra nếu hai loài thuộc cùng nhóm
same_group, group = is_same_group(species1, species2)

# Thực hiện so sánh nếu có cùng nhóm
st.write("## Kết quả so sánh")
if st.button("Xác định tổ tiên chung"):
    if species1 != species2:
        if comparison_type == "ADN":
            similarity = calculate_similarity(adn_sequences[species1], adn_sequences[species2])
        else:
            similarity = calculate_similarity(rna_sequences[species1], rna_sequences[species2])

        if similarity >= 80:
            if same_group:
                result = f"{species1} và {species2} thuộc cùng bộ '{group}' và có tổ tiên chung, với độ tương đồng {similarity:.2f}%."
                st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)
            else:
                result = f"{species1} và {species2} có độ tương đồng cao ({similarity:.2f}%), nhưng không thuộc cùng một bộ tiến hóa."
                st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)
        else:
            st.warning(f"Độ tương đồng giữa {species1} và {species2} là {similarity:.2f}%. Không đủ để xác định tổ tiên chung.")
    else:
        st.warning("Vui lòng chọn hai loài khác nhau để so sánh.")

# Hàm xác định tổ tiên chung
def find_common_ancestor(species1, species2):
    if same_group:
        return f"Tổ tiên chung của {species1} và {species2} là tổ tiên của bộ '{group}'."
    else:
        return "Không thể xác định tổ tiên chung do hai loài không thuộc cùng một bộ."

# Hiển thị thông tin tổ tiên chung
if st.button("Tìm tổ tiên chung"):
    ancestor_info = find_common_ancestor(species1, species2)
    st.markdown(f"<div class='result'>{ancestor_info}</div>", unsafe_allow_html=True)


