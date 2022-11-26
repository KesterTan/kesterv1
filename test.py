// Component to display basic vendor information including vendor name, logo, username, etc.
import React from "react";
import {
  Grid,
  Avatar,
  Typography,
  Card,
  useTheme,
  Button,
  createStyles,
  makeStyles,
  Theme,
  Box,
} from "@material-ui/core";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { getImageURL } from "../../services/api";

type IssuerProps = {
  buyZuzUrl: string;
  slogan: string;
  logo: string;
  businessName: string;
  handle: string;
  isPublicMarketplace: boolean;
  zuzOwned: number;
  bio: string;
  canSellZUZ: boolean;
};

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    campaignDetailName: {
      fontSize: "2.17rem",
      color: "#0071BC",
      textAlign: "center",
    },

    campaignDetailHandle: {
      fontSize: "1.25rem",
      color: "#00A99D",
    },

    campaignSlogan: {
      fontSize: "1.15rem",
      fontStyle: "italic",
      display: "flex",
      justifyContent: "center",
    },
    primary: {
      marginTop: 20,
    },
    store: {
      display: "flex",
      justifyContent: "center",
      minWidth: "40%",
      maxWidth: "40%",
      justify: "center",
    },
    campaignDetailText: {
      fontStyle: "italic",
    },
    campaignDetailSub: {
    },
    large: {
      width: theme.spacing(50),
      padding: theme.spacing(2),
      height: theme.spacing(20),
      textAlign: "center",
      "& img": {
        objectFit: "contain"
      },
      maxWidth: "100%"
    },
    actionButtons: {
      marginBottom: 10,
      borderRadius: 100,
    },
    contentCard: {
      padding: theme.spacing(4),
      height: "100%",
    }
  })
);

function IssuerInfo(props: IssuerProps) {
  const theme = useTheme();
  const classes = useStyles();

  return (
    <>
      <Grid item xs={12} md={10}>
        <Grid
            container
            alignItems="center"
            justify="center"
            spacing={2}
            direction="column"
          >
            <Grid item xs={12}>
            {props.logo ? (
              <Avatar 
                variant="rounded"
                src={getImageURL(props.logo)}
                className={classes.large}
            />
            ) : (
              <FontAwesomeIcon
                icon={["far", "store"]}
                color={theme.palette.primary.main}
                size="7x"
              />
            )}
          </Grid>
        </Grid>
        <Grid
          container
          alignItems="center"
          justify="space-between"
          spacing={2}
          direction="column"
        >
          <Grid item xs={12} md={12} >
            <Typography 
              variant="h1" 
              className={classes.campaignDetailName}
            >
              {props.businessName}
            </Typography>
            <Typography
              align="center"
              variant="h2"
              className={classes.campaignDetailHandle}
              gutterBottom
            >
              @{props.handle}
            </Typography>

          </Grid>

          <Grid item xs={12} md={4} style={{ width: "100%" }} >
            {props.canSellZUZ && (
              <Button
                className={classes.actionButtons}
                variant="contained"
                size="large"
                color="primary"
                fullWidth
                onClick={() => window.open(props.buyZuzUrl, "_blank")}
              >
                Buy ZUZ
              </Button>
            )}
          </Grid>

          <Grid item xs={12} container
            alignItems="center"
            justify="center"
            className={classes.campaignSlogan}
          >
            <Typography
              align="center"
              variant="h2"
              className={classes.campaignSlogan}
              gutterBottom
            >
              {props.slogan}
            </Typography>      
          </Grid>
        </Grid>
      </Grid>
      
      
      <Grid item xs={12} md={6}>
        <Grid container spacing={2}>
          {!props.isPublicMarketplace && (
            <Grid item xs={12} >
              <Card className={classes.contentCard}>
                <Typography
                  className={classes.campaignDetailText}
                  align="center"
                >
                  You own:
                </Typography>
                <Typography
                  className={classes.campaignDetailSub}
                  align="center"
                >
                  {Math.ceil(props.zuzOwned * 100)/100}
                </Typography>
                <Typography
                  className={classes.campaignDetailText}
                  align="center"
                >
                  ZUZ accepted here
                </Typography>
              </Card>
            </Grid>
          )}

          {/* <Grid item xs={props.isPublicMarketplace ? 12 : 6}>
            <Card className={classes.contentCard}>
              <Typography className={classes.campaignDetailText} align="center">
                Find {props.businessName}:
              </Typography>
              <Box justifyContent="center" display="flex">
                 TODO:add issuer website url here
                <a href={"https://zuzlab.com"}>
                  <FontAwesomeIcon icon={["far", "globe"]} size="3x" />
                </a>
              </Box>
            </Card>
          </Grid> */}
          <Grid item xs={12}>
            <Card className={classes.contentCard}>
                {/* <Typography className={classes.campaignDetailText} variant="h6">
                  {props.businessName}'s Story:{" "}
                </Typography> */}
                <Typography 
                className={classes.campaignDetailText} 
                variant="h6" 
                >
                  Our Story:{" "}
                </Typography>
              <Typography className={classes.campaignDetailSub}>
                {props.bio}
              </Typography>
            </Card>
          </Grid>
        </Grid>
      </Grid>
    </>
  );
}

export default IssuerInfo;
