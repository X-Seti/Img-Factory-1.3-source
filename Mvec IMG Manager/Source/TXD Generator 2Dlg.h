
// GTA Tools GUIDlg.h : header file
//

#pragma once

// CGTAToolsGUIDlg dialog
class CGTAToolsGUIDlg : public CDialogEx
{
// Construction
public:
	CGTAToolsGUIDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	enum { IDD = IDD_DIALOG1 };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()

public:
	LRESULT			WindowProc(UINT msg, WPARAM wp, LPARAM lp);
	void			OnDropFiles(HDROP dropInfo);
	afx_msg void	OnNMClickTab1(NMHDR *pNMHDR, LRESULT *pResult);
	afx_msg void	OnBnClicked_Open();
	afx_msg void	OnBnClicked_Close();
	afx_msg void	OnBnClicked_CloseAll();
	afx_msg void	OnBnClicked_Import();
	afx_msg void	OnBnClicked_Remove();
	afx_msg void	OnBnClicked_Rename();
	afx_msg void	OnBnClicked_SelectAll();
	afx_msg void	OnBnClicked_SelectInverse();
	afx_msg void	OnBnClicked_Rebuild();
	afx_msg void	OnBnClicked_RebuildAs();
	afx_msg void	OnBnClicked_RebuildAll();
	afx_msg void	OnBnClicked_Convert();
	afx_msg void	OnBnClicked_Merge();
	afx_msg void	OnBnClicked_Split();
	afx_msg void	OnBnClicked_Replace();
	afx_msg void	OnBnClicked_Export();
	afx_msg void	OnEnChangeEdit_Search();
	afx_msg void	OnBnClicked_Filter_Offset();
	afx_msg void	OnComboClicked_Filter_Offset();
	afx_msg void	OnEnChange_Filter_Offset();
	afx_msg void	OnBnClicked_Filter_Size();
	afx_msg void	OnComboClicked_Filter_Size();
	afx_msg void	OnEnChange_Filter_Size();
	afx_msg void	OnBnClicked_Filter_RWVersion();
	afx_msg void	OnComboClicked_Filter_RWVersion();
	afx_msg void	OnBnClicked_ExportVia();
	afx_msg void	OnBnClicked_Sort();
	afx_msg void	OnBnClicked_RemoveVia();
	afx_msg void	OnBnClicked_ImportVia();
	afx_msg void	OnBnClicked_SearchInAllOpenedFiles();
};
