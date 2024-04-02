import streamlit as st
import prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from jugaad_data.nse import stock_df, bhavcopy_save
from datetime import date
import pandas as pd
import yfinance as yf

#  SETTING TODAY DATE
today = date.today()
today_date = today.strftime("%d/%m/%Y").split("/")
YEAR = int(today_date[2])
DATE1 = int(today_date[0])
MONTH = int(today_date[1])
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


def plot_raw_data(stock_date, stock_open, stock_close):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[stock_date], y=df[stock_open], name="stock_open"))
    fig.add_trace(go.Scatter(x=df[stock_date], y=df[stock_close], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


def indian_stock():
    ind_stock = ['20MICRONS', '21STCENMGM', '3IINFOLTD', '3MINDIA', '3PLAND', '5PAISA', '610GS2031', '63MOONS', '654GS2032', '667GS2050', '676GS2061', '695GS2061', '699GS2051', '710GS2029', '754GS2036', '813GS2045', 'A2ZINFRA', 'AAATECH', 'AAKASH', 'AAREYDRUGS', 'AARON', 'AARTIDRUGS', 'AARTIIND', 'AARTISURF', 'AARVEEDEN', 'AARVI', 'AAVAS', 'ABAN', 'ABB', 'ABBOTINDIA', 'ABCAPITAL', 'ABCOTS', 'ABFRL', 'ABMINTLLTD', 'ABSLAMC', 'ABSLBANETF', 'ABSLNN50ET', 'ACC', 'ACCELYA', 'ACCORD', 'ACCURACY', 'ACE', 'ACEINTEG', 'ACRYSIL', 'ADANIENT', 'ADANIGREEN', 'ADANIPORTS', 'ADANIPOWER', 'ADANITRANS', 'ADFFOODS', 'ADL', 'ADORWELD', 'ADROITINFO', 'ADSL', 'ADVANIHOTR', 'ADVENZYMES', 'AEGISCHEM', 'AETHER', 'AFFLE', 'AGARIND', 'AGI', 'AGRITECH', 'AGROPHOS', 'AGSTRA', 'AHLADA', 'AHLEAST', 'AHLUCONT', 'AIAENG', 'AIRAN', 'AIROLAM', 'AIRTELPP', 'AJANTPHARM', 'AJMERA', 'AJOONI', 'AJRINFRA', 'AKASH', 'AKG', 'AKSHAR', 'AKSHARCHEM', 'AKSHOPTFBR', 'AKZOINDIA', 'ALANKIT', 'ALBERTDAVD', 'ALEMBICLTD', 'ALICON', 'ALKALI', 'ALKEM', 'ALKYLAMINE', 'ALLCARGO', 'ALLSEC', 'ALMONDZ', 'ALOKINDS', 'ALPA', 'ALPHAGEO', 'ALPSINDUS', 'AMARAJABAT', 'AMBANIORG', 'AMBER', 'AMBICAAGAR', 'AMBIKCO', 'AMBUJACEM', 'AMDIND', 'AMIORG', 'AMJLAND', 'AMRUTANJAN', 'ANANDRATHI', 'ANANTRAJ', 'ANDHRACEMT', 'ANDHRAPAP', 'ANDHRSUGAR', 'ANDREWYU', 'ANGELONE', 'ANIKINDS', 'ANKITMETAL', 'ANMOL', 'ANSALAPI', 'ANSALHSG', 'ANTGRAPHIC', 'ANUP', 'ANURAS', 'APARINDS', 'APCL', 'APCOTEXIND', 'APEX', 'APLAPOLLO', 'APLLTD', 'APOLLO', 'APOLLOHOSP', 'APOLLOPIPE', 'APOLLOTYRE', 'APOLSINHOT', 'APTECHT', 'APTUS', 'ARCHIDPLY', 'ARCHIES', 'ARENTERP', 'ARIES', 'ARIHANTCAP', 'ARIHANTSUP', 'ARMANFIN', 'AROGRANITE', 'ARROWGREEN', 'ARSHIYA', 'ARSSINFRA', 'ARTEMISMED', 'ARTNIRMAN', 'ARVEE', 'ARVIND', 'ARVINDFASN', 'ARVSMART', 'ASAHIINDIA', 'ASAHISONG', 'ASAL', 'ASALCBR', 'ASCOM', 'ASHAPURMIN', 'ASHIANA', 'ASHIMASYN', 'ASHOKA', 'ASHOKLEY', 'ASIANENE', 'ASIANHOTNR', 'ASIANPAINT', 'ASIANTILES', 'ASPINWALL', 'ASTEC', 'ASTERDM', 'ASTRAL', 'ASTRAMICRO', 'ASTRAZEN', 'ASTRON', 'ATALREAL', 'ATFL', 'ATGL', 'ATLANTA', 'ATUL', 'ATULAUTO', 'AUBANK', 'AURIONPRO', 'AUROPHARMA', 'AURUM', 'AURUMPP', 'AUSOMENT', 'AUTOAXLES', 'AUTOBEES', 'AUTOIND', 'AVADHSUGAR', 'AVANTIFEED', 'AVROIND', 'AVSL', 'AVTNPL', 'AWHCL', 'AWL', 'AXISBANK', 'AXISBNKETF', 'AXISBPSETF', 'AXISCADES', 'AXISCETF', 'AXISGOLD', 'AXISHCETF', 'AXISNIFTY', 'AXISTECETF', 'AXITA', 'AYMSYNTEX', 'BAFNAPH', 'BAGFILMS', 'BAJAJ-AUTO', 'BAJAJCON', 'BAJAJELEC', 'BAJAJFINSV', 'BAJAJHCARE', 'BAJAJHIND', 'BAJAJHLDNG', 'BAJFINANCE', 'BALAJITELE', 'BALAMINES', 'BALAXI', 'BALKRISHNA', 'BALKRISIND', 'BALMLAWRIE', 'BALPHARMA', 'BALRAMCHIN', 'BANARBEADS', 'BANARISUG', 'BANCOINDIA', 'BANDHANBNK', 'BANG', 'BANKA', 'BANKBARODA', 'BANKBEES', 'BANKINDIA', 'BANSWRAS', 'BARBEQUE', 'BARTRONICS', 'BASF', 'BASML', 'BATAINDIA', 'BAYERCROP', 'BBETF0432', 'BBL', 'BBOX', 'BBTC', 'BCG', 'BCLIND', 'BCONCEPTS', 'BCP', 'BDL', 'BEARDSELL', 'BECTORFOOD', 'BEDMUTHA', 'BEL', 'BEML', 'BEPL', 'BERGEPAINT', 'BESTAGRO', 'BETA', 'BFINVEST', 'BFUTILITIE', 'BGRENERGY', 'BHAGCHEM', 'BHAGERIA', 'BHAGYANGR', 'BHAGYAPROP', 'BHANDARI', 'BHARATFORG', 'BHARATGEAR', 'BHARATRAS', 'BHARATWIRE', 'BHARTIARTL', 'BHEL', 'BIGBLOC', 'BIL', 'BINDALAGRO', 'BIOCON', 'BIOFILCHEM', 'BIRET', 'BIRLACABLE', 'BIRLACORPN', 'BIRLAMONEY', 'BKMINDST', 'BLBLIMITED', 'BLISSGVS', 'BLKASHYAP', 'BLS', 'BLUEDART', 'BLUESTARCO', 'BODALCHEM', 'BOMDYEING', 'BOROLTD', 'BORORENEW', 'BOSCHLTD', 'BPCL', 'BPL', 'BRIGADE', 'BRIGHT', 'BRITANNIA', 'BRITANNIA', 'BRITANNIA', 'BRNL', 'BROOKS', 'BSE', 'BSHSL', 'BSL', 'BSLGOLDETF', 'BSLNIFTY', 'BSLSENETFG', 'BSOFT', 'BTML', 'BURNPUR', 'BUTTERFLY', 'BVCL', 'BYKE', 'CADSYS', 'CALSOFT', 'CAMLINFINE', 'CAMPUS', 'CAMS', 'CANBK', 'CANDC', 'CANFINHOME', 'CANTABIL', 'CAPACITE', 'CAPLIPOINT', 'CAPTRUST', 'CARBORUNIV', 'CAREERP', 'CARERATING', 'CARTRADE', 'CASTROLIND', 'CCCL', 'CCHHL', 'CCL', 'CDSL', 'CEATLTD', 'CELEBRITY', 'CENTENKA', 'CENTEXT', 'CENTRALBK', 'CENTRUM', 'CENTUM', 'CENTURYPLY', 'CENTURYTEX', 'CERA', 'CEREBRAINT', 'CESC', 'CGCL', 'CGPOWER', 'CHALET', 'CHAMBLFERT', 'CHEMBOND', 'CHEMCON', 'CHEMFAB', 'CHEMPLASTS', 'CHENNPETRO', 'CHEVIOT', 'CHOICEIN', 'CHOLAFIN', 'CHOLAHLDNG', 'CIGNITITEC', 'CINELINE', 'CINEVISTA', 'CIPLA', 'CLEAN', 'CLEDUCATE', 'CLNINDIA', 'CLSEL', 'CMICABLES', 'CMMIPL', 'CMSINFO', 'COALINDIA', 'COASTCORP', 'COCHINSHIP', 'COFFEEDAY', 'COFORGE', 'COLPAL', 'COMPINFO', 'COMPUSOFT', 'CONCOR', 'CONFIPET', 'CONSOFINVT', 'CONSUMBEES', 'CONTROLPR', 'COOLCAPS', 'CORALFINAC', 'CORDSCABLE', 'COROMANDEL', 'COSMOFILMS', 'COUNCODOS', 'CPSEETF', 'CRAFTSMAN', 'CREATIVE', 'CREATIVEYE', 'CREDITACC', 'CREST', 'CRISIL', 'CROMPTON', 'CROWN', 'CSBBANK', 'CTE', 'CUB', 'CUBEXTUB', 'CUMMINSIND', 'CUPID', 'CYBERMEDIA', 'CYBERTECH', 'CYIENT', 'DAAWAT', 'DABUR', 'DALBHARAT', 'DALMIASUG', 'DAMODARIND', 'DANGEE', 'DATAMATICS', 'DATAPATTNS', 'DBCORP', 'DBL', 'DBREALTY', 'DBSTOCKBRO', 'DCAL', 'DCBBANK', 'DCM', 'DCMFINSERV', 'DCMNVL', 'DCMSHRIRAM', 'DCMSRIND', 'DCW', 'DECCANCE', 'DEEPAKFERT', 'DEEPAKNTR', 'DEEPENR', 'DEEPINDS', 'DELHIVERY', 'DELPHIFX', 'DELTACORP', 'DELTAMAGNT', 'DEN', 'DENORA', 'DEVIT', 'DEVYANI', 'DFMFOODS', 'DGCONTENT', 'DHAMPURSUG', 'DHANBANK', 'DHANI', 'DHANILOANS', 'DHANILOANS', 'DHANILOANS', 'DHANILOANS', 'DHANILOANS', 'DHANILOANS', 'DHANUKA', 'DHANVARSHA', 'DHARAMSI', 'DHARSUGAR', 'DHRUV', 'DHUNINV', 'DIAMONDYD', 'DICIND', 'DIGISPICE', 'DIGJAMLMTD', 'DIL', 'DISHTV', 'DIVISLAB', 'DIVOPPBEES', 'DIXON', 'DLF', 'DLINKINDIA', 'DMART', 'DNAMEDIA', 'DODLA', 'DOLATALGO', 'DOLLAR', 'DONEAR', 'DPABHUSHAN', 'DPSCLTD', 'DPWIRES', 'DRCSYSTEMS', 'DREDGECORP', 'DRREDDY', 'DSPN50ETF', 'DSPNEWETF', 'DSPQ50ETF', 'DSSL', 'DTIL', 'DUCON', 'DVL', 'DWARKESH', 'DYNAMATECH', 'DYNAMIC', 'DYNPRO', 'DYNPROPP', 'E2E', 'EASEMYTRIP', 'EASTSILK', 'EASUNREYRL', 'EBBETF0423', 'EBBETF0425', 'EBBETF0430', 'EBBETF0431', 'EC5RG', 'ECLERX', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'ECLFINANCE', 'EDELWEISS', 'EDUCOMP', 'EHFLNCD', 'EHFLNCD', 'EICHERMOT', 'EIDPARRY', 'EIFFL', 'EIHAHOTELS', 'EIHOTEL', 'EIMCOELECO', 'EKC', 'ELDEHSG', 'ELECON', 'ELECTCAST', 'ELECTHERM', 'ELGIEQUIP', 'ELGIRUBCO', 'EMAMILTD', 'EMAMIPAP', 'EMAMIREAL', 'EMBASSY', 'EMKAY', 'EMMBI', 'EMUDHRA', 'ENDURANCE', 'ENERGYDEV', 'ENGINERSIN', 'ENIL', 'EPL', 'EQUIPPP', 'EQUITAS', 'EQUITASBNK', 'ERFLNCDI', 'ERFLNCDI', 'ERIS', 'EROSMEDIA', 'ESABINDIA', 'ESCORTS', 'ESSARSHPNG', 'ESSENTIA', 'ESTER', 'ETHOSLTD', 'EUROBOND', 'EVEREADY', 'EVERESTIND', 'EXCEL', 'EXCELINDUS', 'EXIDEIND', 'EXPLEOSOL', 'EXXARO', 'FACT', 'FAIRCHEMOR', 'FCL', 'FCONSUMER', 'FCSSOFT', 'FDC', 'FEDERALBNK', 'FEL', 'FELDVR', 'FELIX', 'FIBERWEB', 'FIDEL', 'FIEMIND', 'FILATEX', 'FINCABLES', 'FINEORG', 'FINOPB', 'FINPIPE', 'FLEXITUFF', 'FLFL', 'FLUOROCHEM', 'FMGOETZE', 'FMNL', 'FOCUS', 'FOODSIN', 'FORCEMOT', 'FORTIS', 'FOSECOIND', 'FRETAIL', 'FSC', 'FSL', 'GABRIEL', 'GAEL', 'GAIL', 'GAL', 'GALAXYSURF', 'GALLANTT', 'GANDHITUBE', 'GANECOS', 'GANESHBE', 'GANESHHOUC', 'GANGAFORGE', 'GANGESSECU', 'GARFIBRES', 'GATEWAY', 'GATI', 'GAYAHWS', 'GAYAPROJ', 'GEECEE', 'GEEKAYWIRE', 'GENCON', 'GENESYS', 'GENUSPAPER', 'GENUSPOWER', 'GEOJITFSL', 'GEPIL', 'GESHIP', 'GET&D', 'GFLLIMITED', 'GFSTEELS', 'GHCL', 'GICHSGFIN', 'GICL', 'GICRE', 'GILLANDERS', 'GILLETTE', 'GILT5YBEES', 'GINNIFILA', 'GIPCL', 'GKWLIMITED', 'GLAND', 'GLAXO', 'GLENMARK', 'GLFL', 'GLOBAL', 'GLOBALVECT', 'GLOBE', 'GLOBUSSPR', 'GLS', 'GMBREW', 'GMDCLTD', 'GMMPFAUDLR', 'GMRINFRA', 'GMRP&UI', 'GNA', 'GNFC', 'GOACARBON', 'GOCLCORP', 'GOCOLORS', 'GODFRYPHLP', 'GODHA', 'GODREJAGRO', 'GODREJCP', 'GODREJIND', 'GODREJPROP', 'GOENKA', 'GOKEX', 'GOKUL', 'GOKULAGRO', 'GOLDBEES', 'GOLDENTOBC', 'GOLDIAM', 'GOLDSHARE', 'GOLDTECH', 'GOODLUCK', 'GOODYEAR', 'GPIL', 'GPPL', 'GPTINFRA', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GRAUWEIL', 'GRAVITA', 'GREAVESCOT', 'GREENLAM', 'GREENPANEL', 'GREENPLY', 'GREENPOWER', 'GRINDWELL', 'GRINFRA', 'GROBTEA', 'GRPLTD', 'GRSE', 'GRWRHITECH', 'GSCLCEMENT', 'GSFC', 'GSPL', 'GSS', 'GTL', 'GTLINFRA', 'GTPL', 'GUFICBIO', 'GUJALKALI', 'GUJAPOLLO', 'GUJGASLTD', 'GUJRAFFIA', 'GULFOILLUB', 'GULFPETRO', 'GULPOLY', 'HAL', 'HAPPSTMNDS', 'HARDWYN', 'HARIOMPIPE', 'HARRMALAYA', 'HATHWAY', 'HATSUN', 'HAVELLS', 'HAVISHA', 'HBANKETF', 'HBLPOWER', 'HBSL', 'HCC', 'HCG', 'HCL-INSYS', 'HCLTECH', 'HDFC', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HDFCMFGETF', 'HDFCNIFETF', 'HDFCSENETF', 'HDIL', 'HEALTHY', 'HECPROJECT', 'HEG', 'HEIDELBERG', 'HEMIPROP', 'HERANBA', 'HERCULES', 'HERITGFOOD', 'HEROMOTOCO', 'HESTERBIO', 'HEXATRADEX', 'HFCL', 'HGINFRA', 'HGS', 'HIKAL', 'HIL', 'HILTON', 'HIMATSEIDE', 'HINDALCO', 'HINDCOMPOS', 'HINDCON', 'HINDCOPPER', 'HINDMOTORS', 'HINDOILEXP', 'HINDPETRO', 'HINDUNILVR', 'HINDWAREAP', 'HINDZINC', 'HIRECT', 'HISARMETAL', 'HITECH', 'HITECHCORP', 'HITECHGEAR', 'HLEGLAS', 'HLVLTD', 'HMT', 'HMVL', 'HNDFDS', 'HNGSNGBEES', 'HOMEFIRST', 'HONAUT', 'HONDAPOWER', 'HOVS', 'HPAL', 'HPL', 'HSCL', 'HTMEDIA', 'HUBTOWN', 'HUDCO', 'HUDCO', 'HUDCO', 'HUDCO', 'HUDCO', 'HUDCO', 'HUHTAMAKI', 'IBMFNIFTY', 'IBREALEST', 'IBUCCREDIT', 'IBUCCREDIT', 'IBUCCREDIT', 'IBULHSGFIN', 'IBULHSGFIN', 'IBULHSGFIN', 'IBULHSGFIN', 'IBULHSGFIN', 'IBULHSGFIN', 'IBULHSGFIN', 'ICDSLTD', 'ICEMAKE', 'ICICI500', 'ICICI5GSEC', 'ICICIALPLV', 'ICICIAUTO', 'ICICIB22', 'ICICIBANK', 'ICICIBANKN', 'ICICIBANKP', 'ICICICONSU', 'ICICIFMCG', 'ICICIGI', 'ICICIGOLD', 'ICICILIQ', 'ICICILOVOL', 'ICICIM150', 'ICICIMCAP', 'ICICINF100', 'ICICINIFTY', 'ICICINV20', 'ICICINXT50', 'ICICIPHARM', 'ICICIPRULI', 'ICICISENSX', 'ICICISILVE', 'ICICITECH', 'ICIL', 'ICRA', 'IDBI', 'IDBIGOLD', 'IDEA', 'IDFC', 'IDFCFIRSTB', 'IDFNIFTYET', 'IEX', 'IFBAGRO', 'IFBIND', 'IFCI', 'IFCI', 'IFGLEXPOR', 'IGARASHI', 'IGL', 'IGPL', 'IIFCL', 'IIFCL', 'IIFL', 'IIFL', 'IIFL', 'IIFL', 'IIFL', 'IIFL', 'IIFL', 'IIFL', 'IIFLSEC', 'IIFLWAM', 'IIHFL', 'IIHFL', 'IIHFL', 'IIHFL', 'IIHFL', 'IITL', 'IL&FSENGG', 'IL&FSTRANS', 'IMAGICAA', 'IMFA', 'IMPAL', 'IMPEXFERRO', 'INCREDIBLE', 'INDBANK', 'INDHOTEL', 'INDIACEM', 'INDIAGLYCO', 'INDIAMART', 'INDIANB', 'INDIANCARD', 'INDIANHUME', 'INDIGO', 'INDIGOPNTS', 'INDIGRID', 'INDIGRID', 'INDIGRID', 'INDIGRID', 'INDLMETER', 'INDNIPPON', 'INDOAMIN', 'INDOBORAX', 'INDOCO', 'INDORAMA', 'INDOSTAR', 'INDOTECH', 'INDOTHAI', 'INDOWIND', 'INDRAMEDCO', 'INDSWFTLAB', 'INDSWFTLTD', 'INDTERRAIN', 'INDUSINDBK', 'INDUSTOWER', 'INEOSSTYRO', 'INFIBEAM', 'INFOBEAN', 'INFOMEDIA', 'INFRABEES', 'INFY', 'INGERRAND', 'INNOVANA', 'INNOVATIVE', 'INOXLEISUR', 'INOXWIND', 'INSECTICID', 'INSPIRISYS', 'INTELLECT', 'INTENTECH', 'INTLCONV', 'INVENTURE', 'IOB', 'IOC', 'IOLCP', 'IONEXCHANG', 'IPCALAB', 'IPL', 'IRB', 'IRBINVIT', 'IRCON', 'IRCTC', 'IREDA', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRFC', 'IRIS', 'IRISDOREME', 'ISEC', 'ISFT', 'ISGEC', 'ISMTLTD', 'ITBEES', 'ITC', 'ITDC', 'ITDCEM', 'ITI', 'IVC', 'IVP', 'IVZINGOLD', 'IVZINNIFTY', 'IWEL', 'IZMO', 'J&KBANK', 'JAGRAN', 'JAGSNPHARM', 'JAIBALAJI', 'JAICORPLTD', 'JAINSTUDIO', 'JAIPURKURT', 'JAMNAAUTO', 'JASH', 'JAYAGROGN', 'JAYBARMARU', 'JAYNECOIND', 'JAYSREETEA', 'JBCHEPHARM', 'JBFIND', 'JBMA', 'JCHAC', 'JETAIRWAYS', 'JETFREIGHT', 'JHS', 'JINDALPHOT', 'JINDALPOLY', 'JINDALSAW', 'JINDALSTEL', 'JINDRILL', 'JINDWORLD', 'JISLDVREQS', 'JISLJALEQS', 'JITFINFRA', 'JKCEMENT', 'JKIL', 'JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMA', 'JMCPROJECT', 'JMFINANCIL', 'JNPT', 'JOCIL', 'JPASSOCIAT', 'JPINFRATEC', 'JPOLYINVST', 'JPPOWER', 'JSL', 'JSLHISAR', 'JSWENERGY', 'JSWHL', 'JSWISPL', 'JSWSTEEL', 'JTEKTINDIA', 'JTLINFRA', 'JUBLFOOD', 'JUBLINDS', 'JUBLINGREA', 'JUBLPHARMA', 'JUNIORBEES', 'JUSTDIAL', 'JWL', 'JYOTHYLAB', 'JYOTISTRUC', 'KABRAEXTRU', 'KAJARIACER', 'KAKATCEM', 'KALPATPOWR', 'KALYANIFRG', 'KALYANKJIL', 'KAMATHOTEL', 'KAMDHENU', 'KANANIIND', 'KANORICHEM', 'KANPRPLA', 'KANSAINER', 'KAPSTON', 'KARMAENG', 'KARURVYSYA', 'KAUSHALYA', 'KAVVERITEL', 'KAYA', 'KBCGLOBAL', 'KCK', 'KCP', 'KCPSUGIND', 'KDDL', 'KEC', 'KECL', 'KEEPLEARN', 'KEERTI', 'KEI', 'KELLTONTEC', 'KENNAMET', 'KERNEX', 'KESORAMIND', 'KEYFINSERV', 'KHADIM', 'KHAICHEM', 'KHAITANLTD', 'KHANDSE', 'KICL', 'KILITCH', 'KIMS', 'KINGFA', 'KIOCL', 'KIRIINDUS', 'KIRLFER', 'KIRLOSBROS', 'KIRLOSENG', 'KIRLOSIND', 'KITEX', 'KKCL', 'KMSUGAR', 'KNAGRI', 'KNRCON', 'KOHINOOR', 'KOKUYOCMLN', 'KOLTEPATIL', 'KOPRAN', 'KOTAKALPHA', 'KOTAKBANK', 'KOTAKBKETF', 'KOTAKGOLD', 'KOTAKIT', 'KOTAKLOVOL', 'KOTAKMID50', 'KOTAKNIFTY', 'KOTAKNV20', 'KOTAKPSUBK', 'KOTARISUG', 'KOTHARIPET', 'KOTHARIPRO', 'KOTYARK', 'KOVAI', 'KPIGREEN', 'KPITTECH', 'KPRMILL', 'KRBL', 'KREBSBIO', 'KRIDHANINF', 'KRISHANA', 'KRISHIVAL', 'KRISHNADEF', 'KRITI', 'KRITIKA', 'KRSNAA', 'KSB', 'KSCL', 'KSHITIJPOL', 'KSL', 'KSOLVES', 'KTKBANK', 'KUANTUM', 'L&TFH', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'L&TFINANCE', 'LAGNAM', 'LAKPRE', 'LALPATHLAB', 'LAMBODHARA', 'LANCER', 'LAOPALA', 'LASA', 'LATENTVIEW', 'LATTEYS', 'LAURUSLABS', 'LAXMICOT', 'LAXMIMACH', 'LCCINFOTEC', 'LEMERITE', 'LEMONTREE', 'LEXUS', 'LFIC', 'LGBBROSLTD', 'LGBFORGE', 'LIBAS', 'LIBERTSHOE', 'LICHSGFIN', 'LICI', 'LICNETFGSC', 'LICNETFN50', 'LICNETFSEN', 'LICNFNHGP', 'LIKHITHA', 'LINC', 'LINCOLN', 'LINDEINDIA', 'LIQUIDBEES', 'LIQUIDETF', 'LODHA', 'LOKESHMACH', 'LOTUSEYE', 'LOVABLE', 'LPDC', 'LSIL', 'LT', 'LTGILTBEES', 'LTI', 'LTTS', 'LUMAXIND', 'LUMAXTECH', 'LUPIN', 'LUXIND', 'LXCHEM', 'LYKALABS', 'LYPSAGEMS', 'M&M', 'M&MFIN', 'M&MFIN', 'M17RG', 'MAANALU', 'MACPOWER', 'MADHAV', 'MADHAVBAUG', 'MADHUCON', 'MADRASFERT', 'MAESGETF', 'MAFANG', 'MAFSETF', 'MAGADSUGAR', 'MAGNUM', 'MAHABANK', 'MAHAPEXLTD', 'MAHASTEEL', 'MAHEPC', 'MAHESHWARI', 'MAHINDCIE', 'MAHKTECH', 'MAHLIFE', 'MAHLOG', 'MAHSCOOTER', 'MAHSEAMLES', 'MAITHANALL', 'MALLCOM', 'MALUPAPER', 'MAM150ETF', 'MAMFGETF', 'MAN50ETF', 'MANAKALUCO', 'MANAKCOAT', 'MANAKSIA', 'MANAKSTEEL', 'MANALIPETC', 'MANAPPURAM', 'MANGALAM', 'MANGCHEFER', 'MANGLMCEM', 'MANINDS', 'MANINFRA', 'MANORAMA', 'MANORG', 'MANUGRAPH', 'MANXT50', 'MANYAVAR', 'MAPMYINDIA', 'MARALOVER', 'MARATHON', 'MARICO', 'MARINE', 'MARKSANS', 'MARSHALL', 'MARUTI', 'MASFIN', 'MASKINVEST', 'MASPTOP50', 'MASTEK', 'MATRIMONY', 'MAWANASUG', 'MAXHEALTH', 'MAXIND', 'MAXVIL', 'MAYURUNIQ', 'MAZDA', 'MAZDOCK', 'MBAPL', 'MBECL', 'MBLINFRA', 'MC2RG', 'MCDOWELL-N', 'MCL', 'MCLEODRUSS', 'MCX', 'MEDICAMEQ', 'MEDICO', 'MEDPLUS', 'MEGASOFT', 'MEGASTAR', 'MELSTAR', 'MENONBE', 'MEP', 'MERCATOR', 'METALFORGE', 'METROBRAND', 'METROPOLIS', 'MFL', 'MFSL', 'MGEL', 'MGL', 'MHHL', 'MHLXMIRU', 'MHRIL', 'MICEL', 'MID150BEES', 'MIDHANI', 'MINDACORP', 'MINDAIND', 'MINDSPACE', 'MINDTECK', 'MINDTREE', 'MIRCELECTR', 'MIRZAINT', 'MITCON', 'MITTAL', 'MKPL', 'MMFL', 'MMP', 'MMTC', 'MODIRUBBER', 'MODISNME', 'MOGSEC', 'MOHITIND', 'MOIL', 'MOKSH', 'MOL', 'MOLDTECH', 'MOLDTKPAC', 'MOLOWVOL', 'MOM100', 'MOM50', 'MOMOMENTUM', 'MON100', 'MONARCH', 'MONQ50', 'MONTECARLO', 'MORARJEE', 'MOREPENLAB', 'MOTHERSON', 'MOTILALOFS', 'MOTOGENFIN', 'MPHASIS', 'MPSLTD', 'MRF', 'MRO-TEK', 'MRPL', 'MSPL', 'MSTCLTD', 'MSUMI', 'MTARTECH', 'MTEDUCARE', 'MTNL', 'MUKANDLTD', 'MUKTAARTS', 'MUNJALAU', 'MUNJALSHOW', 'MURUDCERA', 'MUTHOOTCAP', 'MUTHOOTFIN', 'MWL', 'NABARD', 'NACLIND', 'NAGAFERT', 'NAGREEKCAP', 'NAGREEKEXP', 'NAHARCAP', 'NAHARINDUS', 'NAHARPOLY', 'NAHARSPING', 'NAM-INDIA', 'NATCOPHARM', 'NATHBIOGEN', 'NATIONALUM', 'NAUKRI', 'NAVIFIN', 'NAVINFLUOR', 'NAVKARCORP', 'NAVNETEDUL', 'NAZARA', 'NBCC', 'NBIFIN', 'NBVENTURES', 'NCC', 'NCLIND', 'NDGL', 'NDL', 'NDRAUTO', 'NDTV', 'NECCLTD', 'NECLIFE', 'NELCAST', 'NELCO', 'NEOGEN', 'NESCO', 'NESTLEIND', 'NETF', 'NETWORK18', 'NEULANDLAB', 'NEWGEN', 'NEXTMEDIA', 'NFL', 'NGIL', 'NGLFINE', 'NH', 'NHAI', 'NHAI', 'NHAI', 'NHAI', 'NHAI', 'NHAI', 'NHAI', 'NHAI', 'NHBTF2014', 'NHBTF2014', 'NHPC', 'NHPC', 'NIACL', 'NIBL', 'NIDAN', 'NIF100BEES', 'NIFTYBEES', 'NIITLTD', 'NILAINFRA', 'NILASPACES', 'NILKAMAL', 'NIPPOBATRY', 'NIRAJ', 'NITCO', 'NITINSPIN', 'NITIRAJ', 'NKIND', 'NLCINDIA', 'NMDC', 'NOCIL', 'NOIDATOLL', 'NOVARTIND', 'NPBET', 'NPST', 'NRAIL', 'NRBBEARING', 'NRL', 'NSIL', 'NTPC', 'NTPC', 'NTPC', 'NTPC', 'NUCLEUS', 'NURECA', 'NUVOCO', 'NV20BEES', 'NXTDIGITAL', 'NYKAA', 'OAL', 'OBCL', 'OBEROIRLTY', 'OCCL', 'OFSS', 'OIL', 'OILCOUNTUB', 'OLECTRA', 'OMAXAUTO', 'OMAXE', 'OMINFRAL', 'OMKARCHEM', 'ONELIFECAP', 'ONEPOINT', 'ONGC', 'ONMOBILE', 'ONWARDTEC', 'OPTIEMUS', 'ORBTEXP', 'ORCHPHARMA', 'ORICONENT', 'ORIENTABRA', 'ORIENTALTL', 'ORIENTBELL', 'ORIENTCEM', 'ORIENTELEC', 'ORIENTHOT', 'ORIENTLTD', 'ORIENTPPR', 'ORISSAMINE', 'ORTEL', 'ORTINLAB', 'OSWALAGRO', 'PAGEIND', 'PAISALO', 'PALASHSECU', 'PALREDTEC', 'PANACEABIO', 'PANACHE', 'PANAMAPET', 'PANSARI', 'PAR', 'PARACABLES', 'PARADEEP', 'PARAGMILK', 'PARAS', 'PARSVNATH', 'PARTYCRUS', 'PASHUPATI', 'PASUPTAC', 'PATANJALI', 'PATELENG', 'PATINTLOG', 'PATINTPP', 'PAYTM', 'PBAINFRA', 'PCBL', 'PCHFL', 'PCHFL', 'PCHFL', 'PCJEWELLER', 'PDMJEPAPER', 'PDSL', 'PEARLPOLY', 'PEL', 'PENIND', 'PENINLAND', 'PERSISTENT', 'PETRONET', 'PFC', 'PFC', 'PFC', 'PFC', 'PFIZER', 'PFOCUS', 'PFS', 'PGEL', 'PGHH', 'PGHL', 'PGIL', 'PGINVIT', 'PHARMABEES', 'PHOENIXLTD', 'PIDILITIND', 'PIGL', 'PIIND', 'PILANIINVS', 'PILITA', 'PIONDIST', 'PIONEEREMB', 'PITTIENG', 'PIXTRANS', 'PLASTIBLEN', 'PNB', 'PNBGILTS', 'PNBHOUSING', 'PNC', 'PNCINFRA', 'PODDARHOUS', 'PODDARMENT', 'POKARNA', 'POLICYBZR', 'POLYCAB', 'POLYMED', 'POLYPLEX', 'PONNIERODE', 'POONAWALLA', 'POWERGRID', 'POWERINDIA', 'POWERMECH', 'PPAP', 'PPL', 'PRAENG', 'PRAJIND', 'PRAKASH', 'PRAKASHSTL', 'PRAXIS', 'PRECAM', 'PRECISION', 'PRECOT', 'PRECWIRE', 'PREMEXPLN', 'PREMIER', 'PREMIERPOL', 'PRESSMN', 'PRESTIGE', 'PRICOLLTD', 'PRIMESECU', 'PRINCEPIPE', 'PRITI', 'PRITIKAUTO', 'PRIVISCL', 'PROZONINTU', 'PRSMJOHNSN', 'PRUDENT', 'PSB', 'PSPPROJECT', 'PSUBNKBEES', 'PTC', 'PTL', 'PUNJABCHEM', 'PUNJLLOYD', 'PURVA', 'PVP', 'PVR', 'QGOLDHALF', 'QNIFTY', 'QUADPRO', 'QUESS', 'QUICKHEAL', 'RADAAN', 'RADICO', 'RADIOCITY', 'RAILTEL', 'RAIN', 'RAINBOW', 'RAJESHEXPO', 'RAJMET', 'RAJRATAN', 'RAJSREESUG', 'RAJTV', 'RALLIS', 'RAMANEWS', 'RAMASTEEL', 'RAMCOCEM', 'RAMCOIND', 'RAMCOSYS', 'RAMKY', 'RANASUG', 'RANEENGINE', 'RANEHOLDIN', 'RATEGAIN', 'RATNAMANI', 'RAYMOND', 'RBA', 'RBL', 'RBLBANK', 'RCF', 'RCOM', 'RECLTD', 'RECLTD', 'RECLTD', 'RECLTD', 'RECLTD', 'RECLTD', 'RECLTD', 'RECLTD', 'REDINGTON', 'REFEX', 'REGENCERAM', 'RELAXO', 'RELCAPITAL', 'RELCHEMQ', 'RELIABLE', 'RELIANCE', 'RELIGARE', 'RELINFRA', 'REMSONSIND', 'RENUKA', 'REPCOHOME', 'REPL', 'REPRO', 'RESPONIND', 'REVATHI', 'REXPIPES', 'RGL', 'RHFL', 'RHFL', 'RHIM', 'RICHA', 'RICOAUTO', 'RIIL', 'RILINFRA', 'RITCO', 'RITES', 'RKDL', 'RKEC', 'RKFORGE', 'RMCL', 'RML', 'RNAVAL', 'ROHLTD', 'ROLEXRINGS', 'ROLLT', 'ROLTA', 'ROML', 'ROSSARI', 'ROSSELLIND', 'ROTO', 'ROUTE', 'RPGLIFE', 'RPOWER', 'RPPINFRA', 'RPPL', 'RPSGVENT', 'RSSOFTWARE', 'RSWM', 'RSYSTEMS', 'RTNINDIA', 'RTNPOWER', 'RUBYMILLS', 'RUCHINFRA', 'RUCHIRA', 'RUPA', 'RUSHIL', 'RVHL', 'RVNL', 'SABEVENTS', 'SADBHAV', 'SADBHIN', 'SAFARI', 'SAGARDEEP', 'SAGCEM', 'SAIL', 'SAKAR', 'SAKHTISUG', 'SAKSOFT', 'SAKUMA', 'SALASAR', 'SALONA', 'SALSTEEL', 'SALZERELEC', 'SAMBHAAV', 'SANCO', 'SANDESH', 'SANDHAR', 'SANGAMIND', 'SANGHIIND', 'SANGHVIMOV', 'SANGINITA', 'SANOFI', 'SANSERA', 'SANWARIA', 'SAPPHIRE', 'SARDAEN', 'SAREGAMA', 'SARLAPOLY', 'SARVESHWAR', 'SASKEN', 'SASTASUNDR', 'SATIA', 'SATIN', 'SBC', 'SBCL', 'SBICARD', 'SBIETFCON', 'SBIETFIT', 'SBIETFPB', 'SBIETFQLTY', 'SBILIFE', 'SBIN', 'SCAPDVR', 'SCHAEFFLER', 'SCHAND', 'SCHNEIDER', 'SCI', 'SDBL', 'SDL24BEES', 'SDL26BEES', 'SEAMECLTD', 'SECL', 'SECURKLOUD', 'SEJALLTD', 'SELAN', 'SEPC', 'SEPOWER', 'SEQUENT', 'SERVOTECH', 'SESHAPAPER', 'SETCO', 'SETF10GILT', 'SETFGOLD', 'SETFNIF50', 'SETFNIFBK', 'SETFNN50', 'SETUINFRA', 'SEYAIND', 'SFL', 'SGBAPR28I', 'SGBAUG24', 'SGBAUG27', 'SGBAUG28V', 'SGBAUG29V', 'SGBD29VIII', 'SGBDC27VII', 'SGBFEB24', 'SGBFEB27', 'SGBFEB28IX', 'SGBFEB29XI', 'SGBJ28VIII', 'SGBJAN26', 'SGBJAN29IX', 'SGBJAN29X', 'SGBJAN30IX', 'SGBJU29III', 'SGBJUL27', 'SGBJUL28IV', 'SGBJUL29IV', 'SGBJUN27', 'SGBJUN28', 'SGBJUN29II', 'SGBJUN30', 'SGBMAR24', 'SGBMAR25', 'SGBMAR28X', 'SGBMAR30X', 'SGBMAY25', 'SGBMAY26', 'SGBMAY28', 'SGBMAY29I', 'SGBMR29XII', 'SGBN28VIII', 'SGBNOV23', 'SGBNOV24', 'SGBNV29VII', 'SGBOC28VII', 'SGBOCT25', 'SGBOCT25IV', 'SGBOCT27VI', 'SGBSEP24', 'SGBSEP27', 'SGBSEP28VI', 'SGBSEP29VI', 'SGIL', 'SGL', 'SHAHALLOYS', 'SHAILY', 'SHAKTIPUMP', 'SHALBY', 'SHALPAINTS', 'SHANKARA', 'SHANTI', 'SHANTIGEAR', 'SHARDACROP', 'SHARDAMOTR', 'SHAREINDIA', 'SHARIABEES', 'SHEMAROO', 'SHIGAN', 'SHILPAMED', 'SHIVALIK', 'SHIVAMAUTO', 'SHIVAMILLS', 'SHIVATEX', 'SHK', 'SHOPERSTOP', 'SHRADHA', 'SHREDIGCEM', 'SHREECEM', 'SHREEPUSHK', 'SHREERAMA', 'SHRENIK', 'SHREYANIND', 'SHREYAS', 'SHRIPISTON', 'SHRIRAMCIT', 'SHRIRAMPPS', 'SHUBHLAXMI', 'SHYAMCENT', 'SHYAMMETL', 'SHYAMTEL', 'SICAL', 'SIEMENS', 'SIGACHI', 'SIGIND', 'SIGMA', 'SIKKO', 'SIL', 'SILGO', 'SILINV', 'SILLYMONKS', 'SILVER', 'SILVERBEES', 'SILVERTUC', 'SIMBHALS', 'SIMPLEXINF', 'SINTERCOM', 'SIRCA', 'SIS', 'SITINET', 'SIYSIL', 'SJS', 'SJVN', 'SKFINDIA', 'SKIPPER', 'SKMEGGPROD', 'SKP', 'SMARTLINK', 'SMCGLOBAL', 'SMLISUZU', 'SMLT', 'SMSLIFE', 'SMSPHARMA', 'SNOWMAN', 'SOBHA', 'SOFTTECH', 'SOLARA', 'SOLARINDS', 'SOMANYCERA', 'SOMATEX', 'SOMICONVEY', 'SONACOMS', 'SONAHISONA', 'SONAMCLOCK', 'SONATSOFTW', 'SONUINFRA', 'SORILINFRA', 'SOTL', 'SOUTHBANK', 'SOUTHWEST', 'SPAL', 'SPANDANA', 'SPARC', 'SPCENET', 'SPECIALITY', 'SPENCERS', 'SPENTEX', 'SPIC', 'SPICEJET', 'SPLIL', 'SPLPETRO', 'SPMLINFRA', 'SPRL', 'SPTL', 'SREEL', 'SREINFRA', 'SRF', 'SRHHYPOLTD', 'SRPL', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SRTRANSFIN', 'SSINFRA', 'SSWL', 'STAMPEDE', 'STAR', 'STARCEMENT', 'STARHEALTH', 'STARPAPER', 'STARTECK', 'STCINDIA', 'STEELCAS', 'STEELCITY', 'STEELXIND', 'STEL', 'STERTOOLS', 'STLTECH', 'STOVEKRAFT', 'STYLAMIND', 'SUBCAPCITY', 'SUBEXLTD', 'SUBROS', 'SUDARSCHEM', 'SUMEETINDS', 'SUMICHEM', 'SUMIT', 'SUMMITSEC', 'SUNCLAYLTD', 'SUNDARAM', 'SUNDARMFIN', 'SUNDARMHLD', 'SUNDRMBRAK', 'SUNDRMFAST', 'SUNFLAG', 'SUNPHARMA', 'SUNTECK', 'SUNTV', 'SUPERHOUSE', 'SUPERSPIN', 'SUPRAJIT', 'SUPREMEENG', 'SUPREMEIND', 'SUPREMEINF', 'SUPRIYA', 'SURANASOL', 'SURANAT&P', 'SURYALAXMI', 'SURYAROSNI', 'SURYODAY', 'SUTLEJTEX', 'SUULD', 'SUVEN', 'SUVENPHAR', 'SUVIDHAA', 'SUZLON', 'SVPGLOB', 'SWANENERGY', 'SWARAJ', 'SWARAJENG', 'SWELECTES', 'SWSOLAR', 'SYMPHONY', 'SYNGENE', 'TAINWALCHM', 'TAJGVK', 'TAKE', 'TALBROAUTO', 'TANLA', 'TANTIACONS', 'TARAPUR', 'TARC', 'TARMAT', 'TARSONS', 'TASTYBITE', 'TATACAPHSG', 'TATACAPHSG', 'TATACHEM', 'TATACOFFEE', 'TATACOMM', 'TATACONSUM', 'TATAELXSI', 'TATAINVEST', 'TATAMETALI', 'TATAMOTORS', 'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TATASTLLP', 'TATVA', 'TBZ', 'TCFSL', 'TCFSL', 'TCFSL', 'TCFSL', 'TCI', 'TCIDEVELOP', 'TCIEXP', 'TCNSBRANDS', 'TCPLPACK', 'TCS', 'TDPOWERSYS', 'TEAMLEASE', 'TECH', 'TECHIN', 'TECHM', 'TECHNOE', 'TEGA', 'TEJASNET', 'TEMBO', 'TERASOFT', 'TEXINFRA', 'TEXMOPIPES', 'TEXRAIL', 'TFCILTD', 'TFL', 'TGBHOTELS', 'THANGAMAYL', 'THEINVEST', 'THEJO', 'THEMISMED', 'THERMAX', 'THOMASCOOK', 'THOMASCOTT', 'THYROCARE', 'TI', 'TIDEWATER', 'TIIL', 'TIINDIA', 'TIJARIA', 'TIL', 'TIMESCAN', 'TIMESGTY', 'TIMETECHNO', 'TIMKEN', 'TINPLATE', 'TIPSINDLTD', 'TIRUMALCHM', 'TIRUPATIFL', 'TITAN', 'TMRVL', 'TNIDETF', 'TNPETRO', 'TNPL', 'TNTELE', 'TOKYOPLAST', 'TORNTPHARM', 'TORNTPOWER', 'TOTAL', 'TOUCHWOOD', 'TPLPLASTEH', 'TREEHOUSE', 'TREJHARA', 'TRENT', 'TRIDENT', 'TRIGYN', 'TRIL', 'TRITURBINE', 'TRIVENI', 'TTKHLTCARE', 'TTKPRESTIG', 'TTL', 'TTML', 'TV18BRDCST', 'TVSELECT', 'TVSMOTOR', 'TVSSRICHAK', 'TVTODAY', 'TVVISION', 'TWL', 'UBL', 'UCALFUEL', 'UCOBANK', 'UDAICEMENT', 'UFLEX', 'UFO', 'UGARSUGAR', 'UGROCAP', 'UGROCAP', 'UJAAS', 'UJJIVAN', 'UJJIVANSFB', 'ULTRACEMCO', 'UMAEXPORTS', 'UMANGDAIRY', 'UMESLTD', 'UNICHEMLAB', 'UNIDT', 'UNIENTER', 'UNIINFO', 'UNIONBANK', 'UNITECH', 'UNITEDPOLY', 'UNITEDTEA', 'UNIVASTU', 'UNIVCABLES', 'UNIVPHOTO', 'UPL', 'URJA', 'USHAMART', 'UTIAMC', 'UTIBANKETF', 'UTINEXT50', 'UTINIFTETF', 'UTISENSETF', 'UTISXN50', 'UTTAMSTL', 'UTTAMSUGAR', 'V2RETAIL', 'VADILALIND', 'VAIBHAVGBL', 'VAISHALI', 'VAKRANGEE', 'VALIANTORG', 'VARDHACRLC', 'VARDMNPOLY', 'VARROC', 'VASCONEQ', 'VASWANI', 'VBL', 'VCL', 'VEDL', 'VENKEYS', 'VENUSPIPES', 'VENUSREM', 'VERANDA', 'VERTOZ', 'VESUVIUS', 'VETO', 'VGUARD', 'VHL', 'VICEROY', 'VIDHIING', 'VIJAYA', 'VIJIFIN', 'VIKASECO', 'VIKASLIFE', 'VIKASPROP', 'VIKASWSP', 'VIMTALABS', 'VINATIORGA', 'VINDHYATEL', 'VINEETLAB', 'VINYLINDIA', 'VIPCLOTHNG', 'VIPIND', 'VIPULLTD', 'VISAKAIND', 'VISASTEEL', 'VISESHINFO', 'VISHAL', 'VISHNU', 'VISHWARAJ', 'VIVIDHA', 'VIVIMEDLAB', 'VLSFINANCE', 'VMARCIND', 'VMART', 'VOLTAMP', 'VOLTAS', 'VRLLOG', 'VSSL', 'VSTIND', 'VSTTILLERS', 'VTL', 'WABAG', 'WALCHANNAG', 'WALPAR', 'WANBURY', 'WATERBASE', 'WEALTH', 'WEBELSOLAR', 'WEIZMANIND', 'WELCORP', 'WELENT', 'WELINV', 'WELSPUNIND', 'WENDT', 'WESTLIFE', 'WEWIN', 'WFL', 'WHEELS', 'WHIRLPOOL', 'WILLAMAGOR', 'WINDLAS', 'WINDMACHIN', 'WINPRO', 'WIPL', 'WIPRO', 'WOCKPHARMA', 'WONDERLA', 'WORTH', 'WSTCSTPAPR', 'XCHANGING', 'XELPMOC', 'XPROINDIA', 'YAARI', 'YESBANK', 'YUKEN', 'ZEEL', 'ZEELEARN', 'ZEEMEDIA', 'ZENITHEXPO', 'ZENITHSTL', 'ZENSARTECH', 'ZENTEC', 'ZFCVINDIA', 'ZODIAC', 'ZODIACLOTH', 'ZOMATO', 'ZOTA', 'ZUARI', 'ZUARIIND', 'ZYDUSLIFE', 'ZYDUSWELL']
    selected_stock = st.selectbox("Select stock Symbol", ind_stock, key="<stock_select>")
    data = stock_df(symbol=selected_stock, from_date=date(2018, 1, 1),
                    to_date=date(YEAR, MONTH, DATE1), series="EQ")
    return data


def us_stock():
    us_stocks = ('GOOG', 'AAPL', 'MSFT', 'GME', 'TSLA')
    selected_stock = st.selectbox('Select dataset for prediction', us_stocks, key="<us_stock>")
    return load_data(selected_stock)


def crypto_stock():
    crypto_stocks = ('BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'BNB-USD', 'BUSD-USD', 'XRP-USD')
    selected_stock = st.selectbox('Select dataset for prediction', crypto_stocks, key="<us_stock>")
    return load_data(selected_stock)


# getting stock name and prediction year from user
stock = ["Crypto currency", "Indian Stock", "US Stock"]
st.title('Stock Forecast App')
selected_stock_database = st.selectbox('Select dataset for prediction', stock, key="<database>")

if selected_stock_database == stock[0]:
    df = crypto_stock()
elif selected_stock_database == stock[1]:
    df = indian_stock()
elif selected_stock_database == stock[2]:
    df = us_stock()

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# displaying raw_data

st.subheader('Raw data')
st.write(df.tail(20))


# plotting raw data
if selected_stock_database == stock[1]:
    plot_raw_data(stock_date='DATE', stock_open='OPEN', stock_close='CLOSE')
else:
    plot_raw_data(stock_date='Date', stock_open='Open', stock_close='Close')

# PREDICTION
if selected_stock_database == stock[1]:
    df_train = df[['DATE', 'CLOSE']]
    df_train = df_train.rename(columns={"DATE": "ds", "CLOSE": "y"})
else:
    df_train = df[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})


m = prophet.Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

bitcoin_symbol = [""]