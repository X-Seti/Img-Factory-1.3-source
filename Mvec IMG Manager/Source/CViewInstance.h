#ifndef CViewInstance_H
#define CViewInstance_H

#include <string>
#include <vector>

struct CIMGFile;
struct CIMGEntry;

struct CFilterOptions
{
	CFilterOptions(void)
	{
		m_bCheckboxes[0] = false;
		m_bCheckboxes[1] = false;
		m_bCheckboxes[2] = false;
		m_iComboBoxes[0] = -1;
		m_iComboBoxes[1] = -1;
		m_iComboBoxes[2] = -1;
		m_strEditBoxes[0] = "";
		m_strEditBoxes[1] = "";
	};

	bool						m_bCheckboxes[3];
	unsigned long				m_iComboBoxes[3];
	std::string					m_strEditBoxes[2];
};

bool							sortIMGEntries(CIMGEntry *p1, CIMGEntry *p2);

class CViewInstance
{
public:
	CViewInstance(void) :
		m_bRestoringFilterOptions(false)
	{};

	void						unload(void);

	void						setIMGFile(CIMGFile *pIMGFile) { m_pIMGFile = pIMGFile; }
	CIMGFile*					getIMGFile(void) { return m_pIMGFile; }

	void						setIndex(unsigned long uiIndex) { m_uiIndex = uiIndex; }
	unsigned long				getIndex(void) { return m_uiIndex; }

	void						setSearchText(std::string strSearchText) { m_strSearchText = strSearchText; }
	std::string					getSearchText(void) { return m_strSearchText; }

	bool						isRestoringFilterOptions(void) { return m_bRestoringFilterOptions; }

	void						log(std::string strText);
	std::vector<std::string>&	getLogLines(void) { return m_vecLogLines; }

	void						addFile(std::string strPath);
	void						removeFile(CIMGEntry *pIMGEntry);

	void						addIMGEntries(void);
	void						addIMGEntry(CIMGEntry *pIMGEntry);
	void						updateEntryCount(void);

	void						rebuild(std::string strIMGPath = "");
	void						merge(std::string strPath);
	void						split(std::string strPath);
	void						replace(std::vector<std::string>& vecPaths);
	void						searchText(void);

	void						storeFilterOptions(void);
	void						restoreFilterOptions(void);

	void						loadSortOptionsFromMenu(void);
	void						sortEntries(void);

private:
	unsigned long				m_uiIndex;
	CIMGFile*					m_pIMGFile;
	std::vector<std::string>	m_vecLogLines;
	std::string					m_strSearchText;
	CFilterOptions				m_filterOptions;
	bool						m_bRestoringFilterOptions;
};

#endif